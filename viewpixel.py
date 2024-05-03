import cv2
import sys

def main():
    # Read file from the command line
    image = cv2.imread(sys.argv[1])

    # Print the image array to the console
    print(image)
    
    # Show image on screen
    cv2.imshow(sys.argv[1], image)

    # Pause the program until a key is pressed
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()