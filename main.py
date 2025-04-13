import cv2
print(cv2.__version__)

# Read and display original image
original_img = cv2.imread('test_img.jpg')
cv2.imshow('Original', original_img)

# Convert to HSV color space and display
hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_img)

# Split HSV into individual channels
H = hsv_img[:,:,0]  # Hue 
S = hsv_img[:,:,1]  # Saturation 
V = hsv_img[:,:,2]  # Value 
cv2.imshow('Hue Channel', H)
cv2.imshow('Saturation Channel', S)
cv2.imshow('Value Channel', V)

# Save the original image
cv2.imwrite('new_img.jpg', original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()