import gradio as gr
from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as txt2img:
        with gr.Row():
            prompt = gr.Textbox(label="Prompt", show_label=False, lines=2,
                                placeholder="Prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                value="(best quality:1.9),(masterpiece:1.2),(highres),extremely detailed CG unity 8K wallpaper,\n"
                                      "(ultra-detailed:1.2),(best illustration:1.2),(an extremely delicate and beautiful),\n"
                                    "(loli:1.5),(cute girl:1.5),small breasts,\n"
                                      "(heart-shaped pupils),(beautiful detailed eyes)"
                                )

        with gr.Row():
            negative_prompt1 = gr.Textbox(label="Negative prompt1", show_label=False,
            lines=2,
            placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
            value="lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit,"
                  " fewer digits, cropped, worst quality, low quality, normal quality,"
                  " jpeg artifacts, username, blurry, artist name, bad feet, penis"
                                         )

        with gr.Row():
            negative_prompt2 = gr.Textbox(label="Negative prompt2", show_label=False,
            lines=2,
            placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
            value="multiple breasts, (mutated hands and fingers:1.5 ), (long body :1.3), (mutation, poorly drawn "
                  ":1.2) , black-white, bad anatomy, liquid body, liquid tongue, disfigured, malformed, mutated, "
                  "anatomical nonsense, text font ui, error, malformed hands, long neck, blurred, lowers, lowres, "
                  "bad anatomy, bad proportions, bad shadow, uncoordinated body, unnatural body, fused breasts, "
                  "bad breasts, huge breasts, poorly drawn breasts, extra breasts, liquid breasts, heavy breasts, "
                  "missing breasts, huge haunch, huge thighs, huge calf, bad hands, fused hand, missing hand, "
                  "disappearing arms, disappearing thigh, disappearing calf, disappearing legs, fused ears, bad ears, "
                  "poorly drawn ears, extra ears, liquid ears, heavy ears, missing ears, fused animal ears, "
                  "bad animal ears, poorly drawn animal ears, extra animal ears, liquid animal ears, heavy animal "
                  "ears, missing animal ears, text, ui, error, missing fingers, missing limb, fused fingers, "
                  "one hand with more than 5 fingers, one hand with less than 5 fingers, one hand with more than 5 "
                  "digit, one hand with less than 5 digit, extra digit, fewer digits, fused digit, missing digit, "
                  "bad digit, liquid digit, colorful tongue, black tongue, cropped, watermark, username, blurry, "
                  "JPEG artifacts, signature, 3D, 3D game, 3D game scene, 3D character, malformed feet, extra feet, "
                  "bad feet, poorly drawn feet, fused feet, missing feet, extra shoes, bad shoes, fused shoes, "
                  "more than two shoes, poorly drawn shoes, bad gloves, poorly drawn gloves, fused gloves, bad cum, "
                  "poorly drawn cum, fused cum, bad hairs, poorly drawn hairs, fused hairs, big muscles, ugly, "
                  "bad face, fused face, poorly drawn face, cloned face, big face, long face, bad eyes, fused eyes "
                  "poorly drawn eyes, extra eyes, malformed limbs, more than 2 nipples,missing nipples, "
                  "different nipples, fused nipples, bad nipples, poorly drawn nipples, black nipples, "
                  "colorful nipples, gross proportions. short arm, (((missing arms))), missing thighs, missing calf, "
                  "missing legs, mutation, duplicate, morbid, mutilated, poorly drawn hands, more than 1 left hand, "
                  "more than 1 right hand, deformed, (blurry), disfigured, missing legs, extra arms, extra thighs, "
                  "more than 2 thighs, extra calf, fused calf, extra legs, bad knee, extra knee, more than 2 legs, "
                  "bad tails, bad mouth, fused mouth, poorly drawn mouth, bad tongue, tongue within mouth, "
                  "too long tongue, black tongue, big mouth, cracked mouth, bad mouth, dirty face, dirty teeth, "
                  "dirty pantie, fused pantie, poorly drawn pantie, fused cloth, poorly drawn cloth, bad pantie, "
                  "yellow teeth, thick lips, bad cameltoe, colorful cameltoe, bad asshole, poorly drawn asshole, "
                  "fused asshole, missing asshole, bad anus, bad pussy, bad crotch, bad crotch seam, fused anus, "
                  "fused pussy, fused anus, fused crotch, poorly drawn crotch, fused seam, poorly drawn anus, "
                  "poorly drawn pussy, poorly drawn crotch, poorly drawn crotch seam, bad thigh gap, missing thigh "
                  "gap, fused thigh gap, liquid thigh gap, poorly drawn thigh gap, poorly drawn anus, bad collarbone, "
                  "fused collarbone, missing collarbone, liquid collarbone, strong girl, obesity, worst quality, "
                  "low quality, normal quality, liquid tentacles, bad tentacles, poorly drawn tentacles, "
                  "split tentacles, fused tentacles, missing clit, bad clit, fused clit, colorful clit, black clit, "
                  "liquid clit, QR code, bar code, censored, safety panties, safety knickers, beard, furry ,pony, "
                  "pubic hair, mosaic, excrement, faeces, shit, futa, testis,penis"
                                         )

        with gr.Row():
            negative_prompt3 = gr.Textbox(label="Negative prompt3", show_label=False,
                                         lines=2,
                                         placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                         value="multiple_breasts, (mutated_hands_and_fingers:1.5), (long_body:1.3), "
                                               "(mutation, poorly_drawn:1.2), black-white, bad_anatomy, liquid_body, "
                                               "liquid_tongue, disfigured, malformed, mutated, anatomical_nonsense, "
                                               "text_font_ui, malformed_hands, long_neck, blurred, lowers, lowres, "
                                               "bad_anatomy, bad_proportions, uncoordinated_body, black-white, "
                                               "unnatural_body, fused_breasts, bad_breasts, huge_breasts, "
                                               "poorly_drawn_breasts, extra_breasts, liquid_breasts, heavy_breasts, "
                                               "missing_breasts, huge_haunch, huge_thighs, huge_calf, bad_hands, "
                                               "fused_hand, missing_hand, disappearing_arms, disappearing_thigh, "
                                               "disappearing_calf, disappearing_legs, fused_ears, bad_ears, "
                                               "poorly_drawn_ears, extra_ears, liquid_ears, heavy_ears, missing_ears, "
                                               "fused_animal_ears, bad_animal_ears, poorly_drawn_animal_ears, "
                                               "extra_animal_ears, liquid_animal_ears, heavy_animal_ears, "
                                               "missing_animal_ears, text, ui, error, missing_fingers, missing_limb, "
                                               "fused_fingers, one_hand_with_more_than_5_fingers, "
                                               "one_hand_with_less_than_5_fingers, one_hand_with_more_than_5_digit, "
                                               "one_hand_with_less_than_5_digit, extra_digit, fewer_digits, "
                                               "fused_digit, missing_digit, bad_digit, liquid_digit, colorful_tongue, "
                                               "black_tongue, cropped, jpeg_artifacts, signature,, malformed_feet, "
                                               "extra_feet, bad_feet, poorly_drawn_feet, fused_feet, missing_feet, "
                                               "extra_shoes, bad_shoes, fused_shoes, more_than_two_shoes, "
                                               "poorly_drawn_shoes, bad_gloves, poorly_drawn_gloves, fused_gloves, "
                                               "bad_cum, poorly_drawn_cum, fused_cum, bad_hairs, poorly_drawn_hairs, "
                                               "fused_hairs, big_muscles, ugly, bad_face, fused_face, "
                                               "poorly_drawn_face, cloned_face, big_face, long_face, bad_eyes, "
                                               "fused_eyes_poorly_drawn_eyes, extra_eyes, malformed_limbs, "
                                               "more_than_2_nipples, missing_nipples, different_nipples, "
                                               "fused_nipples, bad_nipples, poorly_drawn_nipples, black_nipples, "
                                               "colorful_nipples, gross_proportions._short_arm, (missing_arms), "
                                               "missing_thighs, missing_calf, missing_legs, mutation, duplicate,"
                                               "mutilated, poorly_drawn_hands, more_than_1_left_hand, "
                                               "more_than_1_right_hand, deformed, (blurry), disfigured, missing_legs, "
                                               "extra_arms, extra_thighs, more_than_2_thighs, extra_calf, fused_calf, "
                                               "extra_legs, bad_knee, extra_knee, more_than_2_legs, bad_tails, "
                                               "bad_mouth, fused_mouth, poorly_drawn_mouth, bad_tongue, long_tongue, "
                                               "black_tongue, big_mouth, cracked_mouth, bad_mouth,dirty_teeth, "
                                               "fused_pantie, poorly_drawn_pantie, fused_cloth, poorly_drawn_cloth, "
                                               "bad_pantie, yellow_teeth, thick_lips, bad_cameltoe, "
                                               "colorful_camelote, bad_asshole, poorly_drawn_asshole, fused_asshole, "
                                               "missing_asshole, bad_anus, bad_pussy, bad_crotch, bad_crotch_seam, "
                                               "fused_anus, poorly_drawn_pussy, fused_pussy, poorly_drawn_anus, "
                                               "fused_anus, fused_crotch, poorly_drawn_crotch, fused_seam, "
                                               "poorly_drawn_anus, poorly_drawn_crotch, poorly_drawn_crotch_seam, "
                                               "bad_thigh_gap, missing_thigh_gap, fused_thigh_gap, liquid_thigh_gap, "
                                               "poorly_drawn_thigh_gap, poorly_drawn_anus, bad_collarbone, "
                                               "fused_collarbone, missing_collarbone, liquid_collarbone, strong_girl, "
                                               "obesity, worst_quality, low_quality, normal_quality, cbad_tentacles, "
                                               "poorly_drawn_tentacles, split_tentacles, fused_tentacles, "
                                               "missing_clit, bad_clit, fused_clit, colorful_clit, black_clit, "
                                               "liquid_clit, QR_code, bar_code, censored, safety_panties, "
                                               "safety_knickers, beard, furry, pony, pubic_hair, bar_censor,"
                                               "heart_censor, mosaic,mosaic censoring, excrement, futa, testis, "
                                               "(too_long_body:1.5), (too_long_upper_body:1.5), (ugly_body:1.2), "
                                               "c(big_head:1.1), crooked_nipples, cignature, username, blurry, penis")

    return (txt2img, "图片生成扩展", "生成扩展"),


script_callbacks.on_ui_tabs(on_ui_tabs)
