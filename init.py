#IMPORT LIBS-----
import cv2
import numpy as np
import pyautogui  
import pytesseract
# from tkinter import *
# import tkinter as tk

#INPUT IMAGE-----
# img = cv2.imread("test2.png")
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
original_img = img;

#IMAGE FILTERING-----
# img = cv2.resize(img,None, fx=0.5, fy=0.5)
img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,1)

#Tesseract call-----
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text=pytesseract.image_to_string(img,lang="eng")
print(text)

#DISPLAY IMAGE-----
# img = original_img
cv2.imshow("Img",img)
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