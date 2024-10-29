import cv2
import matplotlib.pyplot as plt

image = cv2.imread('vinuni_campus.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def scale_image(img, new_width, new_height):
    scaled_image = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Example
new_width = 640
new_height = 480
scaled_image = scale_image(gray_image, new_width, new_height)

plt.imshow(scaled_image, cmap='gray')
plt.title('Scaled Image')
plt.axis('off')
plt.show()