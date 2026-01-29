import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


DOC_LIST_PATH = "./doc250827.txt"
VECTOR_DB_PATH = "./faiss_db"
EMBEDDING_MODEL = "/root/autodl-tmp/models/bge-base-zh-v1.5"

def load_md_documents(doc_list_path):
    documents = []

    with open(doc_list_path, "r", encoding="utf-8") as f:
        md_paths = [line.strip() for line in f if line.strip()]

    for md_path in md_paths:
        if not os.path.exists(md_path):
            print(f"[WARN] File not found: {md_path}")
            continue

        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append(
            Document(
                page_content=text,
                metadata={"source": md_path}
            )
        )

    print(f"[INFO] Loaded {len(documents)} markdown documents")
    return documents


def main():
    print("[INFO] Loading markdown files...")
    documents = load_md_documents(DOC_LIST_PATH)

    print("[INFO] Splitting documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)
    print(f"[INFO] Total chunks: {len(chunks)}")

    print("[INFO] Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True}
    )

    print("[INFO] Building FAISS vector store...")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    print("[INFO] Saving vector store...")
    vectorstore.save_local(VECTOR_DB_PATH)

    print("[DONE] Vector store built successfully!")


if __name__ == "__main__":
    main()
