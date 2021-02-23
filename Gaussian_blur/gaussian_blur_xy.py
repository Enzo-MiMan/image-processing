import cv2
import numpy as np

image = cv2.imread('imgs/lena.bmp', 0)
sigma = 0.6
kernel_size = np.int(np.round(sigma*3)*2+1)
radium = kernel_size//2

kernel_1d = cv2.getGaussianKernel(kernel_size, sigma)
image = np.pad(image, ((radium, radium), (radium, radium)), 'constant')
rows, cols = image.shape
result1 = np.zeros((rows-2*radium, cols-2*radium))
result2 = np.zeros((rows-2*radium, cols-2*radium))

for i in range(radium, rows-radium, 1):
    for j in range(radium, cols-radium, 1):
        result1[i-radium, j-radium] = (image[i:i+1, j-radium:j+radium+1] * kernel_1d.T).sum()

result1 = np.pad(result1, ((radium, radium), (radium, radium)), 'constant')
for i in range(radium, rows-radium, 1):
    for j in range(radium, cols-radium, 1):
        result2[i-radium, j-radium] = (result1[i-radium:i+radium+1, j:j+1] * kernel_1d).sum()

result2 = np.uint8(result2)
cv2.imshow('result', result2)
cv2.waitKey()
cv2.destroyAllWindows()
