import gzip
import json


class RecipeWriter:
    def __init__(self, recipe_data):
        self.__recipe_data = recipe_data

    def save(self, filename):
        full_filename = filename + '.paprikarecipe'
        with gzip.GzipFile(filename=full_filename, mode="w") as file:
            file.write(json.dumps(self.__recipe_data.dict_serialize).encode())

        return full_filename
