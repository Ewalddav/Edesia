import multiprocessing

from modules.allRecipesCrawler import AllRecipesCrawler
from modules.cookbooksCrawler import CookbooksCrawler
from modules.foodCrawler import FoodCrawler
from modules.seriousEatsCrawler import SeriousEatsCrawler
from modules.website import Website

class Edesia(object):

    def __init__(self):
        self.crawlers = []
        self.initCrawlers()

    def run(self):
<<<<<<< Updated upstream
        jobs = []
        
        seriousEatsRecipes = Website('seriouseats', 'https://www.seriouseats.com/', '/recipes/')
        seriousEatsCrawler = SeriousEatsCrawler(seriousEatsRecipes)
        seriousEatsCrawler.start()

        #for crawler in self.crawlers:
            #p = multiprocessing.Process(target=crawler.start, args=())
            #jobs.append(p)
            #p.start()

    def initCrawlers(self):
        #allRecipes = Website('allrecipes', 'http://www.allrecipes.com', '/recipe/')
        #self.crawlers.append(AllRecipesCrawler(allRecipes))

        #foodRecipes = Website('food', 'http://www.food.com', '/recipe/')
        #self.crawlers.append(FoodCrawler(foodRecipes))

        #cookbooksRecipes = Website('cookbooks', 'http://www.cookbooks.com', '/Recipe-Details.aspx?id=')
        #self.crawlers.append(CookbooksCrawler(cookbooksRecipes))

        seriousEatsRecipes = Website('seriouseats', 'http://www.seriouseats.com/', '/recipes/')
        self.crawlers.append(SeriousEatsCrawler(seriousEatsRecipes))
=======
        processes = []

        for crawler in self.crawlers:
            p = multiprocessing.Process(target=crawler.begin, args=[])
            processes.append(p)
            p.start()
        
        for p in processes:
            p.join()

    def initCrawlers(self):
        allRecipes = Website('allrecipes', 'https://www.allrecipes.com', '/recipe/')
        self.crawlers.append(Crawler(allRecipes))

        foodRecipes = Website('food', 'https://www.food.com', '/recipe/')
        self.crawlers.append(Crawler(foodRecipes))

        seriousEatsRecipes = Website('seriouseats', 'https://www.seriouseats.com/', '/recipes/')
        self.crawlers.append(Crawler(seriousEatsRecipes))
>>>>>>> Stashed changes

if __name__ == '__main__':
    edesia = Edesia()
    edesia.run()
     