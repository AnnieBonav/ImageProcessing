import sys, time, cv2, random, numpy as np
from skimage import draw
from math import ceil, pi

flowers1 = "TestImages/FlowersVase1.jpeg"

brushesAmount = 5
def filterImage(inputImage, brushSize, intensity):
    global brushesAmount

    start = time.time()
    
    brushSizeInt = int(brushSize)
    expressionSize = brushSize * intensity
    margin = int(expressionSize * 2)
    halfBrushSizeInt = brushSizeInt // 2

    # shape = ((inputImage.shape[0] - 2 * margin) // brushSizeInt, (inputImage.shape[1] - 2 * margin) // brushSizeInt)
    brushes = [draw.ellipse(halfBrushSizeInt, halfBrushSizeInt, brushSize, random.randint(brushSizeInt, expressionSize), rotation = random.normalvariate(0.8, 1) * pi) for _ in range(brushesAmount)]

    result = np.zeros(inputImage.shape, dtype = np.uint8)
    print("Initial Size:", inputImage.shape)
    
    for x in range(margin, inputImage.shape[0] - margin, brushSizeInt):
        for y in range(margin, inputImage.shape[1] - margin, brushSizeInt):
            brushX, brushY = random.choice(brushes)
            result[x + brushX, y + brushY] = inputImage[x, y]
    
    
    print("Final Size:", result.shape)
    return result, time.time() - start

inputImage = cv2.imread(flowers1)
inputImage = inputImage[:, :, :3]

brushSize = 10.0
intensity = 2.0

result, duration = filterImage(inputImage, brushSize = brushSize, intensity = intensity)
print('Processed in', round(duration, 2), 'seconds.')

def showImage(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage(result)
folderPath = "TestingBrush"
outputImage = f"BrushSize{brushSize}Intensity{intensity}BrushesAmount{brushesAmount}.jpg"

cv2.imwrite(f"{folderPath}/{outputImage}", result)