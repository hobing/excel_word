# -*- coding: utf-8 -*-

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os

import warnings
warnings.filterwarnings('ignore')

folder_path = 'X:\\0000AAAAA周口交通项目\\施工\\00000验收资料\\治安枪机球机调试资料\\2026-01-24治安监控图片-导出清单\\capture'

# 获取文件夹中所有文件的路径
file_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if
              os.path.isfile(os.path.join(folder_path, filename))]

# 遍历所有文件
#tt=0
for file_path in file_paths:
    #tt+=1
    img = Image.open(file_path)
    print(file_path)
    if img.width == 1280:
        imgcrop = img.crop((0, 60, 1280, img.height))#两个坐标点来框选（宽度坐标，高度坐标），以左上角为0，0
        imgcrop.save(file_path)
    elif img.width == 1920:
        imgcrop = img.crop((0,90,1920, 1080))
        imgcrop.save(file_path)
    elif img.width == 2560:
        imgcrop = img.crop((0,90,2560,1440))
        imgcrop.save(file_path)
    #if tt == 10:break


