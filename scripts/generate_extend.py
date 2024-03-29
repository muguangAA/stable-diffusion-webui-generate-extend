import gradio as gr
from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as txt2img:
        with gr.Row():
            prompt1 = gr.Textbox(label="Prompt1", show_label=False, lines=5,
                                placeholder="Prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                value="highly_detailed, extremely_detailed_CG_unity_8k_wallpaper,illustration,highres,absurdres,"
                                      "(loli:1.3),cute,girl,"
                                )

        with gr.Row():
            prompt2 = gr.Textbox(label="Prompt2", show_label=False, lines=5,
                                placeholder="Prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                value="highly_detailed,extremely_detailed_CG_unity_8k_wallpaper,illustration,highres,absurdres,\n"
                                      "(loli:1.3),(cute girl:1.4),\n"
                                      "(heart-shaped pupils:0.5),(beautiful detailed eyes)"
                                )

        with gr.Row():
            parameter = gr.Textbox(label="parameter", show_label=True,
                                   lines=20,
                                   value='{\n' \
                                     '"useTheFollowingPrompt": false,\n' \
                                     '"stepsAndScaleList": [[20, 7]],\n' \
                                     '"negative_prompt": "Default",\n' \
                                     '"pixelList": [[768,1024],[1024,768]],\n' \
                                     '"samplerList": ["DPM adaptive", "Euler", "DPM++ SDE Karras"]\n' \
                                     '}')

        with gr.Row():
            negative_prompt1 = gr.Textbox(label="Negative prompt1", show_label=False,
                                          lines=3,
                                          placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                          value="lowres, bad anatomy, bad hands, text, error, missing fingers, "
                                                "extra digit, fewer digits, cropped, worst quality, low quality, "
                                                "normal quality, jpeg artifacts,signature, watermark, username, "
                                                "blurry, artist name,bad feet"
                                          )

        with gr.Row():
            negative_prompt2 = gr.Textbox(label="Negative prompt3", show_label=False,
                                          lines=30,
                                          placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                          value="multiple breasts, (mutated hands and fingers:1.5), (long body :1.3), "
                                                "(mutation, poorly drawn :1.2), black-white, bad anatomy, "
                                                "liquid body, liquid tongue, disfigured, malformed, mutated, "
                                                "anatomical nonsense, text font ui, error, malformed hands, "
                                                "long neck, blurred, lowers, lowres, bad anatomy, bad proportions, "
                                                "bad shadow, uncoordinated body, unnatural body, fused breasts, "
                                                "bad breasts, huge breasts, poorly drawn breasts, extra breasts, "
                                                "liquid breasts, heavy breasts, missing breasts, huge haunch, "
                                                "huge thighs, huge calf, bad hands, fused hand, missing hand, "
                                                "disappearing arms, disappearing thigh, disappearing calf, "
                                                "disappearing legs, fused ears, bad ears, poorly drawn ears, "
                                                "extra ears, liquid ears, heavy ears, missing ears, fused animal "
                                                "ears, bad animal ears, poorly drawn animal ears, extra animal ears, "
                                                "liquid animal ears, heavy animal ears, missing animal ears, text, "
                                                "ui, error, missing fingers, missing limb, fused fingers, "
                                                "one hand with more than 5 fingers, one hand with less than 5 "
                                                "fingers, one hand with more than 5 digit, one hand with less than 5 "
                                                "digit, extra digit, fewer digits, fused digit, missing digit, "
                                                "bad digit, liquid digit, colorful tongue, black tongue, cropped, "
                                                "watermark, username, blurry, JPEG artifacts, signature, 3D, 3D game, "
                                                "3D game scene, 3D character, malformed feet, extra feet, bad feet, "
                                                "poorly drawn feet, fused feet, missing feet, extra shoes, bad shoes, "
                                                "fused shoes, more than two shoes, poorly drawn shoes, bad gloves, "
                                                "poorly drawn gloves, fused gloves, bad cum, poorly drawn cum, "
                                                "fused cum, bad hairs, poorly drawn hairs, fused hairs, big muscles, "
                                                "ugly, bad face, fused face, poorly drawn face, cloned face, "
                                                "big face, long face, bad eyes, fused eyes poorly drawn eyes, "
                                                "extra eyes, malformed limbs, more than 2 nipples, missing nipples, "
                                                "different nipples, fused nipples, bad nipples, poorly drawn nipples, "
                                                "black nipples, colorful nipples, gross proportions. short arm, "
                                                "(((missing arms))), missing thighs, missing calf, missing legs, "
                                                "mutation, duplicate, morbid, mutilated, poorly drawn hands, "
                                                "more than 1 left hand, more than 1 right hand, deformed, (blurry), "
                                                "disfigured, missing legs, extra arms, extra thighs, more than 2 "
                                                "thighs, extra calf, fused calf, extra legs, bad knee, extra knee, "
                                                "more than 2 legs, bad tails, bad mouth, fused mouth, poorly drawn "
                                                "mouth, bad tongue, tongue within mouth, too long tongue, "
                                                "black tongue, big mouth, cracked mouth, bad mouth, dirty face, "
                                                "dirty teeth, dirty pantie, fused pantie, poorly drawn pantie, "
                                                "fused cloth, poorly drawn cloth, bad pantie, yellow teeth, "
                                                "thick lips, bad cameltoe, colorful cameltoe, bad asshole, "
                                                "poorly drawn asshole, fused asshole, missing asshole, bad anus, "
                                                "bad pussy, bad crotch, bad crotch seam, fused anus, fused pussy, "
                                                "fused anus, fused crotch, poorly drawn crotch, fused seam, "
                                                "poorly drawn anus, poorly drawn pussy, poorly drawn crotch, "
                                                "poorly drawn crotch seam, bad thigh gap, missing thigh gap, "
                                                "fused thigh gap, liquid thigh gap, poorly drawn thigh gap, "
                                                "poorly drawn anus, bad collarbone, fused collarbone, "
                                                "missing collarbone, liquid collarbone, strong girl, obesity, "
                                                "worst quality, low quality, normal quality, liquid tentacles, "
                                                "bad tentacles, poorly drawn tentacles, split tentacles, "
                                                "fused tentacles, missing clit, bad clit, fused clit, colorful clit, "
                                                "black clit, liquid clit, QR code, bar code, censored, "
                                                "safety panties, safety knickers, beard, furry ,pony, pubic hair, "
                                                "mosaic, excrement, faeces, shit, futa, testis")

    return (txt2img, "图片生成扩展", "生成扩展"),


script_callbacks.on_ui_tabs(on_ui_tabs)
