import cv2
print(cv2.__version__)

original_img = cv2.imread('test_img.jpg')
cv2.imshow('original', original_img)

gray_img = cv2.imread('test_img.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('new_img.jpg', original_img)
