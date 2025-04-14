from PIL import Image
import numpy as np

# 1. You must read the RGB image and then invert it.
image = Image.open("task5_img.png").convert("RGB")

image_array = np.array(image)
inverted_array = 255 - image_array

# 2. The inverted image will be rotated counterclockwise by 90 degrees.
rotated_array = np.rot90(inverted_array)
rotated_image = Image.fromarray(rotated_array).resize((image.width, image.height))
