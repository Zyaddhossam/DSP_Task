import cv2
print(cv2.__version__)

# Read and display original image
original_img = cv2.imread('test_img.jpg')
if original_img is None:
    print("Error: Could not load image 'test_img.jpg'")
    exit()
cv2.imshow('Original Image', original_img)


gray_cvt = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale (cvtColor)', gray_cvt)

# scale factors
half_img = cv2.resize(original_img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Half Size (scale factors)', half_img)


# Stretched
stretch_img = cv2.resize(original_img, (500, 600),
             interpolation=cv2.INTER_NEAREST)
cv2.imshow('Stretched (NEAREST)', stretch_img)

# Save the original image
cv2.imwrite('new_img.jpg', original_img)

# Wait for key press and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()