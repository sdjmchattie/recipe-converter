from Gousto.RecipeParser import RecipeParser
from ImageDownloader import ImageDownloader
from Paprika.PhotoProcessor import PhotoProcessor
from Paprika.RecipeData import RecipeData


class GoustoToPaprikaConverter:
    def __init__(self):
        self.photo_processor = PhotoProcessor()

    def convert(self, recipe_parser, recipe_url):
        recipe = RecipeData()
        recipe.source = RecipeParser.source
        recipe.servings = RecipeParser.servings
        recipe.name = recipe_parser.name
        recipe.source_url = recipe_url
        recipe.description = recipe_parser.description
        recipe.prep_time = recipe_parser.prep_time

        recipe.ingredients = GoustoToPaprikaConverter._generate_ingredients(recipe_parser.ingredients)
        recipe.directions = GoustoToPaprikaConverter._generate_directions(recipe_parser.directions)

        self._insert_photo_data(recipe, recipe_parser.main_photo_url, recipe_parser.step_photo_urls)

        return recipe

    def _insert_photo_data(self, recipe, main_photo_url, step_photo_urls):
        step_photo_data = []
        for i, photo_url in enumerate(step_photo_urls, start=1):
            image = ImageDownloader.download(photo_url)
            step_photo_data.append(self.photo_processor.process(image, 'Step %i' % i))

        main_photo = ImageDownloader.download(main_photo_url)
        recipe.photos = [self.photo_processor.process(main_photo, 'Main image')]
        recipe.photos += step_photo_data

        self.photo_processor.output_width = 280
        self.photo_processor.output_height = 280
        main_photo_data = self.photo_processor.process(main_photo, 'Main image')
        recipe.photo = main_photo_data.filename
        recipe.photo_data = main_photo_data.data
        recipe.photo_hash = main_photo_data.hash
        recipe.photo_large = recipe.photos[0].filename

    @staticmethod
    def _generate_ingredients(ingredients_list):
        return '\n'.join(ingredients_list)

    @staticmethod
    def _generate_directions(directions_list):
        all_directions = []
        for i, paragraphs in enumerate(directions_list, start=1):
            joined_paragraphs = '\n\n'.join(paragraphs)
            all_directions.append('[photo:Step %i]\n\n**Step %i:** %s' % (i, i, joined_paragraphs))

        return '\n\n'.join(all_directions)
