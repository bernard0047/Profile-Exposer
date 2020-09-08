import scrapy
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

class govSpider(scrapy.Spider):
    name = "mygovscraper"
    allowed_domains = ["india.gov.in", "uaecabinet.ae","gov.za"]
    start_urls = [
        "https://www.india.gov.in",
        "https://uaecabinet.ae/en/cabinet-members",
        "https://www.gov.za/",
        ]
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

        self.logger.info("Scraped %s", response.url)
        f = open('log.txt', 'a')
        f.write("Scraped {}\n".format(response.url))
        f.close()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for href in soup.find_all('a'):
            try:
                raw = href["href"]
            except:
                continue
            # f2 = open("tags.txt", 'a', encoding='utf-8')
            # f2.write(href.text)
            # f2.write("\n")
            # f2.close()
            if(raw[0]=='h' or raw[0]=='/'):
                new = response.urljoin(raw)
                yield scrapy.Request(new, self.parse)