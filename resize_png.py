import cv2
import os
import numpy as np

folders = ['intro','output/bndry/bon', 'output/bndry/hui','attention', ]# 

for folder in folders:
    path = f'./{folder}'
    files = os.listdir(path)
    for file in files:
        if file.endswith('.png'):
            img = cv2.imread(os.path.join(path, file))
            img = cv2.resize(img, (64+512+128, 64+128+512))
            cv2.imwrite(os.path.join(path, 'c_'+file), img)