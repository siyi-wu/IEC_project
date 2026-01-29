# main.py

from ui.app import demo
import config

if __name__ == "__main__":
    # 启动 Gradio UI
    demo.launch(
        server_name=config.GRADIO_SERVER_NAME,
        server_port=config.GRADIO_SERVER_PORT,
        allowed_paths=["/root/autodl-tmp/IEC_data/images"]
    )
