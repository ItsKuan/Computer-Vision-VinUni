import matplotlib.pyplot as plt
import cv2

image_path = '/home/aa/Documents/Lab_CP/Lab01/lab01_code/images/image01.jpg'
img = cv2.imread(image_path)
#Information
height, width, channels = img.shape
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)
pixel_value = img[50, 100]

print("Dimensions:", width, "x", height)
print("Min pixel value:", img.min())
print("Max pixel value:", img.max())
print("Pixel value at (100, 50):", pixel_value)

#C0nvert
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img_rgb)
axes[0].set_title('RGB Image')
axes[1].imshow(img_hsv)
axes[1].set_title('HSV Image')
plt.show()


