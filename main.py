import cv2
print(cv2.__version__)

# Read and display original image
original_img = cv2.imread('test_img.jpg')
cv2.imshow('Original', original_img)

# Split into Blue, Green, Red channels
B, G, R = cv2.split(original_img)
cv2.imshow('Blue Channel', B)
cv2.imshow('Green Channel', G)
cv2.imshow('Red Channel', R)

# Save the original image
cv2.imwrite('new_img.jpg', original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()