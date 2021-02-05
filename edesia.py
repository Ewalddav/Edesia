from multiprocessing import Process

from modules.crawler import Crawler
from modules.website import Website

class Edesia(object):

    def __init__(self):
        self.crawlers = []
        self.initCrawlers()

    def run(self):
        processes = []

        for crawler in self.crawlers:
            p = Process(target=crawler.begin, args=())
            processes.append(p)
            p.start()
        
        for p in processes:
            p.join()

    def initCrawlers(self):
        allRecipes = Website('allrecipes', 'https://www.allrecipes.com', 'en')
        self.crawlers.append(Crawler(allRecipes))

        foodRecipes = Website('food', 'https://www.food.com', 'en')
        self.crawlers.append(Crawler(foodRecipes))

        seriousEatsRecipes = Website('seriouseats', 'https://www.seriouseats.com', 'en')
        self.crawlers.append(Crawler(seriousEatsRecipes))

        delishRecipes = Website('delish', 'https://www.delish.com', 'en')
        self.crawlers.append(Crawler(delishRecipes))

        foodnetworkRecipes = Website('foodnetwork', 'https://www.foodnetwork.com', 'en')
        self.crawlers.append(Crawler(foodnetworkRecipes))

        chefkochRecipes = Website('chefkoch', 'https://www.chefkoch.de', 'de')
        self.crawlers.append(Crawler(chefkochRecipes))

        giallozafferanoRecipes = Website('giallozafferano', 'https://www.giallozafferano.it', 'it')
        self.crawlers.append(Crawler(giallozafferanoRecipes))

        yummlyRecipes = Website('yummly', 'https://www.yummly.com', 'en')
        self.crawlers.append(Crawler(yummlyRecipes))

if __name__ == '__main__':
    edesia = Edesia()
    edesia.run()