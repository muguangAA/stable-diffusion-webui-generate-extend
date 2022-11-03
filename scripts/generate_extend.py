import gradio as gr
from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as txt2img:
        with gr.Row():
            prompt = gr.Textbox(label="Prompt", show_label=False, lines=2,
                                placeholder="Prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                value="(best quality:1.9),(masterpiece:1.2),(highres),extremely detailed CG unity 8K wallpaper,\n"
                                      "(ultra-detailed:1.2),(best illustration:1.2),(an extremely delicate and beautiful),\n"
                                )

        with gr.Row():
            negative_prompt = gr.Textbox(label="Negative prompt", show_label=False,
            lines=2,
            placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
            value="lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit,"
                  " fewer digits, cropped, worst quality, low quality, normal quality,"
                  " jpeg artifacts, username, blurry, artist name, bad feet, penis"
                                         )

    return (txt2img, "图片生成扩展", "生成扩展"),


script_callbacks.on_ui_tabs(on_ui_tabs)
