#!/usr/bin/env python3

from PIL import Image
import pytesseract

import numpy as np


'''加载图片'''
#img = Image.open('WechatIMG1025.jpeg').convert('L')
img = Image.open('WechatIMG1025.jpeg')

print(img)
'''识别图片，可以指定语言'''
text = pytesseract.image_to_string(img, lang='chi_sim')

print(text)




