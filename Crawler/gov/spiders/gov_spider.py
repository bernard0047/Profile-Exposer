import scrapy
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from functions import pred
import scrape

class govSpider(scrapy.Spider):
    name = "mygovscraper"
    allowed_domains = []
    start_urls = []
    def __init__(self, filename="starter_sites.txt", *args, **kwargs):
        super(govSpider, self).__init__(*args, **kwargs)
        
        if(filename):    
            with open(filename,'r') as f:
                for u in f:
                    u = u.strip()
                    self.start_urls.append(u)
                    self.allowed_domains.append(urlparse(u).netloc)


    def start_requests(self):    
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback = self.parse)

    
    def parse(self,response):

        # self.logger.info("Scraped %s", response.url)
        f = open('log.txt', 'a')
        f.write("Scraped {}\n".format(response.url))
        f.close()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        scrape.parse_soup(response.url,soup.body)

        for href in soup.find_all('a'):
            try:
                raw = href["href"]
                tag = href.text
            except:
                continue

            if(raw[0]=='h' or raw[0]=='/'):
                if(pred(tag)):
                    # print(tag)
                    # f2 = open("tags.txt", 'a')
                    # f2.write(tag)
                    # f2.write("\n")
                    # f2.close()    
                    new = response.urljoin(raw)
                    if(urlparse(new).netloc in self.allowed_domains):
                        yield scrapy.Request(new, self.parse)