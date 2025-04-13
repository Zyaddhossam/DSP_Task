import cv2
print(cv2.__version__)

# Read and display original image
original_img = cv2.imread('test_img.jpg')
cv2.imshow('Original', original_img)

# Convert to grayscale and display
gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR 2 Gray', gray_img)

# Apply threshold to create black and white image
_, Black_White_Img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Black_White_Img', Black_White_Img)

# Save the original image
cv2.imwrite('new_img.jpg', original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()