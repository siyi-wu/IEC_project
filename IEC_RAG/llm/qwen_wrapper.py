import torch
import re
from transformers import AutoTokenizer, AutoModelForCausalLM


class QwenWrapper:
    def __init__(self, model_path: str, device: str = "auto"):
        print(f"[QwenWrapper] Loading tokenizer from {model_path}")
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True
        )

        print(f"[QwenWrapper] Loading model from {model_path}")
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            torch_dtype=torch.float16,
            device_map="auto" if device == "auto" else None
        )

        self.model.eval()
        print("[QwenWrapper] Model loaded successfully")

    def generate(
        self,
        prompt: str,
        max_new_tokens: int = 512,
        temperature: float = 0.7,
        show_thoughts: bool = False
    ) -> str:
        """
        使用 Qwen Chat Template 的标准生成接口
        """

        messages = [
            {"role": "user", "content": prompt}
        ]

        input_ids = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.model.device)

        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                max_new_tokens=max_new_tokens,
                do_sample=temperature > 0,
                temperature=temperature,
                top_p=0.9,
                eos_token_id=self.tokenizer.eos_token_id
            )

        # ⚠️ 关键：只取新生成的部分
        generated_ids = output_ids[0][input_ids.shape[-1]:]
        answer = self.tokenizer.decode(
            generated_ids,
            skip_special_tokens=True
        ).strip()

        if not show_thoughts:
            answer = self._remove_thoughts(answer)

        return answer

    @staticmethod
    def _remove_thoughts(text: str) -> str:
        return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
