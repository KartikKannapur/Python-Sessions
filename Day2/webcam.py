import VideoCapture as VC
from PIL import Image
from PIL import ImageOps
import time
from PIL import ImageFilter

img=[]
cam = VC.Device() 
inp=raw_input("Are you ready for a picture? If yes, type 'ok' ")
if inp=='ok':
    for i in range(1,4):
        print i
        time.sleep(0.8)
        img=cam.getImage()
           
del cam

img.show()
edges=img.filter(ImageFilter.FIND_EDGES)
edges.show()

contour=img.filter(ImageFilter.CONTOUR)
contour.show()

blur=img.filter(ImageFilter.BLUR)
blur.show()





