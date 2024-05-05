import sys, time, cv2
import numpy as np
from skimage import draw

flowers1 = "TestImages/FlowersVase1.jpeg"

def filterImage(inputImage, brushSize):
    start = time.time()
    
    brushSizeInt = int(brushSize)
    margin = brushSizeInt * 2
    halfBrushSizeInt = brushSizeInt // 2
    
    # shape = ((inputImage.shape[0] - 2 * margin) // brushSizeInt, (inputImage.shape[1] - 2 * margin) // brushSizeInt)
    brush = draw.disk((halfBrushSizeInt, halfBrushSizeInt), halfBrushSizeInt)
    result = np.zeros(inputImage.shape, dtype=np.uint8)

    for x in range(margin, inputImage.shape[0] - margin, brushSizeInt):
        for y in range(margin, inputImage.shape[1] - margin, brushSizeInt):
            brushX, brushY = brush
            result[x + brushX, y + brushY] = inputImage[x, y]
    
    return result, time.time() - start

inputImage = cv2.imread(flowers1)
brushSize = 20.0

result, duration = filterImage(inputImage, brushSize = brushSize)
print('Processed in', round(duration, 2), 'seconds.')

def showImage(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage(result)
folderPath = "TestingBrush"
outputImage = f"BrushSize{brushSize}.jpg"

cv2.imwrite(f"{folderPath}/{outputImage}", result)