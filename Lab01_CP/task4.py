import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = '/home/aa/Documents/Lab_CP/Lab01/lab01_code/images/image01.jpg'
img = cv2.imread(image_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Chon value
increase_red = np.random.randint(50, 101)
increase_green = np.random.randint(50, 101)

print(f"Increasing Red by {increase_red}")
print(f"Increasing Green by {increase_green}")

r, g, b = cv2.split(img_rgb)

# Increase red and green
r = cv2.add(r, increase_red)
g = cv2.add(g, increase_green)

r = np.clip(r, 0, 255)
g = np.clip(g, 0, 255)

img_enhanced = cv2.merge([r, g, b])

# Display
plt.imshow(img_enhanced)
plt.title('Enhanced Image (Increased Red and Green)')
plt.show()