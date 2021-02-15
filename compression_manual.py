import numpy as np
import cv2

#lossy compression 8 bit image into 6 bit

def compression():
    image = cv2.imread('/home/ashish/Downloads/dravid.jpg')
    clone = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
             for k in range(image.shape[2]):
                   if image[i][j][k]<=3:
                      clone[i][j][k]=0
                   elif image[i][j][k]<=7:
                      clone[i][j][k]=1
                   elif image[i][j][k]<=11:
                      clone[i][j][k]=2
                   elif image[i][j][k]<=15:
                      clone[i][j][k]=3
                   elif image[i][j][k]<=19:
                      clone[i][j][k]=4
                   elif image[i][j][k]<=23:
                      clone[i][j][k]=5
                   elif image[i][j][k]<=27:
                      clone[i][j][k]=6
                   elif image[i][j][k]<=31:
                      clone[i][j][k]=7
                   elif image[i][j][k]<=35:
                      clone[i][j][k]=8
                   elif image[i][j][k]<=39:
                      clone[i][j][k]=9
                   elif image[i][j][k]<=43:
                      clone[i][j][k]=10
                   elif image[i][j][k]<=47:
                      clone[i][j][k]=11
                   elif image[i][j][k]<=51:
                      clone[i][j][k]=12
                   elif image[i][j][k]<=55:
                      clone[i][j][k]=13
                   elif image[i][j][k]<=59:
                      clone[i][j][k]=14
                   elif image[i][j][k]<=63:
                      clone[i][j][k]=15
                   elif image[i][j][k]<=67:
                      clone[i][j][k]=16
                   elif image[i][j][k]<=71:
                      clone[i][j][k]=17
                   elif image[i][j][k]<=75:
                      clone[i][j][k]=18
                   elif image[i][j][k]<=79:
                      clone[i][j][k]=19
                   elif image[i][j][k]<=83:
                      clone[i][j][k]=20
                   elif image[i][j][k]<=87:
                      clone[i][j][k]=21
                   elif image[i][j][k]<=91:
                      clone[i][j][k]=22
                   elif image[i][j][k]<=95:
                      clone[i][j][k]=23
                   elif image[i][j][k]<=99:
                      clone[i][j][k]=24
                   elif image[i][j][k]<=103:
                      clone[i][j][k]=25
                   elif image[i][j][k]<=107:
                      clone[i][j][k]=26
                   elif image[i][j][k]<=111:
                      clone[i][j][k]=27
                   elif image[i][j][k]<=115:
                      clone[i][j][k]=28
                   elif image[i][j][k]<=119:
                      clone[i][j][k]=29
                   elif image[i][j][k]<=123:
                      clone[i][j][k]=30
                   elif image[i][j][k]<=127:
                      clone[i][j][k]=31
                   elif image[i][j][k]<=131:
                      clone[i][j][k]=32
                   elif image[i][j][k]<=135:
                      clone[i][j][k]=33
                   elif image[i][j][k]<=139:
                      clone[i][j][k]=34
                   elif image[i][j][k]<=143:
                      clone[i][j][k]=35
                   elif image[i][j][k]<=147:
                      clone[i][j][k]=36
                   elif image[i][j][k]<=151:
                      clone[i][j][k]=37
                   elif image[i][j][k]<=155:
                      clone[i][j][k]=38
                   elif image[i][j][k]<=159:
                      clone[i][j][k]=39
                   elif image[i][j][k]<=163:
                      clone[i][j][k]=40
                   elif image[i][j][k]<=167:
                      clone[i][j][k]=41
                   elif image[i][j][k]<=171:
                      clone[i][j][k]=42
                   elif image[i][j][k]<=175:
                      clone[i][j][k]=43
                   elif image[i][j][k]<=179:
                      clone[i][j][k]=44
                   elif image[i][j][k]<=183:
                      clone[i][j][k]=45
                   elif image[i][j][k]<=187:
                      clone[i][j][k]=46
                   elif image[i][j][k]<=191:
                      clone[i][j][k]=47
                   elif image[i][j][k]<=195:
                      clone[i][j][k]=48
                   elif image[i][j][k]<=199:
                      clone[i][j][k]=49
                   elif image[i][j][k]<=203:
                      clone[i][j][k]=50
                   elif image[i][j][k]<=207:
                      clone[i][j][k]=51
                   elif image[i][j][k]<=211:
                      clone[i][j][k]=52
                   elif image[i][j][k]<=215:
                      clone[i][j][k]=53
                   elif image[i][j][k]<=219:
                      clone[i][j][k]=54
                   elif image[i][j][k]<=223:
                      clone[i][j][k]=55
                   elif image[i][j][k]<=227:
                      clone[i][j][k]=56
                   elif image[i][j][k]<=231:
                      clone[i][j][k]=57
                   elif image[i][j][k]<=235:
                      clone[i][j][k]=58
                   elif image[i][j][k]<=239:
                      clone[i][j][k]=59
                   elif image[i][j][k]<=243:
                      clone[i][j][k]=60
                   elif image[i][j][k]<=247:
                      clone[i][j][k]=61
                   elif image[i][j][k]<=251:
                      clone[i][j][k]=62
                   elif image[i][j][k]<=255:
                      clone[i][j][k]=63
          
                                    
                        
    print(clone.shape)
    cv2.imshow("original",image)
    cv2.imwrite('compressed.jpg',clone)
    cv2.imshow('clone',clone) 
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

compression()
