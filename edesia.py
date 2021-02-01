from multiprocessing import Process

from modules.crawler import Crawler
from modules.website import Website

class Edesia(object):

    def __init__(self):
        self.crawlers = []
        self.initCrawlers()

    def run(self):

        for crawler in self.crawlers:
            p = Process(target=crawler.begin, args=())
            p.start()
            p.join()

    def initCrawlers(self):
        allRecipes = Website('allrecipes', 'http://www.allrecipes.com', '/recipe/')
        self.crawlers.append(Crawler(allRecipes))

        foodRecipes = Website('food', 'http://www.food.com', '/recipe/')
        self.crawlers.append(Crawler(foodRecipes))

        seriousEatsRecipes = Website('seriouseats', 'http://www.seriouseats.com/', '/recipes/')
        self.crawlers.append(Crawler(seriousEatsRecipes))

if __name__ == '__main__':
    edesia = Edesia()
    edesia.run()