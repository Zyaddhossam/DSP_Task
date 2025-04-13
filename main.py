import cv2
print(cv2.__version__)

# Read and display original image
original_img = cv2.imread('test_img.jpg')
cv2.imshow('Original', original_img)

rgb_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
cv2.imshow('BGR 2 RGB', rgb_img)
# Save the original image
cv2.imwrite('new_img.jpg', original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()