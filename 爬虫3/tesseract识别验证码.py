# encoding=utf-8
import pytesseract
from PIL import Image
from urllib import request
import requests
url ='http://my.cnki.net/elibregister/CheckCode.aspx'
aa = request.urlretrieve(url,'验证码.png')
image = Image.open("验证码.png")
text = pytesseract.image_to_string(image)
print(text)

