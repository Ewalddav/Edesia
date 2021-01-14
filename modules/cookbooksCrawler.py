import time

from bs4 import BeautifulSoup
import requests

from modules.crawler import Crawler
from modules.mongoHelper import MongoHelper
from modules.recipe import Recipe

class CookbooksCrawler(Crawler):
    _urlMax = 1060000
    _urlMin = 1
    _sleepTime = 1

    def scrape(self, urls):
        recipes = []
        for url in urls:
            try:
                if MongoHelper.getRecipeByUrl(url).count() > 0:
                    print('Recipe is already in DB for URL:{}'.format(url))
                    continue

                home_page = requests.get(url)
                soup = BeautifulSoup(home_page.text, 'html.parser')
                
                if soup.find_all("p", class_="H1")[0].text == "Could NOT Open Recipe Page Due To:":
                    print('Could not find Recipe for URL: {}'.format(url))
                    continue

                name = soup.find_all("p", class_="H2")[0].font.text
                
                if len(name) == 0 or name == '' or name is None:
                    print('Could not find Recipe for URL: {}'.format(url))
                    continue

                servingCount = ''
                
                totalTime = ''
                
                image = ''
                
                ingredientHtml = soup.find_all("p", class_="H1")[0].contents
                directions = soup.find_all("p", class_="H1")[1].text.strip()

                if len(ingredientHtml) == 0: # If there is a picture, the ingredients are one below
                    ingredientHtml = soup.find_all("p", class_="H1")[1].contents
                    directions = soup.find_all("p", class_="H1")[2].text.strip()

                ingredientsText = ingredientHtml[0]
                if len(ingredientHtml) > 2:
                    for i in range(2, len(ingredientHtml), 2):
                        ingredientsText += '|' + ingredientHtml[i]
                
                ingredients = ingredientsText.split('|')
                
                recipe = {'name': name, 'url': url, 'ingredients': ingredients, 'directions': directions, 'servingCount': servingCount, 'image': image, 'totalTime': totalTime, 'sourceName': self.website.name}

                recipes.append(recipe)
                print('Scraped Recipe: {}, from URL: {}, RecipeBatch#: {}'.format(name, url, len(recipes)))
                
                if len(recipes) >= Crawler._recipeBuffer:
                    recipeIds = MongoHelper.insertRecipes(recipes)
                    recipes = []
                    print('100 Recipes have been successfully written: {}'.format(recipeIds))

                time.sleep(self._sleepTime) # Sleeping 2 seconds between recipe scrapes
            except Exception as e:
                print('Error scraping url: {}, with exception: {}'.format(url, str(e)))
