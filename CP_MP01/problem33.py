import cv2
import matplotlib.pyplot as plt

image = cv2.imread('vinuni_campus.jpg')

# gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# display
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

plt.axis('off')
plt.show()