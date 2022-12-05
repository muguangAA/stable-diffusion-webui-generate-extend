import modules.scripts
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

# 背景列表
backgroundList = ['indoors', 'tatami', 'church', 'shop', 'fountain', 'classroom',
                  'street', 'chinese style architecture', 'stairs', 'flower field',
                  'underwater', 'forest', 'futon', 'spring_(season)',
                  'ocean', 'cafe', 'city', 'park', 'restaurant',
                  'Izakaya', 'outdoors', 'under table', 'winter'
                  'gym storeroom', 'public', 'on bed', 'fantasy',
                  'bedroom', 'gym storeroom', 'bathroom', 'swimming pool',
                  'garden', 'waterfall', 'beach']

describeList = ['pubic tattoo', 'saliva', 'pussy juice', 'pussy juice puddle', 'pussy juice trail',
                'comforting', 'exhibitionism', 'flashing', 'masturbation', 'fireworks', 'feather',
                'presenting', 'female ejaculation', 'female orgasm', 'self fondle', 'spread pussy',
                'spread anus', 'nude', 'pussy juice stain', 'flowers meadows', 'sunset', 'moon',
                "valentine", "halloween", "christmas", 'tanabata', 'cherry blossoms',
                'milking machine', 'night',
                'suggestive fluid', 'wet clothes', 'breasts out',
                'bathing', 'clothed masturbation', 'have to pee', 'peeing', 'dusk', 'fog',
                'waking up', 'forced orgasm', 'breath', 'self fondle',
                'steaming body', 'lactation', 'egg vibrator',
                'nipple tweak', 'looking at viewer', 'flower', 'magic circle',
                'detailed light', 'snowflakes', 'flower petals', 'plant', 'crowd',
                'beautiful detailed sky', 'beautiful detailed water', 'dappled sunlight',
                'lying', 'sitting', 'squatting', 'panties around', 'tally',
                'armpit peek', 'skirt lift', 'shy', 'embarrass', 'star',
                'lifted by self', 'shoujo kitou-chuu', 'public nudity',
                'panty lift', 'panty peek', 'pantyshot', 'dynamic angle' 'genshin impact',
                'frottage', 'panties peek', 'angle',
                'spread legs', 'leg up', 'legs apart', 'tiptoes', 'nipple slip', 'areola slip',
                'witch', 'angel', 'princess', 'vibrator under panties',
                'full-face blush', 'clothes lift', 'bra lift', 'bra peek', 'bra pull']

# 上装列表
clothesList = ['revealing clothes', 'baggy pants', 'bath towel', 'serafuku', 'BDSM', 'kimono', 'bikini',
               'school uniform', 'pajamas', 'backless outfit', 'sleepwear', 'sweater', 'rope', 'cape', 'ribbon',
               'summer uniform', 'sailor hat', 'coat', 'tailcoat', 'neck ring', 'uniform', 'kindergarten uniform',
               'cheerleader', 'cardigan', 'casual', 'heart cutout', 'corset', 'crop top', 'cropped shirt',
               'cropped vest', 'gym shirt', 'jersey', 'open kimono', 'kimono lift', 'unbuttoned shirt', 'luxuriant bra',
               'nippleless clothes', 'topless', 'neckerchief',
               'bikini top', 'bikini top removed', 'bra', 'no bra', 'heart pasties', 'see-through', 'downblouse',
               'bell choker', 'neckerchief', 'lolita', 'tuxedo', 'formal', 'japanese clothes', 'cheongsam',
               'loungewear', 'nightgown', 'babydoll', 'yukata', 'hanfu', 'gym uniform', 'yukata', 'sexy lingerie',
               'budget sarashi', 'shirt', 'undershirt', 'halter top', 'backless sweater',
               'hoodie', 'overcoat', 'trench coat', 'cloak', 'jacket', 'downblouse', 'wet clothes',
               'soggy clothes', 'wet shirt', 'topless', 'swimsuit', 'school swimsuit', 'bell',
               'naked cape', 'scarf', 'clothes writing', 'wedding dress',
               'virgin killer sweater', 'long shirt']

