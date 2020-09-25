# IMPORT LIBS-----
import cv2
import numpy as np
import pyautogui
import pytesseract
from PIL import Image
import time
from ocr import ImageTextReader
# from tkinter import *
# import tkinter as tk
IR = ImageTextReader()
# SETTINGS-----
# This means the OCR will search true->char by char, false->word by word
CHARACTER_BASED = False
scale = 8
# time.sleep(7)
# INPUT IMAGE-----
# img = cv2.imread("test2.png")
img = pyautogui.screenshot()
im = img
px = im.load()
# print (px[4, 4])
# to set pixel value
# px[4, 4] = (0, 0, 0)
# cordinate = x, y = 4,4
# # using getpixel method
# print (im.getpixel(cordinate));

img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
hImg, wImg, _ = img.shape
original_img = img

# IMAGE FILTERING-----
img = cv2.resize(img, None, fx=scale, fy=scale)
img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
# img = cv2.adaptiveThreshold(
#    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 1)
#img = cv2.Canny(img, 600, 600)
# Tesseract call-----

# text=pytesseract.image_to_string(img,lang="eng")
# print(text)
if CHARACTER_BASED:
    original_img = IR.char_based(img, scale)
else:
    original_img = IR.word_based(img, scale)


# DISPLAY IMAGE-----
cv2.imshow("Img", original_img)
cv2.waitKey(0)


# window = Tk()  #Makes main window
# window.overrideredirect(True)
# window.wm_attributes("-topmost", True)
# window.geometry("+0+0")
# display1 = Label(window)
# display1.grid(row=1, column=0, padx=0, pady=0)  #Display 1
# imga = pyautogui.screenshot()

# def show_img():
#     # take screenshot using pyautogui
#     img = cv2.cvtColor(np.array(imga), cv2.COLOR_RGB2BGR)
#     # img = cv2.resize(img, (400,400))
#     # img = cv2.flip(img, 1)
#     cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
#     img = Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(master = display1, image=img)
#     display1.imgtk = imgtk #Shows img for display 1
#     display1.configure(image=imgtk)
#     window.after(3, show_img)

# show_img()
# window.mainloop()
