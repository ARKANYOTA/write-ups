from PIL import Image, ImageOps
import numpy as np
from math import sqrt
     
# creating a image1 object
teap = Image.open("theiere.v3.png")
chat = Image.open("chat.jpg")
# im = Image.open("my_chat.v1.jpg")

teappx = teap.load()
chatpx = chat.load()
img = Image.new('RGB', (224, 224), color = 'red') 

for x in range(224): # for every pixel:
    for y in range(224):
        r1,g1,b1 = teappx[x,y]
        r2,g2,b2 = chatpx[x,y]

        dist = sqrt((r1-r2)**2+(g1-g2)**2+(b1-b2)**2)
        rab,gab,bab = (r2-r1,g2-g1,b2-b1)
        dist = sqrt(rab**2+gab**2+bab**2)
        if dist >= 70:
            img.putpixel((x, y), (r2-int((70/dist)*rab),g2-int((70/dist)*gab),b2-int((70/dist)*bab)))
        else:
            img.putpixel((x, y), (r1,g1,b1))

        # img.putpixel((x, y), (r,g,b))#(r,g,b))

img.save("theiere.v4.png")

