from PIL import Image, ImageOps
import numpy as np
from math import sqrt
     
# creating a image1 object
im = Image.open("theiere.png")
# im = Image.open("my_chat.v1.jpg")
im = im.resize((224,224))

px = im.load()
img = Image.new('RGB', (224, 224), color = 'red') 
for x in range(im.size[0]): # for every pixel:
    for y in range(im.size[1]):
        r,g,b,t = px[x,y]
        print(r,g,b,t)

        a = 40
        # im.putpixel((x, y), (min(r+a, 255),min(g+a, 255),min(b+a, 255)))#(r,g,b))
        img.putpixel((x, y), (r,g,b))#(r,g,b))

img.save("theiere.png")

