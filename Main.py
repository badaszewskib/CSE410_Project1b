import cv2
import os

# Placeholder feature extract function, this should be replaced with the entire program logic
def feature_extract(image):
    # CURRENT FUNCTIONALITY - OPEN INPUT IMAGES IN SUCCESSION
    cv2.imshow("Image", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


# !!! Program execution begins here !!!
inputPath = 'data\input'

for fileDir in os.listdir(inputPath):
    fileDir = inputPath + '\\' + fileDir
    try:
        if fileDir.endswith(".BMP"):
            img = cv2.imread(fileDir)  # Read the image file
            feature_extract(img)  # Send to actual project function
    except Exception as e:
        raise e
        print("File error")