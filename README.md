## Scraper  
### Bicameral Minds

#### Initial Testing on
- https://www.india.gov.in
- https://uaecabinet.ae/en/cabinet-members

 ### Installing dependencies
 Make sure to use `venv` for installing dependencies. Use the following line of code to install all the required dependencies in your created virtual environment. 

	pip install -r requirements.txt

### Setting Up:
In directory `Crawler/NER Models/` go to each folder and select `Extract Here` for all 4 zip files.
Setup complete.

### Running the Crawler
Navigate to directory `Crawler/`
To run the crawler with default settings, just use:
	scrapy crawl mygovscraper
The default running time for the crawler is 3 minutes. To run the crawler for a specific amount of time, use:
	scrapy crawl mygovscraper -s CLOSESPIDER_TIMEOUT = {time in secs}

Other specific settings to configure the crawler can be found on official scrapy documentation.


