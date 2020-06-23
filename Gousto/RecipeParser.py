from lxml import html
import re


class RecipeParser:
    source = "Gousto"
    servings = "2"

    def __init__(self, html_string):
        self.__html_string = html_string

        self.__tree = None

    @property
    def _tree(self):
        if self.__tree is None:
            self.__tree = html.fromstring(self.__html_string)

        return self.__tree

    @property
    def name(self):
        return self._tree.xpath('//h1[@class="indivrecipe-title"]/text()')[0]

    @property
    def description(self):
        return self._tree.xpath('//p[@class="indivrecipe-product-description"]/text()')[0]

    @property
    def prep_time(self):
        return self._tree.xpath('//p[text()="Prep Time"]/following-sibling::*/text()')[0]

    @property
    def ingredients(self):
        parsed_ingredients = []
        for ingredient_text in self._tree.xpath('//div[@id="ingredients"]//figcaption/text()'):
            ingredient_text = ingredient_text.replace(' sachet ', ' ')
            ingredient_text = re.sub(r'(\d* x )?(?:\d )?(.+?) \((.+)\)', '\\1\\3 \\2', ingredient_text)
            ingredient_text = re.sub(r'[^\w\(\)]+$', '', ingredient_text)
            parsed_ingredients.append(ingredient_text)

        return parsed_ingredients

    @property
    def directions(self):
        steps = self._tree.xpath('//div[@class="indivrecipe-steps-container"]'
                                 '//div[@class="indivrecipe-cooking-text"]')

        parsed_steps = []
        for step in steps:
            step_paragraphs = []
            for paragraph in step.xpath('p'):
                paragraph_fragments = paragraph.xpath('descendant::text()[not(parent::span[@class="text-danger"])]')
                paragraph_text = ''.join(paragraph_fragments).strip()
                paragraph_text = re.sub(r'^(\w+:)', '**\\1**', paragraph_text)
                paragraph_text += '.' if re.match(r'.*[\w]', paragraph_text) else ''
                step_paragraphs.append(paragraph_text)

            parsed_steps.append(step_paragraphs)

        return parsed_steps

    @property
    def main_photo_url(self):
        return self._tree.xpath('//div[contains(@class, "indivrecipe-product-photo")]//source/@data-srcset')[0]

    @property
    def step_photo_urls(self):
        return self._tree.xpath('//div[@class="indivrecipe-steps-container"]//picture'
                                '//source[last()]/@data-srcset')