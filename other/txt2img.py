import modules.scripts
from modules import sd_samplers
from modules.generation_parameters_copypaste import create_override_settings_dict
from modules.processing import StableDiffusionProcessing, Processed, StableDiffusionProcessingTxt2Img, \
    StableDiffusionProcessingImg2Img, process_images
from modules.shared import opts, cmd_opts
import modules.shared as shared
import modules.processing as processing
from modules.ui import plaintext_to_html
import random
from zipfile import ZipFile
import datetime
import os
from modules.sd_samplers import samplers
import json

# 背景列表
backgroundList = ['indoors', 'tatami', 'church', 'shop', 'fountain', 'classroom',
                  'street', 'chinese style architecture', 'stairs', 'flower field',
                  'underwater', 'forest', 'futon', 'spring_(season)',
                  'ocean', 'cafe', 'city', 'park', 'restaurant',
                  'outdoors', 'under table', 'winter',
                  'gym storeroom', 'public', 'on bed', 'fantasy',
                  'bedroom', 'gym storeroom', 'bathroom', 'swimming pool',
                  'garden', 'waterfall', 'beach']

describeList = ['pubic tattoo', 'pussy juice', 'pussy juice puddle', 'pussy juice trail',
                'comforting', 'exhibitionism', 'flashing', 'masturbation', 'fireworks', 'feather',
                'presenting', 'female ejaculation', 'female orgasm', 'self fondle', 'spread pussy',
                'spread anus', 'nude', 'pussy juice stain', 'flowers meadows', 'sunset', 'moon',
                "valentine", "halloween", "christmas", 'tanabata', 'cherry blossoms',
                'milking machine', 'night',
                'suggestive fluid', 'wet clothes', 'breasts out',
                'bathing', 'clothed masturbation', 'have to pee', 'peeing', 'dusk', 'fog',
                'waking up', 'breath',
                'steaming body', 'lactation',
                'nipple tweak', 'looking at viewer', 'flower', 'magic circle',
                'detailed light', 'snowflakes', 'flower petals', 'plant', 'crowd',
                'beautiful detailed sky', 'beautiful detailed water', 'dappled sunlight',
                'lying', 'sitting', 'squatting', 'panties around', 'tally',
                'armpit peek', 'skirt lift', 'shy', 'embarrass', 'star',
                'lifted by self', 'shoujo kitou-chuu',
                'panty lift', 'panty peek', 'pantyshot', 'dynamic angle' 'genshin impact',
                'frottage', 'panties peek', 'angle',
                'spread legs', 'leg up', 'legs apart', 'tiptoes', 'nipple slip', 'areola slip',
                'witch', 'angel', 'princess',
                'full-face blush', 'clothes lift', 'bra lift', 'bra peek', 'bra pull']

# 衣服列表
clothesList = [  # 上装
    'revealing clothes', 'baggy pants', 'bath towel', 'serafuku', 'kimono', 'bikini',
    'school uniform', 'pajamas', 'backless outfit', 'sleepwear', 'sweater', 'rope', 'cape', 'ribbon',
    'summer uniform', 'sailor hat', 'sailor shirt', 'coat', 'tailcoat', 'neck ring', 'uniform', 'kindergarten uniform',
    'cheerleader', 'cardigan', 'casual wear', 'heart cutout', 'corset', 'crop top', 'cropped shirt',
    'cropped vest', 'gym shirt', 'jersey', 'open kimono', 'kimono lift', 'unbuttoned shirt', 'luxuriant bra',
    'nippleless clothes', 'neckerchief', 'Miko clothing', 'poncho',
    'bikini top', 'bikini top removed', 'bra', 'no bra', 'heart pasties', 'see-through', 'downblouse',
    'bell choker', 'neckerchief', 'lolita', 'tuxedo', 'formal', 'japanese clothes', 'cheongsam',
    'loungewear', 'nightgown', 'babydoll', 'yukata', 'hanfu', 'gym uniform', 'yukata', 'sexy lingerie',
    'budget sarashi', 'shirt', 'undershirt', 'halter top', 'backless sweater', 'towel', 'hanfu',
    'hoodie', 'overcoat', 'trench coat', 'cloak', 'jacket', 'downblouse', 'wet clothes',
    'soggy clothes', 'wet shirt', 'swimsuit', 'school swimsuit', 'bell',
    'naked cape', 'scarf', 'clothes writing', 'wedding dress', 'nun gown', 'chinese clothes',
    'virgin killer sweater', 'long shirt', 'collared shirt', 'sportswear', 'ballet',
    # 下装
    'wedding dress', 'sailor', 'dress', 'miniskirt', 'skirt', 'apron', 'wedding dress',
    'socks', 'pleated skirt', 'maid', 'suspender pants', 'summer long skirt', 'bloomers',
    'shorts', 'underpants', 'white thighhighs', 'sneakers', 'bottomless',
    'gym shorts', 'leotard pull', 'ankle socks', 'sheer legwear', 'leg cutout',
    'panties', 'wet panties', 'crotch plate', 'no panties', 'pink panties', 'bow panties',
    'crotchless panties', 'string panties', 'lace-trimmed panties', 'shorts',
    'bottomless', 'asymmetrical legwear', 'loose socks', 'bubble skirt', 'crotch plate',
    'cat tail']

