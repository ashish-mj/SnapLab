import cv2
import numpy as np
import getpass
import platform
import os
import calendar
import time

def apply(path,effect_img,name="intermediate"):
   if path.count("jpg")>0 or path.count("jpeg")>0:
      cv2.imwrite(name+'.jpg',effect_img)
   elif path.count("png")>0:
      cv2.imwrite(name+'.png',effect_img)


def oreo(path):
   image = cv2.imread(path)  
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
   clahe = cv2.createCLAHE(clipLimit =0) 
   clahe_img = clahe.apply(gray)
   denoised =cv2.fastNlMeansDenoising(clahe_img,None,15,7,21) 
   _, oreo = cv2.threshold(denoised, 127, 255, cv2.THRESH_BINARY)
   apply(path,oreo)
   
def mercury(path):
   image = cv2.imread(path)
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   clahe = cv2.createCLAHE() 
   clahe_img = clahe.apply(gray)
   mercury =cv2.fastNlMeansDenoising(clahe_img,None,40,7,21)
   apply(path,mercury)

 
def alchemy(path):
   image = cv2.imread(path)
   rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   alchemy=cv2.fastNlMeansDenoisingColored(rgb,None,20,10,7,21)
   apply(path,alchemy)

def wacko(path):
   image = cv2.imread(path)
   hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   _,s,v=cv2.split(hsv)
   wacko= cv2.merge([s,v,v])
   apply(path,wacko)

def unstable(path):
    image = cv2.imread(path)
    kernel=np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
    unstable=cv2.filter2D(image, -1, kernel)
    apply(path,unstable)                     
   

def ore(path):
    image = cv2.imread(path)
    kernel=np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
    ore=cv2.filter2D(image, -1, kernel)
    apply(path,ore)

def contour(path):
    image = cv2.imread(path)
    denoised_color=cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    gray=cv2.cvtColor(denoised_color,cv2.COLOR_BGR2GRAY)
    adap=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    contours,hierarchy=cv2.findContours(adap,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour=denoised_color.copy()
    color=(255,255,255)
    for c in contours:
      cv2.drawContours(contour,[c],-1,color,1)
    apply(path,contour)


def snicko(path):
   image = cv2.imread(path)
   clone=image.copy()
   denoised=cv2.fastNlMeansDenoisingColored(clone, None, 5, 5, 7, 21)
   snicko=cv2.Canny(denoised,100,200)
   apply(path,snicko)

def indus(path):
   image = cv2.imread(path)
   template = cv2.imread("../../../images/flag.jpg")
   row1,cols1,_= image.shape
   row2,cols2,_ = template.shape
   x=cols1/cols2
   y=row1/row2
   res = cv2.resize(template, (0, 0), fx = x, fy = y) 
   indus = cv2.addWeighted(image,0.5,res,0.75,0)
   apply(path,indus)

def spectra(path):
   image = cv2.imread(path)
   template = cv2.imread("../../../images/temp.png")
   row1,cols1,_= image.shape
   row2,cols2,_ = template.shape
   x=cols1/cols2
   y=row1/row2
   res = cv2.resize(template, (0, 0), fx = x, fy = y) 
   spectra = cv2.addWeighted(image,0.5,res,0.75,0)
   apply(path,spectra)

def molecule(path):
   image = cv2.imread(path)
   template = cv2.imread("../../../images/dots1.jpg")
   row1,cols1,_= image.shape
   row2,cols2,_ = template.shape
   x=cols1/cols2
   y=row1/row2
   res = cv2.resize(template, (0, 0), fx = x, fy = y) 
   molecule = cv2.addWeighted(image,1,res,0.5,0)
   apply(path,molecule)

    


def lynn(path):
   image = cv2.imread(path)
   template = cv2.imread("../../../images/water.jpeg")
   row1,cols1,_= image.shape
   row2,cols2,_ = template.shape
   x=cols1/cols2
   y=row1/row2
   res = cv2.resize(template, (0, 0), fx = x, fy = y) 
   lynn = cv2.addWeighted(image,1,res,0.5,0)
   apply(path,lynn)

def download(path):
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
       outpath = "SnapLab_Effects_"+ts+".jpg"
       cv2.imwrite(outpath,image)                 
    elif path.count('png')>0:
       outpath = "SnapLab_Effects_"+ts+".png"
       cv2.imwrite(outpath,image)              
    os.chdir(previous)


#oreo()
#mercury()
#alchemy()
#wacko()
#unstable()
#ore()
#contour()
#snicko()
#indus()
#spectra()
#molecule()
#lynn()
