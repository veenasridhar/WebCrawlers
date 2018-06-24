import sys
import re
import urllib.request
import bs4 as bs
import requests
import ctypes
from ctypes import wintypes
import os
import datetime
from PIL import Image
date=datetime.datetime.now()
day=str(str(date.day)+'-'+str(date.month)+'-'+str(date.year))
data=urllib.request.urlopen('https://www.bingwallpaper.com/').read()
soup=bs.BeautifulSoup(data,'html.parser')
img_div=soup.select('.cursor_zoom > img')
img_src=img_div[0].get('src')
image=requests.get(img_src)
print(image)
new_file="C:\\Python\\Python36-32\\Wallpaper\\Bing"+day+".bmp"
with open(new_file,'wb') as file:
    file.write(image.content)
image=Image.open(new_file)
image.save(new_file,"BMP")
r=ctypes.windll.user32.SystemParametersInfoW(20,0,new_file,3)
if not r:
   print(ctypes.WinError())
