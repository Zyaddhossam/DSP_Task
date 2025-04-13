import cv2
import matplotlib.pyplot as plt
print(cv2.__version__)

# Read and process images using OpenCV
original_img = cv2.imread('test_img.jpg')
gray_img = cv2.imread('test_img.jpg', 0)
inv_img_arithmetic = 255 - gray_img
inv_img_bitwise = cv2.bitwise_not(gray_img)
# Display using Matplotlib in a single figure
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Original Grayscale')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(inv_img_arithmetic, cmap='gray')
plt.title('Inverted (Arithmetic)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(inv_img_bitwise, cmap='gray')
plt.title('Inverted (Bitwise)')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save the original image
cv2.imwrite('new_img.jpg', original_img)

# Wait for key press and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()