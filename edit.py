import cv2
import numpy as np
import getpass
import platform
import os
import calendar
import time

def apply(path,edit_img,name="edited"):
   if path.count("jpg")>0 or path.count("jpeg")>0:
      cv2.imwrite(name+'.jpg',edit_img)
   elif path.count("png")>0:
      cv2.imwrite(name+'.png',edit_img)


def brightness(path,value):
    image=cv2.imread(path)
    zero=np.zeros(image.shape,image.dtype)
    bright_img = cv2.addWeighted(image,1,zero,0,value)
    apply(path,bright_img)

def contrast(path,value):
    image=cv2.imread(path)                              # range 0-1 derease contrast ,1-2 increase 
    zero=np.zeros(image.shape,image.dtype)
    con = cv2.addWeighted(image,value,zero,0,0)
    apply(path,con)
    
def sharp(path,value):
    image=cv2.imread(path)
    kernel = np.array([[0,-1,0], 
                       [-1,5,-1],                     #min
                       [0,-1,0]])
    kernel1 =np.array([[-1,-1,-1], 
                [-1, 9,-1],                           #max
                [-1,-1,-1]])
    if value=='max':
        sharpened = cv2.filter2D(image, -1, kernel1)
    else:
        sharpened = cv2.filter2D(image, -1, kernel)
    apply(path,sharpened)
    

def blur(path,value):
    image = cv2.imread(path) 
    blur = cv2.blur(image,(value,value))                              #(x,x) 2,4,6,8,10
    apply(path,blur)

def rotate(path,value):
    image = cv2.imread(path)
    if value=="90":
        rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif value=="180":
        rotated = cv2.rotate(image, cv2.ROTATE_180)
    elif value=="270":
        rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    apply(path,rotated)

def resize(path,value):
    image = cv2.imread(path)
    if value=="25":
        resize=cv2.resize(image,(0,0),fx=0.25,fy=0.25)                    #0.25,0.5,0.75 ,1
    elif value=="50":
        resize=cv2.resize(image,(0,0),fx=0.5,fy=0.5)
    elif value=="75":
        resize=cv2.resize(image,(0,0),fx=0.75,fy=0.75)
    apply(path,resize)
    
def denoise(path,value):
    image = cv2.imread(path)
    if value=="min":
       denoised=cv2.fastNlMeansDenoisingColored(image,None,4,4,7,21)
    elif value=="mid":
       denoised=cv2.fastNlMeansDenoisingColored(image,None,7,7,7,21)
    elif value=="max":
       denoised=cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    apply(path,denoised)
    
def downloads(path):
    username = getpass.getuser()
    folder = ''
    gmt = time.gmtime()
    ts = calendar.timegm(gmt)
    ts=str(ts)
    if platform.system()=='Linux':
        folder += '/home/'+username+'/Downloads/'
    else:
        folder += 'C:\Downloads'
    image = cv2.imread(path)
    previous = os.getcwd()
    os.chdir(folder)
    if path.count('jpg')>0 or path.count('jpeg')>0 :
       outpath = "SnapLab_Edited_"+ts+".jpg"
       cv2.imwrite(outpath,image)                 
    elif path.count('png')>0:
       outpath = "SnapLab_Edited_"+ts+".png"
       cv2.imwrite(outpath,image)              
    os.chdir(previous)

#brightness()
#contrast()
#sharp()
#blur()
#rotate()
#resize()
#denoise()
