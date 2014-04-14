#External Libs Needed - Pillow or Python Imaging Library(PIL)
#Blending of two pictures in grayscale
'''pix,pix1 are pixel access objects ie. pointers to respective images
Any changes made through them directly affect the respective image.'''

import os
import sys
from PIL import Image

row=[]
col=[]

pic1=Image.open("pic1.png").convert("L")
pic=Image.open("pic.jpg").convert("L")

pix=pic.load()
pix1=pic1.load()

p1size=pic1.size
psize=pic.size

for i in range(psize[1]):
    for j in range(psize[0]):
        row.append(pix[j,i])
    col.append(row)
    row=[]

'''for i in range(len(col)):
        for j in range(psize[0]):
                if col[i][j]<50:
                        col[i][j]=0
                else:
                        col[i][j]=255'''
                                                    

for i in range(psize[1]):
    for j in range(psize[0]):
        pix[j,i]=col[i][j]

respic=pic.resize((p1size[0],p1size[1]), Image.NEAREST)
respix=respic.load()

for i in range(p1size[1]):
    for j in range(p1size[0]):
        pix1[j,i]=pix1[j,i]+respix[j,i]
        

pic1.show()
pic1.save('blended.jpg')

        
    
        


        
