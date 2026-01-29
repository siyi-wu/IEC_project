import json
from pathlib import Path
from typing import List, Dict


class ImageManager:
    def __init__(self, image_library_path: str):
        """
        image_library_path: image_libarary.json 的路径
        """
        self.image_library_path = Path(image_library_path)
        self.image_root = self.image_library_path.parent

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
