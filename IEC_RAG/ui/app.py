import gradio as gr

from rag.qa_engine import QAEngine
from image.image_manager import ImageManager
import config

# ---------- 初始化核心组件 ----------
qa_engine = QAEngine(
    llm_model_path=config.QWEN_MODEL_PATH,
    embedding_model_path=config.EMBEDDING_MODEL,
    vector_db_path=config.VECTOR_DB_PATH,
    top_k=config.TOP_K,
)

image_manager = ImageManager(
    image_library_path="../IEC_data/image_library.json"
)

# ---------- 业务逻辑 ----------
def rag_chat(query: str, history):
    if not query.strip():
        return "", "", [], history

    # 将历史注入 QAEngine
    qa_engine.conversation_history = history.copy()

    result = qa_engine.answer(query)
    answer = result["answer"]
    refs = "\n".join([f"- {src}" for src in result["sources"]])
    images_info = image_manager.match_images_from_text(answer)
    image_paths = [img["path"] for img in images_info]

    # 返回新的历史
    new_history = qa_engine.conversation_history.copy()

    return answer, refs, image_paths, new_history

def reset_chat():
    qa_engine.reset_history()
    return "", "", [], []

# ---------- Gradio UI ----------
with gr.Blocks(title="IEC-RAG 学术问答系统") as demo:
    gr.Markdown(
        """
        # 📚 IEC-RAG 学术问答系统
        - 本系统基于 **本地 Qwen 大模型**
        - 支持 **中文学术文献 RAG**
        - 可自动匹配并展示相关图片
        """
    )

    chat_history = gr.State([])  # 存储对话历史

    # 输入
    with gr.Row():
        with gr.Column(scale=3):
            query_input = gr.Textbox(
                label="请输入你的问题",
                placeholder="例如：人脸伪造检测有哪些常用方法？",
                lines=3
            )
            submit_btn = gr.Button("🔍 提问")
            reset_btn = gr.Button("🔄 重置对话")

    # 输出
    with gr.Row():
        with gr.Column(scale=5):
            answer_output = gr.Textbox(label="模型回答", lines=12)
            refs_output = gr.Textbox(label="引用文档", lines=6)
        with gr.Column(scale=5):
            image_gallery = gr.Gallery(
                label="相关图片",
                columns=3,
                elem_id="image-gallery",
            )

    # 绑定事件
    submit_btn.click(
        fn=rag_chat,
        inputs=[query_input, chat_history],
        outputs=[answer_output, refs_output, image_gallery, chat_history]
    )

    reset_btn.click(
        fn=reset_chat,
        inputs=[],
        outputs=[answer_output, refs_output, image_gallery, chat_history]
    )

# ---------- 自定义 CSS ----------
custom_css = """
<style>
#image-gallery img {
    object-fit: contain;
    width: 100%;
    height: auto;
}
</style>
"""

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, inline_styles=custom_css)
