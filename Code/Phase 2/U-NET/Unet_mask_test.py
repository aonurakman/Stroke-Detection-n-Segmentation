# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:18:27 2021

@author: Ahmet
"""
import numpy as np
import random
import time
import cv2 
from keras.models import load_model
import matplotlib.pyplot as plt

kanama_ise_1_iskemi_ise_0 = 0

ornek = "8"

model = load_model(r"C:/Users/emine/Downloads/Test/model18.h5")
path = "C:/Users/emine/Downloads/Test/"
image = cv2.imread("image"+ornek + ".png")
image_s = image.copy()
image = cv2.resize(image, (128, 128))
image = image/255
image = image.reshape((1,128,128,3))
mask = cv2.imread("mask"+ ornek + ".png")
mask512 = mask[:,:,kanama_ise_1_iskemi_ise_0]
mask = cv2.resize(mask, (128, 128))
mask = mask[:,:,1]

y = model.predict(image)
y = y>0.5
y = y*255
y = np.reshape(y,(128,128))

cv2.imwrite("d.png",y)
y = cv2.imread("d.png",0)
y512 = cv2.resize(y, (512, 512))
kesisim = 0
birlesim = 0
for i in range(512):
    for j in range(512):
        if(mask512[i][j]>0):
            if(y512[i][j]>0):
                image_s[i][j][0] = 255
                kesisim += 1
                birlesim += 1
            else:
                image_s[i][j][1] = 255
                birlesim += 1
        elif(y512[i][j]>0):
            image_s[i][j][2] = 255
            birlesim += 1
iou_score=kesisim/(birlesim)            

fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
ax = fig.add_subplot(1, 4, 1)
ax.imshow(image.reshape((128,128,3)), cmap="gray")

fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
ax = fig.add_subplot(1, 4, 2)
ax.imshow(mask, cmap="gray")

fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
ax = fig.add_subplot(1, 4, 3)
ax.imshow(y, cmap="gray")
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
ax = fig.add_subplot(1, 4, 3)
ax.imshow(image_s, cmap="gray")

cv2.imwrite("result" + ornek + ".png",image_s)
