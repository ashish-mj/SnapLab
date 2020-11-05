import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
previous = os.getcwd()
folder = previous +'/static/images/trash/'

def transparentOverlay(src, overlay,scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  
    rows, cols, _ = src.shape  
    for i in range(h):
        for j in range(w):
            if i >= rows or j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[ i][j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[i][j]
    return src

def hind(cap): 
    cap.set(cv2.CAP_PROP_FPS, 30)
    template = cv2.imread("images/flag.jpg")
    while True:
         ret, img = cap.read()
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.3,0)
         cv2.putText(img, 'I LOVE MY INDIA', (60,425),cv2.FONT_HERSHEY_DUPLEX,2, ( 124,174,221),5,cv2.LINE_AA)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')
    

def flora(cap):
    flora_ori = cv2.imread('images/flower.png', -1)
    flora_ori = cv2.cvtColor(flora_ori, cv2.COLOR_BGR2BGRA)
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (50, 50), (400, 400))
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                y=y-40
                flora_symin = int(y )
                flora_symax = int(y + h)
                sh_flora = flora_symax - flora_symin
                face_flora_roi_color = img[flora_symin:flora_symax, x:x + w]
                flora = cv2.resize(flora_ori, (w, sh_flora), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_flora_roi_color, flora)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')



def handlebar(cap):
    mus_ori = cv2.imread('images/mustache.png', -1) 
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                mus_symin = int(y + 3.5 * h / 6)
                mus_symax = int(y + 5 * h / 6)
                sh_mus = mus_symax - mus_symin
                face_mus_roi_color = img[mus_symin:mus_symax, x:x + w]
                mustache = cv2.resize(mus_ori, (w, sh_mus), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_mus_roi_color, mustache)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')

def bella(cap):
    mus_ori = cv2.imread('images/pig.png', -1) 
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         template = cv2.imread("images/pink.jpeg")
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.2,0)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                mus_symin = int(y + 2.0 * h / 7)
                mus_symax = int(y + 5.5* h / 7)
                sh_mus = mus_symax - mus_symin
                face_mus_roi_color = img[mus_symin:mus_symax, x+10:x + w]
                mustache = cv2.resize(mus_ori, (w, sh_mus), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_mus_roi_color, mustache)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')



   

def tilak(cap):
    tilak_ori = cv2.imread('images/tilak.png', -1)
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         template = cv2.imread("images/yellow.jpeg")
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.2,0)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                tilak_symin = int(y)
                tilak_symax = int(y + h/3)
                sh_tilak = tilak_symax - tilak_symin
                x_axis=int(x+2.5*w/4)-int(x+1.5*w/4)
                face_tilak_roi_color = img[tilak_symin:tilak_symax, int(x+1.5*w/4):int(x+2.5*w/4)]
                tilak = cv2.resize(tilak_ori, (x_axis, sh_tilak), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_tilak_roi_color, tilak)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')

def thug(cap):
    specs_ori = cv2.imread('images/glass.png', -1)
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         cv2.putText(img, 'Thug Life', (100,400),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,3, (0,0,0),5,cv2.LINE_AA) 
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                glass_symin = int(y + 1.5 * h / 5)
                glass_symax = int(y + 2.5 * h / 5)
                sh_glass = glass_symax - glass_symin
                face_glass_roi_color = img[glass_symin:glass_symax, x:x + w]
                specs = cv2.resize(specs_ori, (w, sh_glass), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color, specs)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')



def lido(cap):
    specs_ori = cv2.imread('images/beach.png', -1)
    specs_ori = cv2.cvtColor(specs_ori, cv2.COLOR_BGR2BGRA)
    chain_ori = cv2.imread('images/chain.png', -1)
    chain_ori = cv2.cvtColor(chain_ori, cv2.COLOR_BGR2BGRA) 
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         template = cv2.imread("images/red.jpeg")
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.5,0)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                glass_symin = int(y + 1.0 * h / 5)
                glass_symax = int(y + 3.0 * h / 5)
                sh_glass = glass_symax - glass_symin
                face_glass_roi_color = img[glass_symin:glass_symax, x:x + w]
                specs = cv2.resize(specs_ori, (w, sh_glass), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color, specs)
                chain_symin = int(y + h +5 )
                chain_symax = int(y + h+ 150)
                sh_chain = chain_symax - chain_symin
                face_chain_roi_color = img[chain_symin:chain_symax, x:x + w]
                chain = cv2.resize(chain_ori, (w, sh_chain), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_chain_roi_color, chain)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')



def polychrome(cap):
    specs_ori = cv2.imread('images/funny.png', -1)
    specs_ori = cv2.cvtColor(specs_ori, cv2.COLOR_BGR2BGRA)
    template = cv2.imread("images/temp.png") 
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(img, 1.2, 5, 0, (120, 120), (350, 350))
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.5,0)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                glass_symin = int(y + 1.5 * h / 5)
                glass_symax = int(y + 2.5 * h / 5)
                sh_glass = glass_symax - glass_symin
                face_glass_roi_color = img[glass_symin:glass_symax, x:x + w]
                specs = cv2.resize(specs_ori, (w, sh_glass), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color, specs)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')



