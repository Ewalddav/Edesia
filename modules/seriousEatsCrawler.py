from bs4 import BeautifulSoup
import requests

from modules.crawler import Crawler

class SeriousEatsCrawler(Crawler):
    _urls = set()

    def start(self):
        self.crawl()
        self.scrape()

    def crawl(self):
        home_page = requests.get(self.website.baseUrl)
        soup = BeautifulSoup(home_page.text, 'html.parser')

        all_links = soup.find_all('a')
        for link in all_links:
            self._crawl_links(link)
        print(len(self._urls))

    def _crawl_links(self, link):
        href = link.get('href')
        
        if href and href.find(self.website.baseUrl) == 0 and href not in self._urls:
            self._urls.add(href)
            print(href)
            html_page = requests.get(href)
            soup = BeautifulSoup(html_page.text, 'html.parser')
            all_links = soup.find_all('a')
            for link in all_links:
                self._crawl_links(link)