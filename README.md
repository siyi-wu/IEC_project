# 使用说明
- 运行`main.py`即可

## 构建向量索引说明

- 脚本位置：`IEC_project/IEC_data/build_vectorstore.py`
- 默认文档列表：`src_files/doc250827.txt`
- 默认向量库保存位置：`IEC_project/IEC_data/faiss_db`
- 默认嵌入模型：`models/bge-base-zh-v1.5`

命令行参数（可选，不必每次都填）：

- `--doc-list PATH`：指定文档列表文件（每行一个 markdown 路径）。默认使用 `src_files/doc250827.txt`。
- `--vector-db PATH`：指定向量库目录（默认 `IEC_project/IEC_data/faiss_db`）。
- `--model PATH`：嵌入模型路径（默认 `models/bge-base-zh-v1.5`）。
- `--rebuild`：若指定则删除已有向量库并从头重建。
- `--batch-size N`：分批大小，默认 `256`（按 chunk 数计）。用于控制显存/内存峰值。
- `--save-every N`：每处理 N 个批次保存一次索引，默认 `5`。
- `--device {cpu,cuda}`：嵌入模型运行设备，默认 `cuda`。

使用示例：

```
python IEC_data/build_vectorstore.py --doc-list ../../src_files/doc250827.txt --batch-size 512
python IEC_data/build_vectorstore.py --rebuild --device cpu
```

备注：脚本会把 `doc_list` 中的相对路径以该列表文件所在目录为基准解析，并在索引中保存解析后的绝对 `source` 路径。

## WSY RAG
- 代码已经分模块构建完成。新功能可以新建文件夹，放置源代码。最终目的是运行`main.py`可以直接跑通整个工程。
- 需要在`IEC_project`的同级目录下新建`models`文件夹，下载`bge-base-zh-v1.5`和`qwen2.5-7b`模型