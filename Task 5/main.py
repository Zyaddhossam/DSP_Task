from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. You must read the RGB image and then invert it.
image = Image.open("./Task 5/task5_img.png").convert("RGB")

image_array = np.array(image)
inverted_array = 255 - image_array

# 2. The inverted image will be rotated counterclockwise by 90 degrees.
rotated_array = np.rot90(inverted_array)
rotated_image = Image.fromarray(rotated_array).resize((image.width, image.height))

#3.  The output will combine both the input and rotated image
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(image)
plt.axis('off')

plt.subplot(1,2,2)
plt.title('Inverted')
plt.imshow(rotated_image)
plt.axis('off')
plt.show()