# 下装列表
pantsList = ['wedding dress', 'sailor', 'dress', 'miniskirt', 'skirt', 'apron', 'wedding dress',
             'socks', 'pleated skirt', 'maid', 'suspender pants', 'summer long skirt', 'bloomers',
             'shorts', 'underpants', 'white thighhighs', 'sneakers', 'bottomless',
             'gym shorts', 'leotard pull', 'ankle socks', 'sheer legwear', 'leg cutout',
             'panties', 'wet panties', 'crotch plate', 'no panties', 'pink panties', 'bow panties',
             'crotchless panties', 'string panties', 'lace-trimmed panties', 'shorts',
             'bottomless', 'asymmetrical legwear', 'loose socks', 'bubble skirt', 'crotch plate',
             'cat tail']

# 眼睛列表
eyesList = ["beautiful golden eyes", "pink eyes", "blue eyes", "red eyes"]

# 头发颜色
hairColorList = ["pink hair", "blonde hair", "sliver hair"]

# 发型
hairStyleList = ["long hair", "gradient hair", "side ponytail", "princess head", "ponytail"]

# 身体特征描述
characterPartList = ["nsfw,(finely detailed pussy)", "nsfw,(finely detailed pussy),(vaginal)",
                     "nsfw,nipples", "nsfw,nipples,(finely detailed pussy)", "nipples"]


def getString(ls):
    ans = ""
    for s in ls:
        ans += s
        ans += ","
    return ans


def getRandomBackground():
    if random.randint(1, 10) > 6:
        return ""
    return getString(random.sample(backgroundList, 1))


def getRandomClothes():
    if random.randint(1, 10) > 8:
        return ""
    return getString(random.sample(clothesList, 1))


def getRandomPants():
    if random.randint(1, 10) > 8:
        return ""
    return getString(random.sample(pantsList, 1))


def getRandomHair():
    if random.randint(1, 10) > 5:
        hair = ""
        hairColor = getString(random.sample(hairColorList, 1))
        hairStyle = getString(random.sample(hairStyleList, 1))
        hair += hairColor
        hair += hairStyle
        return hair
    return ""


def getRandomEyes():
    if random.randint(1, 10) > 5:
        return getString(random.sample(eyesList, 1))
    return ""


# 获取随机描述
def getRandomDescribe(nsfwDescribeNum, nsfwDescribeNumIsRandom, nsfwDescribeRandomWeight):
    if nsfwDescribeNum > 0:
        if nsfwDescribeNumIsRandom:
            if random.randint(1, 10) > nsfwDescribeRandomWeight:
                return ""
            else:
                return getDescribe(random.randint(1, nsfwDescribeNum))
        else:
            return getDescribe(nsfwDescribeNum)
    else:
        return ""


# 根据数量获取随机样本
def getDescribe(num):
    if num > len(describeList):
        num = len(describeList)
    return getString(random.sample(describeList, num))


# 获取随机部位
def getRandomCharacterPart(characterPartNum, characterPartNumIsRandom, characterPartRandomWeight):
    if characterPartNum > 0:
        if characterPartNumIsRandom:
            if random.randint(1, 10) > characterPartRandomWeight:
                return ""
            else:
                return getCharacterPart()
        else:
            return getCharacterPart()
    else:
        return ""


# 随机获取一个
def getCharacterPart():
    return getString(random.sample(characterPartList, 1))


