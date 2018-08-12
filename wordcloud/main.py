#!/usr/bin/env python3

from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
from os import path
from scipy.misc import imread
import sys

from PIL import Image
import numpy as np


#使用jieba对txt进行分词
filename = 'sign.txt'

with open(filename,encoding='utf-8') as f:
    mytext = f.read()

cut_text =' '.join(jieba.lcut(mytext))
#print(cut_text)

#maskimg = 'welian_logo_blue_mini.jpg'
maskimg = 'self.jpg'
color_mask = imread(maskimg)


cloud = WordCloud(
    background_color='white',   # 背景色
    mask=color_mask,            # 背景图
    #font_path='font.ttf',      # 字体对排布有比较大的影响 
    font_path='font.otf',       
    max_words=10000,            # 最大显示的字数
    #stopwords=STOPWORDS,       # 停用词
    max_font_size=150,          # 字体最大值 影响排布
    random_state=60             # 配色方案个数 影响排布
)
#生成词云图
word_cloud = cloud.generate(cut_text)
#print(type(word_cloud))

def miximg(img1,img2,alpha):
    im1 = img1.convert('RGBA')
    im2 = img2.convert('RGBA')
    return Image.blend(im1,im2,alpha)
    
wordcloud = Image.fromarray(word_cloud.to_array())
background = Image.open(maskimg) 

img= miximg(wordcloud, background, 0.05)
img.show()
img.save('blend.png')



