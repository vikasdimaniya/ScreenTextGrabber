import cv2
import numpy as np
import pyautogui
import pytesseract
from PIL import Image
import time
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class ImageTextReader:
    def filters(self, img):
        img = cv2.resize(img, None, fx=2, fy=2)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
        return img

    def char_based(self, img, scale):
        hImg, wImg, _ = img.shape
        boxes = pytesseract.image_to_boxes(img)
        for b in boxes.splitlines():
            b = b.split(' ')
            print(b[0])
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 0), -1)
            cv2.putText(img, b[0], (x, hImg - y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5*scale, (0, 0, 255), 1)
        return img

    def word_based(self, img, scale):
        #img = self.filters(img)
        im = Image.fromarray(np.uint8(img)).convert('RGB')
        boxes = pytesseract.image_to_data(img)
        img = cv2.resize(
            img, None, fx=1/scale, fy=1/scale)
        for a, b in enumerate(boxes.splitlines()):
            if a != 0:
                b = b.split()
                if len(b) == 12:
                    print(int(b[6]), int(b[7]), int(b[8]), int(b[9]),b[11])

                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    x=int(x/scale);y=int(y/scale);w=int(w/scale);h=int(h/scale);
                    background_color = im.getpixel((x, y))
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,0), -1)
                    # text_color=im.getpixel((x,y))
                    text_color = (255, 255, 255)
                    cv2.putText(
                        img, b[11], (x, y+h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)
                    # cv2.putText(img, str(x)+" "+str(y), (x, y+h),
                    #             cv2.FONT_HERSHEY_SIMPLEX, 0.3, text_color, 1)
        return img
