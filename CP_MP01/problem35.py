import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('vinuni_campus.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find min pixel value and its leocation
min_value = gray_image.min()
min_index = np.unravel_index(gray_image.argmin(), gray_image.shape)

# result
print(f"Darkest pixel value: {min_value}")
print(f"Darkest pixel location (row, column): {min_index}")