# =======================
# 模型路径
# =======================
QWEN_MODEL_PATH = "../../models/qwen2.5-7b"  # 本地 Qwen
EMBEDDING_MODEL = "../../models/bge-base-zh-v1.5"  # 中文向量模型

# =======================
# 向量库路径
# =======================
VECTOR_DB_PATH = "../IEC_data/faiss_db"

# =======================
# RAG 参数
# =======================
TOP_K = 3  # 检索 top K 文档

# =======================
# Image 库路径
# =======================
IMAGE_LIBRARY_PATH = "../IEC_data/image_library.json"

# =======================
# Gradio UI 参数
# =======================
GRADIO_SERVER_NAME = "0.0.0.0"
GRADIO_SERVER_PORT = 7860
