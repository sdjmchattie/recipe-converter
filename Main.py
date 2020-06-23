import sys
from urllib.parse import urlparse

from Gousto.RecipeParser import RecipeParser
from GoustoToPaprikaConverter import GoustoToPaprikaConverter
from Paprika.RecipeWriter import RecipeWriter
from RequestDownloader import RequestDownloader

recipe_url = sys.argv[1]
output_filename = urlparse(recipe_url)[2].rpartition('/')[2]

print('Starting recipe conversion.')
html_downloader = RequestDownloader(recipe_url)

print('Downloading and parsing recipe.')
gousto_parser = RecipeParser(html_downloader.content)

print('Converting recipe to Paprika: %s.' % gousto_parser.name)
converter = GoustoToPaprikaConverter()
paprika_recipe = converter.convert(gousto_parser, recipe_url)

print('Writing recipe file.')
recipe_writer = RecipeWriter(paprika_recipe)
saved_filename = recipe_writer.save(output_filename)

print("Completed writing file '%s'" % saved_filename)