def visor(cap):
    mask_ori = cv2.imread('images/mask.png', -1)
    mask_ori = cv2.cvtColor(mask_ori, cv2.COLOR_BGR2BGRA) 
    template = cv2.imread("images/corona.jpg")
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.2,0)
         cv2.putText(img, 'Go Corona', (100,400),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,3, ( 64, 51,242),5,cv2.LINE_AA)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                mask_symin = int(y-30+h/2 )
                mask_symax = int(y + h+40)
                sh_mask = mask_symax - mask_symin
                face_mask_roi_color = img[mask_symin:mask_symax, x:x + w+20]
                mask = cv2.resize(mask_ori, (w, sh_mask), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_mask_roi_color, mask)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')



def rcb(cap):
    rcb_ori = cv2.imread('images/band.png', -1)
    specs_ori= cv2.imread('images/nags.png', -1)
    template = cv2.imread("images/red.jpeg") 
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(img, 1.2, 5, 0, (120, 120), (350, 350))
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.5,0)
         cv2.putText(img, 'BOLD ARMY', (60,400),cv2.FONT_HERSHEY_DUPLEX,3, ( 124,174,221),5,cv2.LINE_AA)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                rcb_symin = int(y-40)
                rcb_symax = int(y + h/3)
                sh_rcb = rcb_symax - rcb_symin
                face_rcb_roi_color = img[rcb_symin:rcb_symax, x:x + w]
                rcb = cv2.resize(rcb_ori, (w, sh_rcb), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_rcb_roi_color, rcb)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')

def mi(cap):
    mi_ori = cv2.imread('images/Blue_band.png', -1)
    mi_ori = cv2.cvtColor(mi_ori, cv2.COLOR_BGR2BGRA) 
    template = cv2.imread("images/blue.jpeg")
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()                                
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         row1,cols1,_= img.shape
         row2,cols2,_ = template.shape
         x=cols1/cols2
         y=row1/row2
         res = cv2.resize(template, (0, 0), fx = x, fy = y) 
         img = cv2.addWeighted(img,1,res,0.3,0)
         cv2.putText(img, 'MI PALTAN', (80,400),cv2.FONT_HERSHEY_DUPLEX,3, ( 155,91,3),4,cv2.LINE_AA)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                mi_symin = int(y-40)
                mi_symax = int(y + h/3)
                sh_mi = mi_symax - mi_symin
                face_mi_roi_color = img[mi_symin:mi_symax, x:x + w]
                mi = cv2.resize(mi_ori, (w, sh_mi), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_mi_roi_color, mi)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')

def nags(cap):
    rcb_ori = cv2.imread('images/band.png', -1)
    specs_ori= cv2.imread('images/nag.png', -1)
    mus_ori = cv2.imread('images/nag_mus.png', -1)
    mus_ori = cv2.cvtColor(mus_ori, cv2.COLOR_BGR2BGRA) 
    cap.set(cv2.CAP_PROP_FPS, 30)
    while True:
         ret, img = cap.read()
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.2, 5, 0, (120, 120), (350, 350))
         cv2.putText(img, 'PEAS!', (200,400),cv2.FONT_HERSHEY_DUPLEX,3, ( 124,174,221),5,cv2.LINE_AA)
         for (x, y, w, h) in faces:
            if h > 0 and w > 0:
                glass_symin = int(y + 1.5 * h / 5)
                glass_symax = int(y + 2.7 * h / 5)
                sh_glass = glass_symax - glass_symin
                face_glass_roi_color = img[glass_symin:glass_symax, x:x + w]
                specs = cv2.resize(specs_ori, (w, sh_glass), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color, specs)
                mus_symin = int(y + 3.7* h / 6)
                mus_symax = int(y + 4.8* h / 6)
                sh_mus = mus_symax - mus_symin
                face_mus_roi_color = img[mus_symin:mus_symax, x-50:x+w]
                mustache = cv2.resize(mus_ori, (w+100, sh_mus), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_mus_roi_color, mustache)
                rcb_symin = int(y-40)
                rcb_symax = int(y + h/3)
                sh_rcb = rcb_symax - rcb_symin
                face_rcb_roi_color = img[rcb_symin:rcb_symax, x:x + w]
                rcb = cv2.resize(rcb_ori, (w, sh_rcb), interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_rcb_roi_color, rcb)
         os.chdir(folder)
         cv2.imwrite("filter.jpg",img)
         os.chdir(previous)
         imgencode=cv2.imencode('.jpg',img)[1]
         strinData = imgencode.tostring()
         yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')




#hind()
#flora()
#handlebar()
#bella()
#tilak()
#thug()
#lido()
#polychrome()
#mask()
#rcb()
#mi()
#nags()

