import io
from PIL import Image

from RequestDownloader import RequestDownloader


class ImageDownloader:
    @staticmethod
    def download(url):
        downloader = RequestDownloader(url)
        raw_data = downloader.content
        return Image.open(io.BytesIO(raw_data))