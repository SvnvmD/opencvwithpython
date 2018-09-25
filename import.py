import cv2
cv2.CV_LOAD_IMAGE_COLOR = 0
image = cv2.imread('k.jpg', cv2.CV_LOAD_IMAGE_COLOR)
cv2.imwrite('l.png', image)