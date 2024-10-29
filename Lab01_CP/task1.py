import matplotlib.pyplot as plt
import cv2

image_paths = []
for i in range(1, 5):
  image_path = f'/home/aa/Documents/Lab_CP/Lab01/lab01_code/images/image0{i}.jpg'
  image_paths.append(image_path)

images = []
for path in image_paths:
  img = cv2.imread(path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  images.append(img)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for i, ax in enumerate(axes.flat):
    ax.imshow(images[i])
    ax.set_title(f'Image {i+1}')
    ax.axis('off')

plt.tight_layout()
plt.show()
