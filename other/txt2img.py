import modules.scripts
from modules import sd_samplers
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


def getBasePrompt(quality, featuresCharacters, others, background, characterPartNum, characterPartNumIsRandom,
                  characterPartRandomWeight, nsfwDescribeNum, nsfwDescribeNumIsRandom,
                  nsfwDescribeRandomWeight):
    randomCharacterPart = getRandomCharacterPart(characterPartNum, characterPartNumIsRandom, characterPartRandomWeight)
    randomClothes = getRandomClothes()
    # randomPants = getRandomPants()
    randomEyes = getRandomEyes()
    randomHair = getRandomHair()
    randomDescribe = getRandomDescribe(nsfwDescribeNum, nsfwDescribeNumIsRandom, nsfwDescribeRandomWeight)
    randomBackground = getRandomBackground()

    s = ""
    s += quality + ",\n"
    s += featuresCharacters + ","
    s += randomCharacterPart + ",\n"
    s += others + ","
    s += randomEyes + ",\n"
    s += randomHair + ",\n"
    s += randomClothes + ","
    # s += randomPants + ",\n"
    s += randomDescribe + ",\n"
    s += background + ","
    s += randomBackground + ","

    # 检测tag加nsfw
    if s.find("naked") != -1 or s.find("nude") != -1 or s.find("sex") != -1 or s.find(
            "pussy") != -1:
        if s.find("nsfw") == -1:
            s = ""
            s += quality + ",\n"
            s += featuresCharacters + ","
            s += "nsfw,nipples" + ","
            s += randomCharacterPart + ",\n"
            s += others + ","
            s += randomEyes + ",\n"
            s += randomHair + ",\n"
            s += randomClothes + ","
            # s += randomPants + ",\n"
            s += randomDescribe + ",\n"
            s += background + ","
            s += randomBackground + ","

    return s


def getRandomPrompt(quality, featuresCharacters, others, background, characterPartNum, characterPartNumIsRandom,
                    characterPartRandomWeight, nsfwDescribeNum, nsfwDescribeNumIsRandom,
                    nsfwDescribeRandomWeight):
    ans = []
    ans.append(
        getBasePrompt(quality, featuresCharacters, others, background, characterPartNum, characterPartNumIsRandom,
                      characterPartRandomWeight, nsfwDescribeNum, nsfwDescribeNumIsRandom,
                      nsfwDescribeRandomWeight))
    return ans


def getSFWAndNSFWRandomPrompt(quality, featuresCharacters, others, background, characterPartNum,
                              characterPartNumIsRandom,
                              characterPartRandomWeight, nsfwDescribeNum, nsfwDescribeNumIsRandom,
                              nsfwDescribeRandomWeight):
    ans = []

    s = ""
    s += quality + ",\n"
    s += featuresCharacters + ","
    s += getRandomCharacterPart(characterPartNum, characterPartNumIsRandom, characterPartRandomWeight) + ",\n"
    s += others + ","
    s += getRandomEyes() + ",\n"
    s += getRandomHair() + ",\n"
    s += getRandomClothes() + ","
    # s += getRandomPants() + ",\n"
    s += getRandomDescribe(nsfwDescribeNum, nsfwDescribeNumIsRandom, nsfwDescribeRandomWeight) + ",\n"
    s += background + ","
    s += getRandomBackground() + ","
    ans.append(s)
    ans.append(
        getBasePrompt(quality, featuresCharacters, others, background, characterPartNum, characterPartNumIsRandom,
                      characterPartRandomWeight, nsfwDescribeNum, nsfwDescribeNumIsRandom,
                      nsfwDescribeRandomWeight))
    return ans


