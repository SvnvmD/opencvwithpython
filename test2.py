import numpy as np
import cv2
#create object VideoCapture
cap = cv2.VideoCapture(0)
while(True):
    # Capture video frame-by-frame
    ret, frame = cap.read()

    # Convert frames to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the gray frames
    cv2.imshow('THIS IS MY FRAME',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()