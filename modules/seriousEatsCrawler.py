from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me

import requests

from modules.crawler import Crawler

class SeriousEatsCrawler(Crawler):
    # _url is the visited links for the bfs
    _urls = set()
    queue = []
    real_links = []
    

    def start(self):
        self.crawl()
        self.scrape()

    # this method use bfs to crawl all the websites into _urls field
    def crawl(self):
        home_page = requests.get(self.website.baseUrl)
        print(self.website.baseUrl)
        soup = BeautifulSoup(home_page.text, 'html.parser')
        self.queue.append(self.website.baseUrl)
        self._urls.add(self.website.baseUrl)
        while self.queue:
            href = self.queue.pop(0)
            try:
                scraper = scrape_me(href, wild_mode=True)
                print(href)
                self.real_links.append(href)
                scraper.title()
                scraper.instructions()
                #print(scraper.ingredients())
            except:
                print('This url is not scrapeable ' + href)
            html_page = requests.get(href)
            soup = BeautifulSoup(html_page.text, 'html.parser')
            all_links = soup.find_all('a')
            for link in all_links:
                hrefNeighbor = link.get('href')
                if hrefNeighbor and hrefNeighbor.find(self.website.baseUrl) == 0 and hrefNeighbor not in self._urls:
                    self._urls.add(hrefNeighbor)
                    self.queue.append(hrefNeighbor)