# 下装列表
pantsList = ['wedding dress', 'sailor', 'dress', 'naked apron', 'miniskirt', 'skirt', 'apron',
             'socks', 'pleated skirt', 'maid', 'suspender pants', 'trousers', 'summer long skirt',
             'shorts', 'pants', 'underpants', 'white thighhighs', 'sneakers', 'bottomless', 'clothes between thighs',
             'gym shorts', 'leotard pull', 'ankle socks', 'sheer legwear', 'leg cutout',
             'panties', 'wet panties', 'crotch plate', 'no panties', 'pink panties', 'bow panties',
             'crotchless panties', 'string panties', 'lace-trimmed panties', 'shorts',
             'bottomless', 'asymmetrical legwear', 'loose socks', 'bubble skirt', 'diaper', 'crotch plate',
             'uwabaki', 'cat tail']

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
    randomPants = getRandomPants()
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
    s += randomPants + ",\n"
    s += randomDescribe + ",\n"
    s += background + ","
    s += randomBackground + ","

    # 检测tag加nsfw
    if s.find("naked") != -1 or s.find("nudity") != -1 or s.find("nude") != -1 or s.find("sex") != -1 or s.find(
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
            s += randomPants + ",\n"
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
    s += getRandomPants() + ",\n"
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


def txt2img(prompt: str, negative_prompt: str, prompt_style: str, prompt_style2: str, steps: int, sampler_index: int,
            restore_faces: bool, tiling: bool, n_iter: int, batch_size: int, cfg_scale: float, seed: int, subseed: int,
            subseed_strength: float, seed_resize_from_h: int, seed_resize_from_w: int, seed_enable_extras: bool,
            height: int, width: int, enable_hr: bool, denoising_strength: float, firstphase_width: int,
            firstphase_height: int,
            useTheFollowingPrompt: bool, isRandom: bool, methodName: str, quality: str,
            featuresCharacters: str, others: str, background: str, characterPartNumIsRandom: bool,
            characterPartNum: int, characterPartRandomWeight: int, nsfwDescribeNumIsRandom: bool,
            nsfwDescribeNum: int, nsfwDescribeRandomWeight: int, justGenerate: bool, stepsAndScaleList: str,
            pixelList: str,
            *args):
    stepsAndScaleList = eval(stepsAndScaleList)
    pixelList = eval(pixelList)


    if justGenerate:
        return justGenerateMethod(prompt, negative_prompt, prompt_style, prompt_style2, steps, sampler_index,
                                  restore_faces,
                                  tiling, n_iter, batch_size, cfg_scale, seed, subseed, subseed_strength,
                                  seed_resize_from_h, seed_resize_from_w,
                                  seed_enable_extras, height, width, enable_hr, denoising_strength, firstphase_width,
                                  firstphase_height, stepsAndScaleList, pixelList, methodName, isRandom,
                                  quality, featuresCharacters, others, background,
                                  characterPartNumIsRandom, characterPartNum, characterPartRandomWeight,
                                  nsfwDescribeNumIsRandom, nsfwDescribeNum, nsfwDescribeRandomWeight, *args)
    else:
        return generateAndReturn(prompt, negative_prompt, prompt_style, prompt_style2, steps, sampler_index,
                                 restore_faces,
                                 tiling, n_iter, batch_size, cfg_scale, seed, subseed, subseed_strength,
                                 seed_resize_from_h, seed_resize_from_w,
                                 seed_enable_extras, height, width, enable_hr, denoising_strength, firstphase_width,
                                 firstphase_height, methodName, isRandom,
                                 quality, featuresCharacters, others, background,
                                 characterPartNumIsRandom, characterPartNum, characterPartRandomWeight,
                                 nsfwDescribeNumIsRandom, nsfwDescribeNum, nsfwDescribeRandomWeight,
                                 useTheFollowingPrompt, *args)


def justGenerateMethod(prompt, negative_prompt, prompt_style, prompt_style2, steps, sampler_index, restore_faces,
                       tiling,
                       n_iter, batch_size, cfg_scale, seed, subseed, subseed_strength, seed_resize_from_h,
                       seed_resize_from_w, seed_enable_extras, height, width, enable_hr, denoising_strength,
                       firstphase_width, firstphase_height, stepsAndScaleList, pixelList, methodName, isRandom,
                       quality, featuresCharacters, others, background,
                       characterPartNumIsRandom, characterPartNum, characterPartRandomWeight,
                       nsfwDescribeNumIsRandom, nsfwDescribeNum, nsfwDescribeRandomWeight, *args):
    print("仅生成图片")
    generateNum = n_iter
    n_iter = 1
    for n in range(generateNum):
        promptList = getPromptList(prompt, negative_prompt, methodName, isRandom,
                                   quality, featuresCharacters, others, background,
                                   characterPartNumIsRandom, characterPartNum, characterPartRandomWeight,
                                   nsfwDescribeNumIsRandom, nsfwDescribeNum, nsfwDescribeRandomWeight)
        for newPrompt in promptList:
            print("prompt: " + newPrompt)
            for stepsAndScale in stepsAndScaleList:
                newSteps = stepsAndScale[0]
                newScale = stepsAndScale[1]

                for pixel in pixelList:
                    newWidth = pixel[0]
                    newHeight = pixel[1]

                    print(
                        f"当前第{n + 1}张，steps:{newSteps}, scale:{newScale}, width:{newWidth}, height:{newHeight}, seed:{seed}")

                    generate(newPrompt, negative_prompt, prompt_style, prompt_style2, newSteps, sampler_index,
                             restore_faces,
                             tiling, n_iter, batch_size, newScale, seed, subseed, subseed_strength, seed_resize_from_h,
                             seed_resize_from_w,
                             seed_enable_extras, newHeight, newWidth, enable_hr, denoising_strength, firstphase_width,
                             firstphase_height, *args)
    return


def generateAndReturn(prompt, negative_prompt, prompt_style, prompt_style2, steps, sampler_index, restore_faces,
                      tiling, n_iter, batch_size, cfg_scale, seed, subseed, subseed_strength, seed_resize_from_h,
                      seed_resize_from_w,
                      seed_enable_extras, height, width, enable_hr, denoising_strength, firstphase_width,
                      firstphase_height, methodName, isRandom,
                      quality, featuresCharacters, others, background,
                      characterPartNumIsRandom, characterPartNum, characterPartRandomWeight,
                      nsfwDescribeNumIsRandom, nsfwDescribeNum, nsfwDescribeRandomWeight, useTheFollowingPrompt, *args):
    print("生成且返回")
    if useTheFollowingPrompt:
        prompt = getPromptList(prompt, negative_prompt, methodName, isRandom,
                               quality, featuresCharacters, others, background,
                               characterPartNumIsRandom, characterPartNum, characterPartRandomWeight,
                               nsfwDescribeNumIsRandom, nsfwDescribeNum, nsfwDescribeRandomWeight)[0]
    print("prompt: " + prompt)
    print("sampler: " + samplers[sampler_index])
    return generate(prompt, negative_prompt, prompt_style, prompt_style2, steps, sampler_index, restore_faces,
                    tiling, n_iter, batch_size, cfg_scale, seed, subseed, subseed_strength, seed_resize_from_h,
                    seed_resize_from_w,
                    seed_enable_extras, height, width, enable_hr, denoising_strength, firstphase_width,
                    firstphase_height, *args)


def batchSave(processed, prompt, negative_prompt, steps, scale, width, height, seed, sampler_index):
    # 我的保存图片
    print("图片的数量：" + str(len(processed.images)))
    imageList = processed.images
    if len(imageList) > 1:
        saveImage(imageList[0], prompt, negative_prompt, steps, scale, width, height, 0, sampler_index)
        for i in range(1, len(imageList)):
            saveImage(imageList[i], prompt, negative_prompt, steps, scale, width, height, seed, sampler_index)
            seed += 1
    else:
        saveImage(imageList[0], prompt, negative_prompt, steps, scale, width, height, seed, sampler_index)


def saveImage(image, prompt, negative_prompt, steps, scale, width, height, seed, sampler_index):
    filePath = "/content/stable-diffusion-webui/images/"
    drivePath = "/content/drive/MyDrive/stable-diffusion-webui/images/"
    os.makedirs(drivePath, exist_ok=True)
    os.makedirs(filePath, exist_ok=True)

    # 获取当前时间
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 设置文件名
    baseFilename = f'{cur_time}__{seed}__{width}x{height}'.strip()
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
            f.write(f'sampler: {samplers[sampler_index]}\n')
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


def generate(prompt: str, negative_prompt: str, prompt_style: str, prompt_style2: str, steps: int, sampler_index: int,
             restore_faces: bool, tiling: bool, n_iter: int, batch_size: int, cfg_scale: float, seed: int, subseed: int,
             subseed_strength: float, seed_resize_from_h: int, seed_resize_from_w: int, seed_enable_extras: bool,
             height: int, width: int, enable_hr: bool, denoising_strength: float, firstphase_width: int,
             firstphase_height: int, *args):
    if seed is None or seed == -1:
        seed = random.randint(1, 4294967295)

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
        sampler_index=sampler_index,
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

    batchSave(processed, prompt, negative_prompt, steps, cfg_scale, width, height, seed, sampler_index)

    return processed.images, generation_info_js, plaintext_to_html(processed.info)
