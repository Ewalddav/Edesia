from bs4 import BeautifulSoup
import requests

from modules.crawler import Crawler

class SeriousEatsCrawler(Crawler):

    def start(self):
        urls = self.crawl()
        #self.scrape(urls)

    def crawl(self):
        urls = []
        home_page = requests.get(self.website.baseUrl)
        soup = BeautifulSoup(home_page.text, 'html.parser')

        all_links = soup.find_all('a')
        for link in all_links:
            href = link.get('href')
            if self.website.baseUrl in href:
                print(link.get('href'))
                urls.append(link.get('href'))
        return urls

    def _crawl_links(self, url, level):
        links = []
