# rag/qa_engine.py

from llm.qwen_wrapper import QwenWrapper
from vector_store.vector_manager import VectorManager


class QAEngine:
    def __init__(
        self,
        llm_model_path: str,
        embedding_model_path: str,
        vector_db_path: str,
        top_k: int = 3,
        show_thoughts: bool = False,
    ):
        self.llm = QwenWrapper(llm_model_path)
        self.vector_manager = VectorManager(
            embedding_model_path=embedding_model_path,
            vector_db_path=vector_db_path,
        )
        self.top_k = top_k
        self.show_thoughts = show_thoughts

        # 会话历史，每条记录是 "用户：xxx" 或 "助手：xxx"
        self.conversation_history = []

    def build_prompt(self, query: str, docs):
        """
        构建多轮 RAG Prompt
        """
        # 历史对话
        history = "\n".join(self.conversation_history)

        # 检索文档内容
        context = "\n\n".join(
            [f"【文档{i+1}】{doc.page_content}" for i, doc in enumerate(docs)]
        )

        prompt = f"""
你是一个学术问答助手，请**仅基于给定文档内容**回答问题。
请直接给出答案，不要在回答中加“参考文档”或编号。
如果文档中没有相关信息，请回答“文档中未提及”。

【历史对话】
{history}

【文档内容】
{context}

【用户问题】
{query}

【助手回答】
"""
        return prompt.strip()

    def answer(self, query: str, show_thoughts: bool = None):
        """
        执行一次 RAG 问答，并更新历史对话
        """
        if show_thoughts is not None:
            self.show_thoughts = show_thoughts

        # 检索相关文档
        docs = self.vector_manager.search(query, self.top_k)
        prompt = self.build_prompt(query, docs)
        answer = self.llm.generate(
            prompt,
            show_thoughts=self.show_thoughts
        )

        # 去重后的 source
        sources = []
        for doc in docs:
            src = doc.metadata.get("source")
            if src not in sources:
                sources.append(src)

        # 更新会话历史
        self.conversation_history.append(f"用户：{query}")
        self.conversation_history.append(f"助手：{answer}")

        return {
            "answer": answer,
            "sources": sources,
            "docs": docs,
        }

    def reset_history(self):
        """重置多轮对话历史"""
        self.conversation_history = []
