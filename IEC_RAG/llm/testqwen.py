from qwen_wrapper import QwenWrapper

MODEL_PATH = "/root/autodl-tmp/models/qwen2.5-7b"

llm = QwenWrapper(MODEL_PATH)

prompt = "请用一句话解释什么是对极几何。"
answer = llm.generate(prompt)

print("模型输出：")
print(answer)
