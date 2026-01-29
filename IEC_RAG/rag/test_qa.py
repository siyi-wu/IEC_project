# rag/test_qa.py

from rag.qa_engine import QAEngine

engine = QAEngine(
    llm_model_path="/root/autodl-tmp/models/qwen2.5-7b",
    embedding_model_path="/root/autodl-tmp/models/bge-base-zh-v1.5",
    vector_db_path="/root/autodl-tmp/IEC_data/faiss_db",
    top_k=3,
)

result = engine.answer("人脸伪造检测有哪些常用方法？")

print("\n===== 回答 =====\n")
print(result["answer"])

print("\n===== 引用 =====\n")
for src in result["sources"]:
    print(src)
