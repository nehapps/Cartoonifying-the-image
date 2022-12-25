#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import easygui
import imageio
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog 
from tkinter import *
from PIL import ImageTk, Image
top =tk.Tk()
top.geometry('400x400')
top.title('Cartoonify your Imgae!')
top.configure(background = 'white')
label = Label(top,background = '#CDCDCD', font = ('calibari',20,'bold'))


# In[2]:


def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)


# In[3]:


def cartoonify(ImagePath):
    originalImage = cv2.imread(ImagePath)
#print(originalImage)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)

    if originalImage is None:
        print("can't find any image.Choose the right extension file")
    sys.exit()
    ReSized1 = cv2.resize(originalImage,(960,540))
    plt.imshow(ReSized1,cmap='gray')
    grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage,(960,540))
    plt.imshow(ReSized2, cmap='gray')
    smoothGrayScale = cv2.medianBlur(grayScaleImage,5)
    ReSized3 = cv2.resize(smoothGrayScale,(960,540))
    plt.imshow(ReSized3, cmap="gray")
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY,9,9)
    ReSized4 = cv2.resize(getEdge,(960,540))
    plt.imshow(ReSized4, cmap='gray')
    colorImage = cv2.bilateralFilter(originalImage,9,300,300)
    ReSized5 = cv2.resize(colorImage,(960,540))
    plt.imshow(ReSized5, cmap = 'gray')
    cartoonImage = cv2.bitwise_and(colorImage,colorImage,mask = getEdge)
    ReSized6 = cv2.resize(cartoonImage, (960,540))
    plt.imshow(ReSized6, cmap='gray')
    image=(ReSized1,ReSized2,ReSized3,ReSized4,ReSized5,ReSized6)
    fig,axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[],'yticks':[]}, gridspec_kw=dict(hspace=0.1,wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(image[i], cmap = 'gray')
    save1 = Button(top,text='save cartoon image', command=lambda: save(Imagepath,Resized6),padx = 30,pady =5)
    save1.configure(background = '#364156', foreground = 'white', font= ('calibari',10,"bold"))
    save1.pack(side=TOP,pady=50)
    plt.show()


# In[4]:


def save(Resized6, catimg):
    newName = "cartoonified_Image"
    path1 = os.path.dirname(catimg)
    extension=os.path.splitext(catimg)[1]
    path = os.path.join(path1,newName+extension)
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name" + newName +"at"+path
    tk.messagebox.showinfo(title=None, Message= I)


# In[5]:


upload = Button(top,text = "Cartoonify an Image", command = upload, padx = 10, pady =5)
upload.configure(background = "#364156", foreground = 'white', font=("calibari",10,"bold"))
upload.pack(side = TOP,pady =50)


# In[6]:


top.mainloop()


# In[ ]:




