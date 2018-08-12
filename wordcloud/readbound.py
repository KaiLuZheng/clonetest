#!/usr/bin/env python3

from PIL import Image, ImageFilter
from PIL import ImageOps

import numpy as np

img = Image.open("myself.jpg");


img = img.convert('L')

img = img.filter(ImageFilter.FIND_EDGES);
img = ImageOps.invert(img)

img = img.convert('RGB')

source = np.array(img)
bound = np.array(img) 

for hnum,i in enumerate(source):
    for wnum,j in enumerate(source[hnum]):
        if j[0] > 250:
           #bound[i][j] = [255,255,255] 
            pass
        else:
           bound[i][j] = [0,0,0]
    #print(hnum)

img = np.array(bound)
img = Image.fromarray(img)

img.save('self.jpg')
img.show();
