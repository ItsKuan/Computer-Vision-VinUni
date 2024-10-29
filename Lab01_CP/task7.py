import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = '/home/aa/Documents/Lab_CP/Lab01/lab01_code/images/image01.jpg'
img = cv2.imread(image_path)

height, width, _ = img.shape

# Dowonscale
new_height, new_width = height // 2, width // 2
downscaled_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

# Avg pooling
for i in range(new_height):
    for j in range(new_width):
        # Calculate the region in the original image corresponding to the current pixel in the downscaled image
        i_start, i_end = i * 2, (i + 1) * 2
        j_start, j_end = j * 2, (j + 1) * 2

        # Extract the 2x2 region
        region = img[i_start:i_end, j_start:j_end]

        # Calculate the average of the region
        downscaled_img[i, j] = np.mean(region, axis=(0, 1)).astype(np.uint8)

downscaled_img = cv2.cvtColor(downscaled_img, cv2.COLOR_BGR2RGB)

# Display
plt.imshow(downscaled_img)
plt.title('Downscaled Image (Average Pooling)')
plt.show()