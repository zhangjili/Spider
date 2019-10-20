# coding=utf-8
import pytesseract
from PIL import Image
import tesserocr

im=Image.open('1.png')
print(pytesseract.image_to_string(im))
