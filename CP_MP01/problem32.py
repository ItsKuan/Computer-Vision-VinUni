import cv2
import matplotlib.pyplot as plt

image = cv2.imread('vinuni_campus.jpg')

#Access pixel
pixel_value = image[50, 50]

#print value
print(f"Pixel value at (50, 50): {pixel_value}")