import pywt
import cv2
import numpy as np



def w2d(img, mode='haar', level=1):
    imarray=img
    imarray=cv2.cvtColor(imarray,cv2.COLOR_BGR2GRAY)
    imarray=np.float32(imarray)
    imarray /= 255
    coeffs=pywt.wavedec2(imarray, mode, level=level)
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0
    imarray_H=pywt.waverec2(coeffs_H,mode)
    imarray_H *=255
    imarray_H= np.uint8(imarray_H)
    return imarray_H