#!/usr/bin/env python3

from PIL import Image,ImageDraw
import pytesseract

import numpy as np

import matplotlib.pyplot as plt

import scipy
import time

'''加载图片'''
#img = np.array(Image.open('WechatIMG1025.jpeg').convert('L'))

img = Image.open('WechatIMG1025.jpeg')
numpix = np.array(img)

plt.imshow(numpix)
plt.show()

#img = Image.open('1234.jpeg')

print(type(img.size[0]))
print(type(1))
print(img.size[1])
#clearNoise(img,50,4,4)

#img.save('temp.jpeg')
 
for i in range(0,img.size[1]):
    for j in range(0,img.size[0]):
        r,g,b = numpix[i][j]
        if r > 150:
            numpix[i][j] = [0,0,0]
            continue
        numpix[i][j] = [255-r,255-g,255-b]



im = Image.fromarray(numpix)
im.save("test.jpg")

time.sleep(1)
plt.imshow(im)

#text = pytesseract.image_to_string(im, lang='chi_sim')
#text = pytesseract.image_to_string(im, lang='eng')
#text = pytesseract.image_to_string(im, lang='num')

#print(text)


#scipy.misc.imsave('meelo.jpg', img)


'''识别图片，可以指定语言'''
#text = pytesseract.image_to_string(img, lang='chi_sim')
#text = pytesseract.image_to_string(img, lang='eng')

#print(text)




