import cv2
print(cv2.__version__)

# Read and display original image
original_img = cv2.imread('test_img.jpg')
cv2.imshow('Original', original_img)

# Resize image to half its original dimensions
height, width = original_img.shape[:2]
half_img = cv2.resize(original_img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Half Size', half_img)

# Save the original image
cv2.imwrite('new_img.jpg', original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()