from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorManager:
    def __init__(
        self,
        embedding_model_path: str,
        vector_db_path: str,
    ):
        """
        向量库管理器
        """
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model_path
        )

        self.vectorstore = FAISS.load_local(
            vector_db_path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )

    def search(self, query: str, top_k: int = 3):
        """
        相似度检索
        """
        return self.vectorstore.similarity_search(query, k=top_k)
