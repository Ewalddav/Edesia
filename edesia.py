import multiprocessing

from modules.crawler import Crawler
from modules.website import Website

class Edesia(object):

    def __init__(self):
        self.crawlers = []
        self.initCrawlers()

    def run(self):
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

if __name__ == '__main__':
    edesia = Edesia()
    edesia.run()
     