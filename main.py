import cv2
print(cv2.__version__)

# Read and display original image
original_img = cv2.imread('test_img.jpg')
cv2.imshow('Original Image', original_img)

gray_img = cv2.imread('test_img.jpg', 0)
cv2.imshow('Grayscale Image', gray_img)

# Invert image using arithmetic operation
inv_img1 = 255 - gray_img
cv2.imshow('Inverted Image (Arithmetic)', inv_img1)

# Invert image using bitwise NOT
inv_img2 = cv2.bitwise_not(gray_img)
cv2.imshow('Inverted Image (Bitwise NOT)', inv_img2)

# Save the original image
cv2.imwrite('new_img.jpg', original_img)

# Wait for key press and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()