def getPromptList(prompt, negative_prompt, methodName, isRandom, quality, featuresCharacters, others, background,
                  characterPartNumIsRandom, characterPartNum, characterPartRandomWeight, nsfwDescribeNumIsRandom,
                  nsfwDescribeNum, nsfwDescribeRandomWeight):
    ans = []
    if isRandom is not None and isRandom:
        ls = []
        if methodName == "getRandomPrompt":
            ls = getRandomPrompt(quality, featuresCharacters, others, background,
                                 characterPartNum, characterPartNumIsRandom,
                                 characterPartRandomWeight, nsfwDescribeNum,
                                 nsfwDescribeNumIsRandom, nsfwDescribeRandomWeight)

        elif methodName == "getSFWAndNSFWRandomPrompt":
            ls = getSFWAndNSFWRandomPrompt(quality, featuresCharacters, others, background,
                                           characterPartNum, characterPartNumIsRandom,
                                           characterPartRandomWeight, nsfwDescribeNum,
                                           nsfwDescribeNumIsRandom, nsfwDescribeRandomWeight)
        else:
            print("未找到方法")

        for s in ls:
            ans.append(optimizeTheFormat(s))
    else:
        s = quality + "," + featuresCharacters + "," + others + "," + background
        ans.append(optimizeTheFormat(s))
    return ans


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


def txt2img(prompt: str, negative_prompt: str, prompt_style: str, prompt_style2: str, steps: int, sampler_index: int,
            restore_faces: bool, tiling: bool, n_iter: int, batch_size: int, cfg_scale: float, seed: int, subseed: int,
            subseed_strength: float, seed_resize_from_h: int, seed_resize_from_w: int, seed_enable_extras: bool,
            height: int, width: int, enable_hr: bool, denoising_strength: float, firstphase_width: int,
            firstphase_height: int, *args):
    jsonLoad = json.loads(negative_prompt)
    negative_prompt = jsonLoad["negative_prompt"]
    useTheFollowingPrompt = jsonLoad["useTheFollowingPrompt"]
    isRandom = jsonLoad["isRandom"]
    methodName = jsonLoad["methodName"]
    quality = jsonLoad["quality"]
    featuresCharacters = jsonLoad["featuresCharacters"]
    others = jsonLoad["others"]
    background = jsonLoad["background"]
    characterPartNumIsRandom = jsonLoad["characterPartNumIsRandom"]
    characterPartRandomWeight = jsonLoad["characterPartRandomWeight"]
    nsfwDescribeNumIsRandom = jsonLoad["nsfwDescribeNumIsRandom"]
    nsfwDescribeNum = jsonLoad["nsfwDescribeNum"]
    nsfwDescribeRandomWeight = jsonLoad["nsfwDescribeRandomWeight"]
    stepsAndScaleList = jsonLoad["stepsAndScaleList"]
    pixelList = jsonLoad["pixelList"]
    samplerList = jsonLoad["samplerList"]

    if useTheFollowingPrompt:
        print("仅生成图片")
        for n in range(1000):

            promptList = getPromptList(prompt, negative_prompt, methodName, isRandom,
                                       quality, featuresCharacters, others, background,
                                       characterPartNumIsRandom, 1, characterPartRandomWeight,
                                       nsfwDescribeNumIsRandom, nsfwDescribeNum, nsfwDescribeRandomWeight)
            seed = processing.get_fixed_seed(seed)
            for newPrompt in promptList:
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
                                styles=[prompt_style, prompt_style2],
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
                                firstphase_width=firstphase_width if enable_hr else None,
                                firstphase_height=firstphase_height if enable_hr else None,
                            )

                            p.scripts = modules.scripts.scripts_txt2img
                            p.script_args = args

                            if cmd_opts.enable_console_prompts:
                                print(f"\ntxt2img: {newWidth}", file=shared.progress_print_out)

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

                            # 保存图片
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
            styles=[prompt_style, prompt_style2],
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
            firstphase_width=firstphase_width if enable_hr else None,
            firstphase_height=firstphase_height if enable_hr else None,
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

        # 保存图片
        batchSave(processed, prompt, negative_prompt, steps, cfg_scale, width, height, seed,
                  sampler)

        return processed.images, generation_info_js, plaintext_to_html(processed.info)
