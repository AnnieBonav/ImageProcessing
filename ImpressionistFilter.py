import sys, random, time, cv2
import numpy as np
import skimage as ski
from skimage import draw
from math import ceil, pi

BRUSHES = 50
flowers1 = "TestImages/FlowersVase1.jpeg"

# Cargar y mostrar una imagen con Scikit-Image
img = ski.io.imread(flowers1)
ski.io.imshow(img)
def process(inputImage, brushSize, intensity):
    start = time.time()
    
    brushSizeInt = int(brushSize)
    expressionSize = brushSize * intensity
    margin = int(expressionSize * 2)
    halfBrushSizeInt = brushSizeInt // 2
    
    shape = ((inputImage.shape[0] - 2 * margin) // brushSizeInt, (inputImage.shape[1] - 2 * margin) // brushSizeInt)
    brushes = [draw.ellipse(halfBrushSizeInt, halfBrushSizeInt, brushSize, random.randint(brushSizeInt, expressionSize), rotation=random.random() * pi) for _ in range(BRUSHES)]

    result = np.zeros(inputImage.shape, dtype=np.uint8)

    for x in range(margin, inputImage.shape[0] - margin, brushSizeInt):
        for y in range(margin, inputImage.shape[1] - margin, brushSizeInt):
            ellipseXs, ellipseYs = random.choice(brushes)
            result[x + ellipseXs, y + ellipseYs] = inputImage[x, y]
    
    return result, time.time() - start


inputImage = cv2.imread(flowers1)
brushSize = 5.0
intensity = 5.0


if inputImage.ndim < 3:
    sys.exit('Only RGB or RGBA images supported.')
elif inputImage.ndim == 4:
    inputImage = inputImage[:, :, :3]

result, duration = process(inputImage, brushSize = brushSize, intensity = intensity)
print('Processed in', round(duration, 2), 'seconds.')

def showImage(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage(result)
folderPath = "ImpressionistFilterTests"
outputImage = f"IFBrushSize{brushSize}Intensity{intensity}.jpg"
cv2.imwrite(f"{folderPath}/{outputImage}", result)
