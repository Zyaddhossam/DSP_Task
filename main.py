import cv2
print(cv2.__version__)

original_img = cv2.imread('test_img.jpg')
cv2.imshow('original', original_img)

gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR 2 Gray', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('new_img.jpg', original_img)
