import cv2
import numpy as np
import math

# 默认高斯核尺寸 高度等于宽度
sigma=0.84089642
kernel_size = np.int(np.round(3*sigma)*2+1)
radium = kernel_size//2

# opencv 通过函数 cv2.getGaussianKernel 生成二维高斯核
kernel_1d = cv2.getGaussianKernel(ksize=kernel_size, sigma=sigma, ktype=cv2.CV_32F)
kernel_2d = kernel_1d * kernel_1d.T
print(kernel_2d)

# 手撸高斯核，通过二维高斯公式计算得出
constant = 1/(2 * math.pi * sigma**2)
gaussian_kernel = np.zeros((kernel_size, kernel_size))
for i in range(0, kernel_size, 1):
    for j in range(0, kernel_size, 1):
        x = i-radium
        y = j-radium
        gaussian_kernel[i,j] = constant*math.exp(-0.5/(sigma**2)*(x**2+y**2))
# 归一化
gaussian_kernel = gaussian_kernel/gaussian_kernel.sum()
print('\n', gaussian_kernel)
