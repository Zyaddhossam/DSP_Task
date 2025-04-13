import cv2
print(cv2.__version__)
cv2.imread("test_img.jpg")
cv2.imshow("test", cv2.imread("test_img.jpg"))
cv2.waitKey(0)
cv2.destroyAllWindows()


