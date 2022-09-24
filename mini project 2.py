#checker board 8x8

import numpy as np
import cv2

img = np.zeros((800, 800, 3))
i = 0
j = 100
while (i <= 700):

    k = 100
    l = 200
    while (k <= 700):
        #img[i:j, k:l] = 255, 255, 255
       # a = l/200
        if (l%200 == 0):
            i += 100
            j += 100
            img[i:j,k:l] = 255, 255, 255
            cv2.imshow('CHECKER BOARD',img)
            cv2.waitKey(2)
        else :
            i -= 100
            j -= 100
            img[i:j,k:l] = 255, 255, 255
            cv2.imshow('CHECKER BOARD',img)
            cv2.waitKey(2)
        k += 100
        l += 100
            
        
    j += 100
    i += 100
img[0:100,0:100] = 255, 255, 255
img[200:300,0:100] = 255, 255, 255
img[400:500,0:100] = 255, 255, 255
img[600:700,0:100] = 255, 255, 255
cv2.imshow('CHECKER BOARD',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
