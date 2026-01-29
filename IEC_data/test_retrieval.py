from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_DB_PATH = "./faiss_db"
EMBEDDING_MODEL = "/root/autodl-tmp/models/bge-base-zh-v1.5"


def main():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True}
    )

    print("[INFO] Loading vector store...")
    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    query = "人脸伪造检测有哪些常用方法？"
    print(f"\n[QUERY] {query}\n")

    docs = vectorstore.similarity_search(query, k=3)

    for i, doc in enumerate(docs):
        print(f"----- Result {i+1} -----")
        print(f"Source: {doc.metadata.get('source')}")
        print(doc.page_content[:300])
        print()


if __name__ == "__main__":
    main()
