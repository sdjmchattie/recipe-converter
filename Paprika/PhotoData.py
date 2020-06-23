import base64
import hashlib
import io
from uuid import uuid4 as uuid


class PhotoData:
    def __init__(self, name):
        self.name = name
        self.filename = '%s.jpg' % str(uuid()).upper()
        self.data = ''
        self.hash = ''

    def add_photo(self, photo):
        self.data, self.hash = PhotoData._photo_data_and_hash(photo)

    @property
    def dict_serialize(self):
        return {
            'name': self.name,
            'filename': self.filename,
            'data': self.data,
            'hash': self.hash,
        }

    @staticmethod
    def _photo_data_and_hash(photo):
        sha256 = hashlib.sha256()

        with io.BytesIO() as memory_file:
            photo.save(memory_file, 'JPEG')
            photo_data = memory_file.getvalue()
            base64_bytes = base64.b64encode(photo_data)
            sha256.update(photo_data)

        return base64_bytes.decode('ascii'), sha256.hexdigest()

