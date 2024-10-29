import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = '/home/aa/Documents/Lab_CP/Lab01/lab01_code/images/image01.jpg'
img = cv2.imread(image_path)

# Upscale by a factor of 2 using OpenCV's nearest neighbor interpolation
scale_factor = 2
img_nearest_opencv = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)

def nearest_neighbor_interpolation(img, scale_factor):
    height, width, channels = img.shape
    new_height, new_width = int(height * scale_factor), int(width * scale_factor)
    upscaled_img = np.zeros((new_height, new_width, channels), dtype=img.dtype)

    for i in range(new_height):
        for j in range(new_width):
            orig_i = int(i / scale_factor)
            orig_j = int(j / scale_factor)
            upscaled_img[i, j] = img[orig_i, orig_j]

    return upscaled_img

# Upscale using the custom nearest neighbor interpolation function
img_nearest_custom = nearest_neighbor_interpolation(img, scale_factor)

img_nearest_opencv = cv2.cvtColor(img_nearest_opencv, cv2.COLOR_BGR2RGB)
img_nearest_custom = cv2.cvtColor(img_nearest_custom, cv2.COLOR_BGR2RGB)

# Display
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img_nearest_opencv)
axes[0].set_title('OpenCV Nearest Neighbor')
axes[1].imshow(img_nearest_custom)
axes[1].set_title('Custom Nearest Neighbor')
plt.show()

# C0mparison
is_same = np.array_equal(img_nearest_opencv, img_nearest_custom)
print("Identical?", is_same)