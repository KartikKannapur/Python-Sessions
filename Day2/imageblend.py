#External Libs Needed - Pillow or Python Imaging Library(PIL)
#Blending of two pictures in grayscale
'''pix,pix1 are pixel access objects ie. pointers to respective images
Any changes made through them directly affect the respective image.'''

from PIL import Image


row=[]
col=[]
pic1=Image.open("pic1.jpg").convert("L")
pic=Image.open("pic.png").convert("L")

pix=pic.load()
pix1=pic1.load()

p1size=pic1.size
psize=pic.size

respic=pic.resize((p1size[0],p1size[1]), Image.NEAREST)
respix=respic.load()

blend=Image.blend(pic1,pic,0.5)
        

blend.show()
blend.save('blend.jpg')

        
    
        


        
