import cv2
import matplotlib.pyplot as plt

image_path = '/home/aa/Documents/Lab_CP/Lab01/lab01_code/images/image01.jpg'
img = cv2.imread(image_path)

scale_factor = 2

img_nearest = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)
img_bilinear = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
img_bicubic = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

img_nearest = cv2.cvtColor(img_nearest, cv2.COLOR_BGR2RGB)
img_bilinear = cv2.cvtColor(img_bilinear, cv2.COLOR_BGR2RGB)
img_bicubic = cv2.cvtColor(img_bicubic, cv2.COLOR_BGR2RGB)

# Display upscaled image
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(img_nearest)
axes[0].set_title('Nearest Neighbor')
axes[1].imshow(img_bilinear)
axes[1].set_title('Bilinear')
axes[2].imshow(img_bicubic)
axes[2].set_title('Bicubic')
plt.show()