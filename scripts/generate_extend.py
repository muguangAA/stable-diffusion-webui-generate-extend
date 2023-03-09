import gradio as gr
from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as txt2img:
        with gr.Row():
            prompt1 = gr.Textbox(label="Prompt1", show_label=False, lines=5,
                                placeholder="Prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                value="highly_detailed, extremely_detailed_CG_unity_8k_wallpaper, illustration, highres, absurdres, beautiful_detailed_eyes, finely_detailed_light, highly_detail_hair,"
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
                                     '"samplerList": ["Euler", "DPM++ SDE Karras"]\n' \
                                     '}')

        with gr.Row():
            negative_prompt1 = gr.Textbox(label="Negative prompt1", show_label=False,
                                          lines=3,
                                          placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                          value="artifacts, signature, watermark, username, blurry, artist name, "
                                                "bad felowres, bad anatomy, bad hands, text, error, missing fingers, "
                                                "extra digit, fewer digits, cropped, worst quality, low quality, "
                                                "normal quality, jpeg artifacts "
                                          )

        with gr.Row():
            negative_prompt2 = gr.Textbox(label="Negative prompt3", show_label=False,
                                          lines=30,
                                          placeholder="Negative prompt (press Ctrl+Enter or Alt+Enter to generate)",
                                          value="multiple_breasts,{mutated_hands_and_fingers},{long_body},{mutation,"
                                                "poorly_drawn}_,black-white,bad_anatomy,liquid_body,liquid_tongue,"
                                                "disfigured,malformed,mutated,anatomical_nonsense,text_font_ui,error,"
                                                "malformed_hands,long_neck,blurred,lowers,lowres,bad_anatomy,"
                                                "bad_proportions,bad_shadow,uncoordinated_body,unnatural_body,"
                                                "fused_breasts,bad_breasts,huge_breasts,poorly_drawn_breasts,"
                                                "extra_breasts,liquid_breasts,heavy_breasts,missing_breasts,"
                                                "huge_haunch,huge_thighs,huge_calf,bad_hands,fused_hand,missing_hand,"
                                                "disappearing_arms,disappearing_thigh,disappearing_calf,"
                                                "disappearing_legs,fused_ears,bad_ears,poorly_drawn_ears,extra_ears,"
                                                "liquid_ears,heavy_ears,missing_ears,fused_animal_ears,"
                                                "bad_animal_ears,poorly_drawn_animal_ears,extra_animal_ears,"
                                                "liquid_animal_ears,heavy_animal_ears,missing_animal_ears,text,ui,"
                                                "error,missing_fingers,missing_limb,fused_fingers,"
                                                "one_hand_with_more_than_5_fingers,one_hand_with_less_than_5_fingers,"
                                                "one_hand_with_more_than_5_digit,one_hand_with_less_than_5_digit,"
                                                "extra_digit,fewer_digits,fused_digit,missing_digit,bad_digit,"
                                                "liquid_digit,colorful_tongue,black_tongue,cropped,watermark,"
                                                "username,blurry,JPEG_artifacts,signature,3D,3D_game,3D_game_scene,"
                                                "3D_character,malformed_feet,extra_feet,bad_feet,poorly_drawn_feet,"
                                                "fused_feet,missing_feet,extra_shoes,bad_shoes,fused_shoes,"
                                                "more_than_two_shoes,poorly_drawn_shoes,bad_gloves,"
                                                "poorly_drawn_gloves,fused_gloves,bad_cum,poorly_drawn_cum,fused_cum,"
                                                "bad_hairs,poorly_drawn_hairs,fused_hairs,big_muscles,ugly,bad_face,"
                                                "fused_face,poorly_drawn_face,cloned_face,big_face,long_face,"
                                                "bad_eyes,fused_eyes_poorly_drawn_eyes,extra_eyes,malformed_limbs,"
                                                "more_than_2_nipples,missing_nipples,different_nipples,fused_nipples,"
                                                "bad_nipples,poorly_drawn_nipples,black_nipples,colorful_nipples,"
                                                "gross_proportions._short_arm,{{{missing_arms}}},missing_thighs,"
                                                "missing_calf,missing_legs,mutation,duplicate,morbid,mutilated,"
                                                "poorly_drawn_hands,more_than_1_left_hand,more_than_1_right_hand,"
                                                "deformed,{blurry},disfigured,missing_legs,extra_arms,extra_thighs,"
                                                "more_than_2_thighs,extra_calf,fused_calf,extra_legs,bad_knee,"
                                                "extra_knee,more_than_2_legs,bad_tails,bad_mouth,fused_mouth,"
                                                "poorly_drawn_mouth,bad_tongue,tongue_within_mouth,too_long_tongue,"
                                                "black_tongue,big_mouth,cracked_mouth,bad_mouth,dirty_face,"
                                                "dirty_teeth,dirty_pantie,fused_pantie,poorly_drawn_pantie,"
                                                "fused_cloth,poorly_drawn_cloth,bad_pantie,yellow_teeth,thick_lips,"
                                                "bad_cameltoe,colorful_cameltoe,bad_asshole,poorly_drawn_asshole,"
                                                "fused_asshole,missing_asshole,bad_anus,bad_pussy,bad_crotch,"
                                                "bad_crotch_seam,fused_anus,fused_pussy,fused_anus,fused_crotch,"
                                                "poorly_drawn_crotch,fused_seam,poorly_drawn_anus,poorly_drawn_pussy,"
                                                "poorly_drawn_crotch,poorly_drawn_crotch_seam,bad_thigh_gap,"
                                                "missing_thigh_gap,fused_thigh_gap,liquid_thigh_gap,"
                                                "poorly_drawn_thigh_gap,poorly_drawn_anus,bad_collarbone,"
                                                "fused_collarbone,missing_collarbone,liquid_collarbone,strong_girl,"
                                                "obesity,worst_quality,low_quality,normal_quality,liquid_tentacles,"
                                                "bad_tentacles,poorly_drawn_tentacles,split_tentacles,"
                                                "fused_tentacles,missing_clit,bad_clit,fused_clit,colorful_clit,"
                                                "black_clit,liquid_clit,QR_code,bar_code,censored,safety_panties,"
                                                "safety_knickers,beard,furry_,pony,pubic_hair,mosaic,excrement,"
                                                "faeces,shit,futa,testis")

    return (txt2img, "图片生成扩展", "生成扩展"),


script_callbacks.on_ui_tabs(on_ui_tabs)
