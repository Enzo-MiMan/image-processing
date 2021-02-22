import cv2
import numpy as np
import os
from os.path import join

kernel_1d = cv2.getGaussianKernel(ksize=7, sigma=0.84089642, ktype=cv2.CV_32F)
kernel_2d = kernel_1d * kernel_1d.T
print(kernel_2d)

image = cv2.imread('images/lena.bmp', 0)
cv2.imshow('original', image)

rows, cols = image.shape
m, n = kernel_2d.shape
radium_m = (m-1)//2
radium_n = (n-1)//2
result = np.zeros(image.shape)

for i in range(radium_m, rows-radium_m, 1):
    for j in range(radium_n, rows-radium_n, 1):
        result[i, j] = (image[i-radium_m:i+radium_m+1, j-radium_n:j+radium_n+1] * kernel_2d).sum()

result = np.uint8(result)
cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()
