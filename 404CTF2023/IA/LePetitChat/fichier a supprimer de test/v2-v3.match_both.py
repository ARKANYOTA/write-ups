from PIL import Image, ImageOps
import numpy as np
from math import sqrt
     
# creating a image1 object
teap = Image.open("teapot.v2.png")
chat = Image.open("chat.jpg")
# im = Image.open("my_chat.v1.jpg")

teappx = teap.load()
chatpx = chat.load()
img = Image.new('RGB', (224, 224), color = 'red') 

for x in range(224): # for every pixel:
    for y in range(224):
        r1,g1,b1 = teappx[x,y]
        r2,g2,b2 = chatpx[x,y]

        a = 40
        if (r1+g1+b1)//3 > 70:
            a = 40
            img.putpixel((x, y), (min(r2+a, 255),min(g2+a, 255),min(b2+a, 255)))#(r,g,b))
        else:
            a = -40
            img.putpixel((x, y), (max(r2+a, 0),max(g2+a, 0),max(b2+a, 0)))#(r,g,b))
            img.putpixel((x, y), (r2,g2,b2))

        # img.putpixel((x, y), (r,g,b))#(r,g,b))

img.save("teapot.v3.png")

