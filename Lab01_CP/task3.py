import matplotlib.pyplot as plt
import numpy as np
import cv2

image_path = '/home/aa/Documents/Lab_CP/Lab01/lab01_code/images/image01.jpg'
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(img_rgb)

# Create zero matrices
zeros = np.zeros(img.shape[:2], dtype="uint8")

# Create channel for each color
img_red = cv2.merge([r, zeros, zeros])
img_green = cv2.merge([zeros, g, zeros])
img_blue = cv2.merge([zeros, zeros, b])

# Display
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(img_red)
axes[0].set_title('Red Channel')
axes[1].imshow(img_green)
axes[1].set_title('Green Channel')
axes[2].imshow(img_blue)
axes[2].set_title('Blue Channel')
plt.show()