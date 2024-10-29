import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('vinuni_campus.jpg')

def add_gaussian_noise(img, mean=0, std_dev=20):
    noise = np.random.normal(mean, std_dev, img.shape)
    noisy_image = np.clip(img + noise, 0, 255).astype(np.uint8)
    return noisy_image

# add noise
noisy_image = add_gaussian_noise(image, std_dev=80)  # std_dev = noise level

# display
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.title('Noisy Image')
plt.axis('off')
plt.show()