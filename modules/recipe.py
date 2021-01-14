import datetime

class Recipe(object):
    _collectionName = 'recipes'

    def __init__(self, name, websiteUrl, ingredients, directions, servingCount, image, reviewCount = None, prepTime = None, cookTime = None, totalTime = None, scrapeDateTime = datetime.datetime.utcnow()):
        self.name = name
        self.websiteUrl = websiteUrl
        self.ingredients = ingredients
        self.directions = directions
        self.servingCount = servingCount
        self.image = image
        self.reviewCount = reviewCount
        self.prepTime = prepTime
        self.cookTime = cookTime
        self.totalTime = totalTime
        self.scrapeDateTime = scrapeDateTime