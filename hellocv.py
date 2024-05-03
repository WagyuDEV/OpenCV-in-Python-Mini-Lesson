import cv2

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
        _, frame = cam.read()

        # create or write to a window named "Hello OpenCV" 
        # and display our captures frame
        cv2.imshow('Hello OpenCV', frame)

        # wait for the user to press "q" before exiting
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # free the webcam devicce
    cam.release()
    # close "Hello OpenCV"
    cv2.destroyWindow('Hello OpenCV')

if __name__ == "__main__":
    main()