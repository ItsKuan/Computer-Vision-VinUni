import cv2
import matplotlib.pyplot as plt

image = cv2.imread('vinuni_campus.jpg')

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#conver to Rgb
plt.title('vinuni-campus')
plt.axis('off')
plt.show()

# Dimensions
height, width, channels = image.shape
print(f"Image Dimensions: Width = {width}, Height = {height}, Channels = {channels}")