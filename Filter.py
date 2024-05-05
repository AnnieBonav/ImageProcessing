from abc import ABC, abstractmethod

# A filter can:
# - Apply the filter to an image (returns the image)
# - Preview an image it receives (needs the image)
# - Save an image (needs a path)

class Filter(ABC):
    def __init__(self, brush_size):
        self.brush_size = brush_size

    # This method will be implemented by the subclasses
    @abstractmethod
    def apply(self, image):
        pass

    def applyAndPreview(self, image):
        appliedFilterImage = self.apply(image)
        self.preview(appliedFilterImage)

    def preview(self, image):
        pass

    def save(self, image, fileName = "FooImage", path = ""):
        pass

class BlackWhiteFilter(Filter):
    def apply(self, image):
        # Implement the logic to apply the black and white filter to the image
        pass

class BlurFilter(Filter):
    def apply(self, image):
        # Implement the logic to apply the blur filter to the image
        pass

class DotsFilter(Filter):
    def apply(self, image):
        # Implement the logic to apply the sharpen filter to the image
        pass

class GranulateFilter(Filter):
    def apply(self, image):
        # Implement the logic to apply the granulate filter to the image
        pass

class ImpressionistFilter(Filter):
    def apply(self, image):
        # Implement the logic to apply the impressionist filter to the image
        pass

class SepiaFilter(Filter):
    def apply(self, image):
        # Implement the logic to apply the sepia filter to the image
        pass


# Usage
image = "Sample Image"
bwFilter = BlackWhiteFilter()
blurFilter = BlurFilter()
dotsFilter = DotsFilter()
granulatedFilter = GranulateFilter()
impressionistFilter = ImpressionistFilter()
sepiaFilter = SepiaFilter()

sepiaModifiedImage = sepiaFilter.apply(image)
sepiaFilter.save(image = sepiaModifiedImage, fileName = "SepiaTest")

bwModifiedImage = bwFilter.apply(image)
bwFilter.save(image = bwModifiedImage, fileName = "BWTest")