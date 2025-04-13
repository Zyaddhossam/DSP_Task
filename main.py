import cv2
import numpy as np
import matplotlib.pyplot as plt
print(cv2.__version__)

# Load and preprocess images
img = cv2.imread('test_img.jpg')
if img is None:
    print("Error: Could not load image")
    exit()

# --- Core Operations ---
# 1. Resizing
resized_square = cv2.resize(img, (300, 300))  # Force 300x300
resized_half = cv2.resize(img, None, fx=0.5, fy=0.5)  # Scale down 50%

# 2. Cropping (center 50%)
h, w = img.shape[:2]
cropped = img[h//4:3*h//4, w//4:3*w//4]  # Center crop

# 3. Rotation (45 degrees)
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

# --- Grayscale Processing ---
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv_arith = 255 - gray_img
inv_bitwise = cv2.bitwise_not(gray_img)

# --- Matplotlib Display ---
plt.figure(figsize=(15, 8))

# Original and spatial transforms
plt.subplot(2, 4, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(2, 4, 2)
plt.imshow(cv2.cvtColor(resized_square, cv2.COLOR_BGR2RGB))
plt.title('Resized (300x300)')
plt.axis('off')

plt.subplot(2, 4, 3)
plt.imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
plt.title('Cropped (Center 50%)')
plt.axis('off')

plt.subplot(2, 4, 4)
plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.title('Rotated 45°')
plt.axis('off')

# Grayscale and inversions
plt.subplot(2, 4, 5)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(2, 4, 6)
plt.imshow(inv_arith, cmap='gray')
plt.title('Arithmetic Invert')
plt.axis('off')

plt.subplot(2, 4, 7)
plt.imshow(inv_bitwise, cmap='gray')
plt.title('Bitwise Invert')
plt.axis('off')

plt.tight_layout()
plt.show()

# --- Save Results ---
cv2.imwrite('resized_square.jpg', resized_square)
cv2.imwrite('resized_half.jpg', resized_half)
cv2.imwrite('cropped.jpg', cropped)
cv2.imwrite('rotated.jpg', rotated)
cv2.imwrite('inversions.jpg', np.hstack([gray_img, inv_arith, inv_bitwise]))

# --- OpenCV Display ---
cv2.imshow('Resized Half', resized_half)
cv2.imshow('Cropped', cropped)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()