def getPrompt(prompt, jsonLoad):
    randomCharacterPart = getRandomCharacterPart(2, True, 5)
    randomClothes = getRandomClothes()
    randomEyes = getRandomEyes()
    randomHair = getRandomHair()
    randomDescribe = getRandomDescribe(3, True, 5)
    randomBackground = getRandomBackground()
    s = ""
    s += randomCharacterPart + ",\n"
    s += randomEyes + ",\n"
    s += randomHair + ",\n"
    s += randomClothes + ","
    s += randomDescribe + ",\n"
    s += randomBackground + ","

    return optimizeTheFormat(s)


def optimizeTheFormat(s: str):
    # flag = 0
    # while flag != 3:

    while s.find(", ") != -1 or s.find(",,") != -1 or s.find(",\n,") != -1:
        s = s.replace(", ", ",").replace(",,", ",").replace(",\n,", ",")
    if s[len(s) - 1] == ',':
        return s[0:len(s) - 1]
    return s


def batchSave(processed, prompt, negative_prompt, steps, scale, width, height, seed, sampler):
    # 我的保存图片
    print("图片的数量：" + str(len(processed.images)))
    imageList = processed.images
    if len(imageList) > 1:
        saveImage(imageList[0], prompt, negative_prompt, steps, scale, width, height, 0, sampler)
        for i in range(1, len(imageList)):
            saveImage(imageList[i], prompt, negative_prompt, steps, scale, width, height, seed, sampler)
            seed += 1
    else:
        saveImage(imageList[0], prompt, negative_prompt, steps, scale, width, height, seed, sampler)


def saveImage(image, prompt, negative_prompt, steps, scale, width, height, seed, sampler):
    filePath = "/content/stable-diffusion-webui/images/"
    drivePath = "/content/drive/MyDrive/stable-diffusion-webui/images/"
    os.makedirs(drivePath, exist_ok=True)
    os.makedirs(filePath, exist_ok=True)

    # 获取当前时间
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 设置文件名
    baseFilename = f'{cur_time}__{sampler}__{width}x{height}__{seed}'.strip()
    suff = '.png'
    filename = filePath + baseFilename.strip()

    # 保存图片
    image.save(filename + suff)

    # 保存图片信息
    try:
        with open(filename + '.txt', 'w') as f:
            f.write(f'prompt: {prompt}\n')
            f.write(f'ne_prompt: {negative_prompt}\n')
            f.write(f'steps: {steps}\n')
            f.write(f'scale: {scale}\n')
            f.write(f'width: {width}\n')
            f.write(f'height: {height}\n')
            f.write(f'seed: {seed}\n')
            f.write(f'sampler: {sampler}\n')
    except Exception as e:
        print("failed to save imageInfo:", e)

    try:
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d")
        with ZipFile(drivePath + str(cur_time) + ".zip", "a") as handle:
            handle.write(filename + '.png')
            handle.write(filename + '.txt')
    except Exception as e:
        print("failed to save imageInfo:", e)
    finally:
        handle.close()


