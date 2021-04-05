import cv2
import os, math
import numpy as np

#  up image into 3px*3px chunks, makes and returns orientation map
def orientation_map(img):
    blockSize = 3
    row = -1
    col = -1
    oMap = np.zeros((int(img.shape[1]/blockSize), int(img.shape[0]/blockSize)))  # Should be 32Y x 30X
    numCols, numRows = oMap.shape
    oMap = oMap.astype(np.double)
    varX = oMap.copy()
    varY = oMap.copy()
    for x in range(0, numRows):
        row = row+1  # Increment row
        for y in range(0, numCols):
            col = col+1  # Increment col
            xPix = x*blockSize;
            yPix = y*blockSize;
            xGrad = cv2.Sobel(img[xPix:xPix+blockSize, yPix:yPix+blockSize], -1, 1, 0)
            yGrad = cv2.Sobel(img[xPix:xPix+blockSize, yPix:yPix+blockSize], -1, 0, 1)
            for i in range(0, blockSize):
                for j in range(0, blockSize):
                    print(xGrad[i][j])
                    varX[row][col] += ((xGrad[i][j])*(yGrad[i][j]))**2
                    varY[row][col] += 2*((xGrad[i][j])*(yGrad[i][j]))
        oMap[row][col] = 0.5*(math.atan(varY[row][col]/varX[row][col]))
    col = -1
    print(oMap)
    cv2.blur(img, (2,2))

# SRC: https://medium.com/@cuevas1208/fingerprint-algorithm-recognition-fd2ac0c6f5fc
# SRC: https://www.rroij.com/open-access/fingerprint-image-enhancementalgorithm-and-performance-evaluation.pdf

# Placeholder feature extract function, this should be replaced with the entire program logic
def feature_extract(img):
    # CURRENT FUNCTIONALITY - OPEN INPUT IMAGES IN SUCCESSION
    # Crop border features of image
    img = img[3:99, 2:92]
    # Resulting image size: 96Y x 90X

    orientation_map(img)
    # Display a blown up image x5
    newWidth = int(img.shape[1] * 5);
    newHeight = int(img.shape[0] * 5);
    dim = (newWidth, newHeight)
    rect = cv2.resize(img, dim)
    cv2.imshow("Image", rect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# !!! Program execution begins here !!!
inputPath = 'data\\input'

for fileDir in os.listdir(inputPath):  # Loop thru all files in data/input directory, will only work in Windows machine
    fileDir = inputPath + '\\' + fileDir
    try:
        if fileDir.endswith(".BMP"):
            image = cv2.imread(fileDir)  # Read the image file
            feature_extract(image)  # Send to actual project function
    except Exception as e:
        raise e
        print("File error")
