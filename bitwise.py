import cv2
import numpy as np

def main():
    # Open the first webcam device found by your system
    cam = cv2.VideoCapture(0)


    # Run continuous loop while webcam device is being used
    while(cam.isOpened()):

        # grab the next video frame
        # cv2.VideoCapture.read returns 2 values
        # retval: returns true or false if the read
        # operation was successful or not, we discard
        # it here by using the _ variable name
        # image: this returns a matrix containing the
        # pixel values of the image, in we assign this
        # value to frame

        # _, frame0 = cam.read()
        _, frame1 = cam.read()
        _, frame = cam.read()
        

        # You can do bitwise operations of image matrices
        # Challenge: try using different operators on the images
        frame = frame^frame1

        # create or write to a window named "Hello OpenCV" 
        # and display our captures frame
        cv2.imshow('Frame Diff', frame)

        # wait for the user to press "q" before exiting
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # free the webcam devicce
    cam.release()
    # close "Hello OpenCV"
    cv2.destroyWindow('Frame Diff')

if __name__ == "__main__":
    main()