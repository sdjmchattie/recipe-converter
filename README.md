# Recipe Converter

A Python 3 based converter for Gousto recipes into Paprika

## Usage

You can scrape the data from a [Gousto](https://www.gousto.co.uk) recipe such as [https://www.gousto.co.uk/cookbook/chicken-recipes/chicken-ciabatta-sandwich-with-garlic-mayo](https://www.gousto.co.uk/cookbook/chicken-recipes/chicken-ciabatta-sandwich-with-garlic-mayo). The converter will import the ingredients and directions etc then it will create a file that can be imported into [Paprika](https://www.paprikaapp.com/).

To import the above recipe you would use:

```bash
python Main.py https://www.gousto.co.uk/cookbook/chicken-recipes/chicken-ciabatta-sandwich-with-garlic-mayo
```

This would create a file named `chicken-ciabatta-sandwich-with-garlic-mayo.paprikarecipe` which can then be imported directly into the Paprika app on either macOS or iPhone / iPad.