def txt2img(id_task: str, prompt: str, negative_prompt: str, prompt_styles, steps: int, sampler_index: int, restore_faces: bool, tiling: bool, n_iter: int, batch_size: int, cfg_scale: float, seed: int, subseed: int, subseed_strength: float, seed_resize_from_h: int, seed_resize_from_w: int, seed_enable_extras: bool, height: int, width: int, enable_hr: bool, denoising_strength: float, hr_scale: float, hr_upscaler: str, hr_second_pass_steps: int, hr_resize_x: int, hr_resize_y: int, override_settings_texts, *args):
    override_settings = create_override_settings_dict(override_settings_texts)

    jsonLoad = json.loads(negative_prompt)
    if negative_prompt == "Default":
        negative_prompt = "multiple_breasts,{mutated_hands_and_fingers},{long_body},{mutation,poorly_drawn}_,black-white,bad_anatomy,liquid_body,liquid_tongue,disfigured,malformed,mutated,anatomical_nonsense,text_font_ui,error,malformed_hands,long_neck,blurred,lowers,lowres,bad_anatomy,bad_proportions,bad_shadow,uncoordinated_body,unnatural_body,fused_breasts,bad_breasts,huge_breasts,poorly_drawn_breasts,extra_breasts,liquid_breasts,heavy_breasts,missing_breasts,huge_haunch,huge_thighs,huge_calf,bad_hands,fused_hand,missing_hand,disappearing_arms,disappearing_thigh,disappearing_calf,disappearing_legs,fused_ears,bad_ears,poorly_drawn_ears,extra_ears,liquid_ears,heavy_ears,missing_ears,fused_animal_ears,bad_animal_ears,poorly_drawn_animal_ears,extra_animal_ears,liquid_animal_ears,heavy_animal_ears,missing_animal_ears,text,ui,error,missing_fingers,missing_limb,fused_fingers,one_hand_with_more_than_5_fingers,one_hand_with_less_than_5_fingers,one_hand_with_more_than_5_digit,one_hand_with_less_than_5_digit,extra_digit,fewer_digits,fused_digit,missing_digit,bad_digit,liquid_digit,colorful_tongue,black_tongue,cropped,watermark,username,blurry,JPEG_artifacts,signature,3D,3D_game,3D_game_scene,3D_character,malformed_feet,extra_feet,bad_feet,poorly_drawn_feet,fused_feet,missing_feet,extra_shoes,bad_shoes,fused_shoes,more_than_two_shoes,poorly_drawn_shoes,bad_gloves,poorly_drawn_gloves,fused_gloves,bad_cum,poorly_drawn_cum,fused_cum,bad_hairs,poorly_drawn_hairs,fused_hairs,big_muscles,ugly,bad_face,fused_face,poorly_drawn_face,cloned_face,big_face,long_face,bad_eyes,fused_eyes_poorly_drawn_eyes,extra_eyes,malformed_limbs,more_than_2_nipples,missing_nipples,different_nipples,fused_nipples,bad_nipples,poorly_drawn_nipples,black_nipples,colorful_nipples,gross_proportions._short_arm,{{{missing_arms}}},missing_thighs,missing_calf,missing_legs,mutation,duplicate,morbid,mutilated,poorly_drawn_hands,more_than_1_left_hand,more_than_1_right_hand,deformed,{blurry},disfigured,missing_legs,extra_arms,extra_thighs,more_than_2_thighs,extra_calf,fused_calf,extra_legs,bad_knee,extra_knee,more_than_2_legs,bad_tails,bad_mouth,fused_mouth,poorly_drawn_mouth,bad_tongue,tongue_within_mouth,too_long_tongue,black_tongue,big_mouth,cracked_mouth,bad_mouth,dirty_face,dirty_teeth,dirty_pantie,fused_pantie,poorly_drawn_pantie,fused_cloth,poorly_drawn_cloth,bad_pantie,yellow_teeth,thick_lips,bad_cameltoe,colorful_cameltoe,bad_asshole,poorly_drawn_asshole,fused_asshole,missing_asshole,bad_anus,bad_pussy,bad_crotch,bad_crotch_seam,fused_anus,fused_pussy,fused_anus,fused_crotch,poorly_drawn_crotch,fused_seam,poorly_drawn_anus,poorly_drawn_pussy,poorly_drawn_crotch,poorly_drawn_crotch_seam,bad_thigh_gap,missing_thigh_gap,fused_thigh_gap,liquid_thigh_gap,poorly_drawn_thigh_gap,poorly_drawn_anus,bad_collarbone,fused_collarbone,missing_collarbone,liquid_collarbone,strong_girl,obesity,worst_quality,low_quality,normal_quality,liquid_tentacles,bad_tentacles,poorly_drawn_tentacles,split_tentacles,fused_tentacles,missing_clit,bad_clit,fused_clit,colorful_clit,black_clit,liquid_clit,QR_code,bar_code,censored,safety_panties,safety_knickers,beard,furry_,pony,pubic_hair,mosaic,excrement,faeces,shit,futa,testis"
    useTheFollowingPrompt = jsonLoad["useTheFollowingPrompt"]

    if useTheFollowingPrompt is not None and useTheFollowingPrompt:
        print("仅生成图片")
        stepsAndScaleList = jsonLoad["stepsAndScaleList"]
        pixelList = jsonLoad["pixelList"]
        samplerList = jsonLoad["samplerList"]
        for n in range(1000):
            seed = processing.get_fixed_seed(seed)
            newPrompt = getPrompt(prompt, jsonLoad)
            for stepsAndScale in stepsAndScaleList:
                newSteps = stepsAndScale[0]
                newScale = stepsAndScale[1]

                for pixel in pixelList:
                    newWidth = pixel[0]
                    newHeight = pixel[1]

                    for sampler in samplerList:
                        print(
                            f"当前第{n + 1}张，sampler:{sampler}, seed:{seed}, prompt: {newPrompt}")
                        p = StableDiffusionProcessingTxt2Img(
                            sd_model=shared.sd_model,
                            outpath_samples=opts.outdir_samples or opts.outdir_txt2img_samples,
                            outpath_grids=opts.outdir_grids or opts.outdir_txt2img_grids,
                            prompt=newPrompt,
                            styles=prompt_styles,
                            negative_prompt=negative_prompt,
                            seed=seed,
                            subseed=subseed,
                            subseed_strength=subseed_strength,
                            seed_resize_from_h=seed_resize_from_h,
                            seed_resize_from_w=seed_resize_from_w,
                            seed_enable_extras=seed_enable_extras,
                            sampler_name=sampler,
                            batch_size=batch_size,
                            n_iter=n_iter,
                            steps=newSteps,
                            cfg_scale=newScale,
                            width=newWidth,
                            height=newHeight,
                            restore_faces=restore_faces,
                            tiling=tiling,
                            enable_hr=enable_hr,
                            denoising_strength=denoising_strength if enable_hr else None,
                            hr_scale=hr_scale,
                            hr_upscaler=hr_upscaler,
                            hr_second_pass_steps=hr_second_pass_steps,
                            hr_resize_x=hr_resize_x,
                            hr_resize_y=hr_resize_y,
                            override_settings=override_settings,
                        )

                        p.scripts = modules.scripts.scripts_txt2img
                        p.script_args = args

                        if cmd_opts.enable_console_prompts:
                            print(f"\ntxt2img: {prompt}", file=shared.progress_print_out)

                        processed = modules.scripts.scripts_txt2img.run(p, *args)

                        if processed is None:
                            processed = process_images(p)

                        p.close()

                        shared.total_tqdm.clear()

                        generation_info_js = processed.js()
                        if opts.samples_log_stdout:
                            print(generation_info_js)

                        if opts.do_not_show_images:
                            processed.images = []

                        batchSave(processed, newPrompt, negative_prompt, newSteps, newScale, newWidth,
                                  newHeight, seed,
                                  sampler)
    else:
        print("生成且返回")
        print("prompt: " + prompt)
        sampler = samplers[sampler_index].name
        print("sampler: " + sampler)
        seed = processing.get_fixed_seed(seed)
        p = StableDiffusionProcessingTxt2Img(
            sd_model=shared.sd_model,
            outpath_samples=opts.outdir_samples or opts.outdir_txt2img_samples,
            outpath_grids=opts.outdir_grids or opts.outdir_txt2img_grids,
            prompt=prompt,
            styles=prompt_styles,
            negative_prompt=negative_prompt,
            seed=seed,
            subseed=subseed,
            subseed_strength=subseed_strength,
            seed_resize_from_h=seed_resize_from_h,
            seed_resize_from_w=seed_resize_from_w,
            seed_enable_extras=seed_enable_extras,
            sampler_name=sd_samplers.samplers[sampler_index].name,
            batch_size=batch_size,
            n_iter=n_iter,
            steps=steps,
            cfg_scale=cfg_scale,
            width=width,
            height=height,
            restore_faces=restore_faces,
            tiling=tiling,
            enable_hr=enable_hr,
            denoising_strength=denoising_strength if enable_hr else None,
            hr_scale=hr_scale,
            hr_upscaler=hr_upscaler,
            hr_second_pass_steps=hr_second_pass_steps,
            hr_resize_x=hr_resize_x,
            hr_resize_y=hr_resize_y,
            override_settings=override_settings,
        )

        p.scripts = modules.scripts.scripts_txt2img
        p.script_args = args

        if cmd_opts.enable_console_prompts:
            print(f"\ntxt2img: {prompt}", file=shared.progress_print_out)

        processed = modules.scripts.scripts_txt2img.run(p, *args)

        if processed is None:
            processed = process_images(p)

        p.close()

        shared.total_tqdm.clear()

        generation_info_js = processed.js()
        if opts.samples_log_stdout:
            print(generation_info_js)

        if opts.do_not_show_images:
            processed.images = []

        batchSave(processed, prompt, negative_prompt, steps, cfg_scale, width,
                  height, seed,
                  samplers)

        return processed.images, generation_info_js, plaintext_to_html(processed.info), plaintext_to_html(
            processed.comments)

