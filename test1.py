import cv2
import numpy as np 
import matplotlib.pyplot as mlt 
# img = cv2.imread('k.png', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_GRAYSCALE = 0
#IMREAD_UNCHANGED = -1

#cv2.imshow('image', img)	#for showing image 
#cv2.waitKey(0)				#for waiting until any key is pressed
#cv2.destroyAllWindows()		#destroy all windows
# mlt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# mlt.plot([50,100], [80,100], 'c', linewidth=5)
# mlt.show()
# cv2.imwrite('writeimg.png', img) #write image


# Loading Video Source - OpenCV with Python for Image and Video Analysis 2
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
# while True:
# 	ret, frame = cap.read()
# 	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 	cv2.imshow('frame', frame)
# 	cv2.imshow('THIS IS GRAY FRAME', gray)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break
# cap.release()
# out.release()
# cv2.destroyAllWindows()


#drawing and writing on image
img = cv2.imread('l.png', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (150, 150), (0,0, 255), 15)
cv2.imshow('image', img)
cv.waitKey(0)
cv2.destroyAllWindows()
