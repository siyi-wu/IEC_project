import json
from pathlib import Path
from typing import List, Dict


class ImageManager:
    def __init__(self, image_library_path: str):
        """
        image_library_path: image_library.json 的路径（支持相对路径）
        """
        # 将输入路径转为 Path 对象，并立即解析为绝对路径（关键！）
        self.image_library_path = Path(image_library_path).resolve()
        self.image_root = self.image_library_path.parent

        # 检查文件是否存在（友好报错）
        if not self.image_library_path.exists():
            raise FileNotFoundError(
                f"Image library file not found at: {self.image_library_path}\n"
                "Please check the path and ensure the file exists."
            )

        with open(self.image_library_path, "r", encoding="utf-8") as f:
            self.image_library = json.load(f)

    def match_images_from_text(
        self,
        text: str,
        max_images: int = 3
    ) -> List[Dict]:
        """
        根据输入文本（问题或回答）匹配相关图片
        """
        matched = []

        for key, item in self.image_library.items():
            keywords = item.get("similar_word", [])
            description = item.get("description", "")
            image_path = self.image_root / item.get("path", "")

            for kw in keywords:
                if kw in text:
                    matched.append({
                        "key": key,
                        "path": str(image_path),
                        "description": description,
                        "matched_word": kw
                    })
                    break  # 一个图片命中一次即可

            if len(matched) >= max_images:
                break

        return matched
