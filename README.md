## Team name: Bicameral Minds
**Team members:**
1. Avik Kuthiala  (101803116)
2. Naman Tuli (101983040)

**Video Link:**
>https://youtu.be/5m0k-aWA6L8
 #### 	KINDLY READ IMPORTANT NOTES AT THE END OF THIS README FILE.
 ## Installing Dependencies
 
 Make sure to use `venv` for installing dependencies. Use the following line of code to install all the required dependencies in your created virtual environment. To make an env, run:
 
	conda create --name myenv
	conda activate myenv
##### Replace your environment name with myenv.
**Note:** If we missed any dependency, kindly pip install the library which was not found. Run the following in your terminal:

	pip install -r requirements.txt

### Setting Up
After installing the dependencies, navigate to directory `Code/NER Models/` go to each folder and select `Extract Here` for all 4 zip files.
Setup complete.

### Running the Crawler
Navigate to directory `Code/`
To run the crawler with default settings, just use:

	scrapy crawl mygovscraper

The default running time for the crawler is 3 minutes. To run the crawler for a specific amount of time, use:

	scrapy crawl mygovscraper -s CLOSESPIDER_TIMEOUT=<time in secs>
Example (To run for 1800 seconds):

	scrapy crawl mygovscraper -s CLOSESPIDER_TIMEOUT=1800
**Note:** Do not give space after  CLOSESPIDER_TIMEOUT=  as it  will give error.

Other specific settings to configure the crawler can be found on official scrapy documentation.

### Post Processing 
Navigate to directory `Code/` and run in terminal:

	python postprocess.py
2 databases will be created:
1. database.csv
2. clean_database.csv

### Important Notes
1. After the crawler starts running, you can see the sites that are being crawled in `log.txt` file. Currently it has been emptied out.
2. The sites which are to be crawled in are to be mentioned in `starter_sites.txt` currently, the file contains all 14 sites to be considered. We strongly advise that for testing purposes, try with only 1 site since **crawling govt sites is a very computationally costly process,** the crawler would take very long before you start seeing meaningful sites being crawled.
3.  The database that we created was run for a total of 20 hours. 