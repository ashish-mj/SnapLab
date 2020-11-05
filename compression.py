import cv2
import numpy as np
import getpass
import platform
import os
import calendar
import time
 
jpg={'max':25,'mid':50,'min':75}
png={'max':9,'mid':6,'min':3}

def save(path, image, jpg_quality=None, png_compression=None):
  if jpg_quality:
    cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
  elif png_compression:
    cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])         
  else:
    cv2.imwrite(path, image)
 
def compression(path,typ):
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
       outpath = "SnapLab_compressed"+ts+".jpg"
       save(outpath,image,jpg_quality=jpg[typ])                #jpg 0-100 
    elif path.count('png')>0:
       outpath = "SnapLab_compressed"+ts+".png"
       save(outpath, image,png_compression=png[typ])              #png 0-9 high means small but more time
    else:
        save('unsupported',image)
    os.chdir(previous)
   

