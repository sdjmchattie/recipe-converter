from PIL import ImageOps

from Paprika.PhotoData import PhotoData


class PhotoProcessor:
    def __init__(self):
        self.output_width = None
        self.output_height = None

    def process(self, image, photo_name):
        photo_data = PhotoData(photo_name)
        output_image = image if self.output_width is None or self.output_height is None else self._resize_image(image)
        photo_data.add_photo(output_image)

        return photo_data

    def _resize_image(self, image):
        return ImageOps.fit(image, (self.output_width, self.output_height))
