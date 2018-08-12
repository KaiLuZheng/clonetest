#!/usr/bin/env python3

from PIL import Image, ImageDraw

import matplotlib.pyplot as plt
import numpy as np


im1 = Image.open('welian_logo_blue_mini.jpg')
im2 = Image.open('welian.png')

source = np.array(im1)
cloudword = np.array(im2)

wmax = 0
hmax = 0

dh = int(im1.height/2)
dw = int(im1.width/2)

herr = 0
werr = 10

aim_h_middle = int(im2.height/2+herr)
aim_w_middle = int(im2.width/2+werr)

hfrom = aim_h_middle - dh 
wfrom = aim_w_middle - dw 
   

newim = []
for i in (range(hfrom,hfrom+im1.height)):
    newim2=[]
    for j in (range(wfrom,wfrom+im1.width)):
        newim2.append(cloudword[i][j][0:3])
    newim.append(newim2)

cloudim = np.array(newim)
temp = Image.fromarray(cloudim)
#print(cloudim[0][0])
#temp.save('test.jpeg')

img1 = temp.convert('RGBA')
img2 = im1.convert('RGBA')

img = Image.blend(img1, img2, 0.3)
img.show()
img.save( "blend.png")



