import sys, time, cv2
import numpy as np
from skimage import draw

BRUSHES = 50
flowers1 = "TestImages/FlowersVase1.jpeg"

def process(inputImage, brushSize):
    start = time.time()
    
    brushSizeInt = int(brushSize)
    margin = brushSizeInt * 2
    halfBrushSizeInt = brushSizeInt // 2
    
    shape = ((inputImage.shape[0] - 2 * margin) // brushSizeInt, (inputImage.shape[1] - 2 * margin) // brushSizeInt)
    brushes = [draw.disk((halfBrushSizeInt, halfBrushSizeInt), halfBrushSizeInt) for _ in range(BRUSHES)]

    result = np.zeros(inputImage.shape, dtype=np.uint8)

    for x in range(margin, inputImage.shape[0] - margin, brushSizeInt):
        for y in range(margin, inputImage.shape[1] - margin, brushSizeInt):
            diskXs, diskYs = brushes[0]
            result[x + diskXs, y + diskYs] = inputImage[x, y]
    
    return result, time.time() - start


inputImage = cv2.imread(flowers1)
brushSize = 10.0

if inputImage.ndim < 3:
    sys.exit('Only RGB or RGBA images supported.')
elif inputImage.ndim == 4:
    inputImage = inputImage[:, :, :3]

result, duration = process(inputImage, brushSize = brushSize)
print('Processed in', round(duration, 2), 'seconds.')

def showImage(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage(result)
folderPath = "SimpleImpressionistFilterTests"
outputImage = f"IFBrushSize{brushSize}.jpg"
cv2.imwrite(f"{folderPath}/{outputImage}", result)