import time
<<<<<<< Updated upstream
=======
import requests
from queue import Queue
>>>>>>> Stashed changes

from recipe_scrapers import scrape_me

from modules.mongoHelper import MongoHelper
from modules.parsingHelper import ParsingHelper
from modules.recipe import Recipe

class Crawler(object):
    _recipeBuffer = 100
    _urlMax = 1000000
    _urlMin = 1
    _sleepTime = 2
<<<<<<< Updated upstream
    _urls = []
=======
    # _url is the visited links for the bfs
    _urls = set()
    queue = Queue()
>>>>>>> Stashed changes

    def __init__(self, website):
        self.website = website
        self.queue.put(self.website.baseUrl)
        self._urls.add(self.website.baseUrl)

    def start(self):
        self.crawl()
        self.scrape()

    def crawl(self):
<<<<<<< Updated upstream
        for i in range(self._urlMin, self._urlMax): # Picking psuedo random numbers to get recipes
            self._urls.append(self.website.baseUrl + self.website.recipeUrl + str(i))
=======
        while not self.queue.empty():
            try:
                href = self.queue.get()
                print('Popped from queue: ', href)
                html_page = requests.get(href)
                soup = BeautifulSoup(html_page.text, 'html.parser')
                all_links = soup.find_all('a')
                for link in all_links:
                    hrefNeighbor = link.get('href')
                    if hrefNeighbor and hrefNeighbor.find(self.website.baseUrl) == 0 and hrefNeighbor not in self._urls:
                        self._urls.add(hrefNeighbor)
                        self.queue.put(hrefNeighbor)
            except Exception as e:
                print('Exception encountered while crawling: ', e)
                continue
>>>>>>> Stashed changes
        
    def scrape(self):
        recipes = []
        for url in self._urls:
            if MongoHelper.getRecipeByUrl(url).count() > 0:
                print('Recipe is already in DB for URL:{}'.format(url))
                continue

            try:    
                scraper = scrape_me(url)
            except Exception as e:
                    print('Could not parse as recipe, exception: {}'.format(e))
                    time.sleep(self._sleepTime)
                    continue
            
            name = scraper.title()
            
            if len(name) == 0 or name == '' or name is None:
                print('Could not find Recipe for URL: {}'.format(url))
                continue

            servingCount = scraper.yields()
            
            totalTime = scraper.total_time()
            
            image = scraper.image()
            
            ingredients = scraper.ingredients()

            directions = scraper.instructions()

            ratings = scraper.ratings()
            
            recipe = {'name': name, 'url': url, 'ingredients': ingredients, 'directions': directions, 'servingCount': servingCount, 'image': image, 'totalTime': totalTime, 'sourceName': self.website.name, 'ratings': ratings}

            recipes.append(recipe)
            print('Scraped Recipe: {}, from URL: {}, RecipeBatch#: {}'.format(name, url, len(recipes)))
            
            if len(recipes) >= self._recipeBuffer:
                recipeIds = MongoHelper.insertRecipes(recipes)
                recipes = []
                print('{} Recipes have been successfully written: {}'.format(Crawler._recipeBuffer, recipeIds))

            time.sleep(self._sleepTime) # Sleeping between requests to avoid limit