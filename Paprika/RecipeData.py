from datetime import datetime
from uuid import uuid4 as uuid


class RecipeData:
    def __init__(self):
        self.__uid = str(uuid()).upper()
        self.__created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.source_url = ''
        self.source = ''
        self.name = ''
        self.description = ''
        self.servings = ''
        self.prep_time = ''
        self.cook_time = ''
        self.total_time = ''
        self.ingredients = ''
        self.directions = ''
        self.photo = '%s.jpg' % str(uuid()).upper()
        self.photo_data = ''
        self.photo_hash = ''
        self.photo_large = ''
        self.photos = []
        self.difficulty = ''
        self.rating = 0
        self.categories = []
        self.notes = ''
        self.hash = ''
        self.nutritional_info = ''
        self.image_url = None

    @property
    def dict_serialize(self):
        return {
            'uid': self.__uid,
            'created': self.__created,
            'source_url': self.source_url,
            'source': self.source,
            'name': self.name,
            'description': self.description,
            'servings': self.servings,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'total_time': self.total_time,
            'ingredients': self.ingredients,
            'directions': self.directions,
            'photo': self.photo,
            'photo_data': self.photo_data,
            'photo_hash': self.photo_hash,
            'photo_large': self.photo_large,
            'photos': [photo.dict_serialize for photo in self.photos],
            'difficulty': self.difficulty,
            'rating': self.rating,
            'categories': self.categories,
            'notes': self.notes,
            'hash': self.hash,
            'nutritional_info': self.nutritional_info,
            'image_url': self.image_url,
        }
