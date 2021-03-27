import cv2
import os

# Usage - place data to be used inside the data>input folder, output will
# be placed into the data>output folder.


def feature_extract(image):
    cv2.imshow("Image", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


# Program execution begins here
inputPath = 'data\input'

for fileDir in os.listdir(inputPath):
    fileDir = inputPath + '\\' + fileDir
    try:
        if fileDir.endswith(".BMP"):
            # CURRENT FUNCTIONALITY - OPEN INPUT IMAGES IN SUCCESSION
            img = cv2.imread(fileDir)
            feature_extract(img)
    except Exception as e:
        raise e
        print("File error")