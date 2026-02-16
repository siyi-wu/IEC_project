import os
import hashlib
import argparse
import shutil
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


DOC_LIST_PATH = "../../src_files/markdown_filenames_with_suffix.txt"
VECTOR_DB_PATH = "./faiss_db"
EMBEDDING_MODEL = "/root/autodl-tmp/models/bge-base-zh-v1.5"


def parse_args():
    p = argparse.ArgumentParser(description="Build or update FAISS vectorstore from markdown list")
    p.add_argument("--doc-list", default=DOC_LIST_PATH, help="Path to file listing markdown files (one per line)")
    p.add_argument("--vector-db", default=VECTOR_DB_PATH, help="Directory to save/load FAISS index")
    p.add_argument("--model", default=EMBEDDING_MODEL, help="Embedding model path")
    p.add_argument("--rebuild", action="store_true", help="Force rebuild: delete existing index and recreate")
    p.add_argument("--batch-size", type=int, default=256, help="Number of chunks to process per batch")
    p.add_argument("--save-every", type=int, default=5, help="Save index every N batches")
    p.add_argument("--device", choices=["cpu", "cuda"], default="cuda", help="Device for embedding model")
    return p.parse_args()

def load_md_documents(doc_list_path):
    documents = []

    base_dir = os.path.dirname(os.path.abspath(doc_list_path))

    with open(doc_list_path, "r", encoding="utf-8") as f:
        md_paths = [line.strip() for line in f if line.strip()]

    for md_path in md_paths:
        # 如果是相对路径，则以 doc_list 文件所在目录为基准解析
        if not os.path.isabs(md_path):
            md_path_resolved = os.path.normpath(os.path.join(base_dir, md_path))
        else:
            md_path_resolved = md_path

        if not os.path.exists(md_path_resolved):
            print(f"[WARN] File not found: {md_path_resolved}")
            continue

        with open(md_path_resolved, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append(
            Document(
                page_content=text,
                metadata={"source": md_path_resolved}
            )
        )

    print(f"[INFO] Loaded {len(documents)} markdown documents")
    return documents


def main():
    args = parse_args()

    doc_list = args.doc_list
    vector_db = args.vector_db
    embedding_model = args.model
    rebuild = args.rebuild
    batch_size = max(1, args.batch_size)
    save_every = max(1, args.save_every)
    device = args.device

    print(f"[INFO] Loading markdown files from {doc_list}...")
    documents = load_md_documents(doc_list)

    print("[INFO] Splitting documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)
    print(f"[INFO] Total chunks: {len(chunks)}")

    # 为每个 chunk 计算内容哈希，便于去重
    for doc in chunks:
        content = doc.page_content or ""
        h = hashlib.sha256(content.encode("utf-8")).hexdigest()
        doc.metadata["chunk_hash"] = h

    print(f"[INFO] Loading embedding model {embedding_model} on {device}...")
    embeddings = HuggingFaceEmbeddings(
        model_name=embedding_model,
        model_kwargs={"device": device},
        encode_kwargs={"normalize_embeddings": True}
    )

    print("[INFO] Building/Updating FAISS vector store (incremental + batching)...")

    vectorstore = None
    existing_hashes = set()

    # 如果要求重建，删除旧索引
    if rebuild and os.path.exists(vector_db):
        print(f"[INFO] Rebuild requested: removing existing vector DB at {vector_db}")
        try:
            shutil.rmtree(vector_db)
        except Exception as e:
            print(f"[WARN] Failed to remove {vector_db}: {e}")

    # 如果本地已有向量库，尝试加载并收集已有 chunk 的哈希用于去重
    if os.path.exists(vector_db):
        try:
            vectorstore = FAISS.load_local(vector_db, embeddings)
            try:
                for v in vectorstore.docstore._dict.values():
                    if isinstance(v, Document):
                        eh = v.metadata.get("chunk_hash")
                        if not eh:
                            eh = hashlib.sha256((v.page_content or "").encode("utf-8")).hexdigest()
                        existing_hashes.add(eh)
                    elif isinstance(v, dict):
                        eh = v.get("metadata", {}).get("chunk_hash")
                        if not eh:
                            eh = hashlib.sha256((v.get("page_content","") or "").encode("utf-8")).hexdigest()
                        existing_hashes.add(eh)
            except Exception:
                existing_hashes = set()
            print(f"[INFO] Loaded existing vectorstore with {len(existing_hashes)} known chunk hashes")
        except Exception as e:
            print(f"[WARN] Failed to load existing vectorstore: {e}. A new one will be created.")
            vectorstore = None

    # 过滤出新增的 chunks（全局过滤）
    new_chunks: List[Document] = [d for d in chunks if d.metadata.get("chunk_hash") not in existing_hashes]
    if not new_chunks:
        print("[INFO] No new chunks to add. Exiting.")
        return

    # 分批处理
    total_new = len(new_chunks)
    batches = (total_new + batch_size - 1) // batch_size
    batch_count = 0
    for i in range(0, total_new, batch_size):
        batch = new_chunks[i:i + batch_size]
        # 再次按已有哈希过滤，防止跨批重复
        batch_filtered = [d for d in batch if d.metadata.get("chunk_hash") not in existing_hashes]
        if not batch_filtered:
            continue

        if vectorstore is None:
            vectorstore = FAISS.from_documents(batch_filtered, embeddings)
            print(f"[INFO] Created new vectorstore with first batch of {len(batch_filtered)} chunks")
        else:
            vectorstore.add_documents(batch_filtered)
            print(f"[INFO] Added batch of {len(batch_filtered)} chunks to existing vectorstore")

        # 更新已存在哈希集合
        for d in batch_filtered:
            existing_hashes.add(d.metadata.get("chunk_hash"))

        batch_count += 1
        # 周期性保存
        if batch_count % save_every == 0:
            try:
                vectorstore.save_local(vector_db)
                print(f"[INFO] Saved vectorstore after {batch_count} batches")
            except Exception as e:
                print(f"[WARN] Failed to save vectorstore: {e}")

    # 最终保存
    try:
        vectorstore.save_local(vector_db)
        print(f"[DONE] Vector store built/updated successfully! Total new chunks added: {len(new_chunks)}")
    except Exception as e:
        print(f"[WARN] Failed to save final vectorstore: {e}")


if __name__ == "__main__":
    main()
