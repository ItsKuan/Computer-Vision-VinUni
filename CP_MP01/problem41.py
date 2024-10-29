import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('vinuni_campus.jpg')

# Gaussian Smoothing
kernel_size = (5, 5)
sigma = 1.0
smoothed_image = cv2.GaussianBlur(image, kernel_size, sigma)

# Display
plt.imshow(cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB))
plt.title('Smoothed Image')
plt.axis('off')
plt.show()