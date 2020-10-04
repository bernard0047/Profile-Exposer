## Team name: Bicameral Minds
**Team members:**
1. Avik Kuthiala  (101803116)
2. Naman Tuli (101983040)
 #### 	KINDLY READ THE ENTIRE README FILE. IT CONTAINS SOME IMPORTANT INFERENCES.
**Video Link:**
>https://youtu.be/96deQshdM6g
###### Kindly view the video in 720p or above.
### Presentation File [Here](https://github.com/bernard0047/Bicameral-Minds/blob/master/Design/Bicameral%20Minds.pdf).

 ## Installing Dependencies
 
 Make sure to use `venv` for installing dependencies. Use the following line of code to install all the required dependencies in your created virtual environment. To make an env, run:
 
	python -m venv myenv
	myenv\Scripts\activate.bat
###### Replace your environment name with myenv.
Run the following in your terminal:

	pip install -r requirements.txt
**Note:** If we missed any dependency, kindly pip install the library which was not found.

### Setting Up
First navigate to `/Bicameral-Minds`, the repository you cloned.
After installing the dependencies, navigate to directory `Code/NER Models/` go to each folder and select `Extract Here` for all 4 zip files.
Setup complete.


## Running the Crawler
Navigate to directory `Code/`
To run the crawler with default settings, just use:

	scrapy crawl mygovscraper

The default running time for the crawler is 3 minutes. To run the crawler for a specific amount of time, use:

	scrapy crawl mygovscraper -s CLOSESPIDER_TIMEOUT=<time in secs>
Example (To run for 1800 seconds):

	scrapy crawl mygovscraper -s CLOSESPIDER_TIMEOUT=1800
**Note:** Do not give space after  CLOSESPIDER_TIMEOUT=  as it  will give error.
Other specific settings to configure the crawler can be found on official scrapy documentation.<br>
A database will be created:
>database.csv

## Post Processing 
Navigate to directory `Code/` and run in terminal:

	python postprocess.py
New database will be created:
> clean_database.csv

## Important Notes and Inferences:
1. **The problem statement mentioned that 15 countries will be considered for the hackathon. Hence we used only 3 countries to train our NLP models(since training for 15 countries and then producing results on them would not make sense). But in the FAQs of the e-mail sent by MSC on 17-09-2020(for deadline extention), it was mentioned, "Try to train with as many countries'  govt websites' HTML structures as possible". We trained with data for 3 countries and scaled it for 15, hence we believe we can train for 15 countries and scale the solution to 70-80 countries. However, it was not feasible to carry out this upscaling in under 4 days.**
2. The crawler visits all the sites, but without following any particular order. It may happen that you would have to wait for some while before you start seeing meaningful websites appear in logs.
3. After the crawler starts running, you can see the sites that are being crawled in `Code/log.txt` file. Currently it has been emptied out.
4. The sites which are to be crawled in are to be mentioned in `starter_sites.txt` currently, the file contains all 14 sites to be considered. We strongly advise that for testing purposes, try with only 1 site since **crawling govt sites is a very computationally costly process**.
5.  The sample [database](https://github.com/bernard0047/Bicameral-Minds/blob/master/DATABASE/sample_database(57600s).csv) that we created was run for a total of 16 hours. 
6.  Results on news article pages: 

![Profile extracted from news article](https://github.com/bernard0047/Bicameral-Minds/blob/master/Design/news.jfif)
The above image is an example of a news article webpage from which Prefix, Name and Position held was correctly extracted. The scraper is not designed to extract profiles from huge paragraphs, yet we noticed a few profiles being successfully extracted from news articles as well. 

### High Level Diagram of Solution:
![HLD](https://github.com/bernard0047/Bicameral-Minds/blob/master/Design/HLDbw.png)

### Low Level Diagram of Scraper (universal):
![LLD_scraper](https://github.com/bernard0047/Bicameral-Minds/blob/master/Design/LLDscraperbw.png)

### Low Level Diagram of Crawler:
![LLD_crawler](https://github.com/bernard0047/Bicameral-Minds/blob/master/Design/LLD_crawlerbw.png) 

### API
The API has been built using node.js and express.js and functions by fetching data from a mongo.db database.\
Ensure that you have a functioning mongo.db database setup before running the API on postman.

Navigate to the `db_api` directory and install the required modules using npm:\
`npm install express node body-parser mongoose nodemon`

First start the database server using -\
`mongod`

To import the csv database into mongo.db, run the following command -\
`mongoimport --type csv -d record_db -c records --headerline --drop final_db.csv`

Then make sure you are in `db_api/` and run the command - \
`npm run start`

Now the setup is running and you can use `postman` to test your API. The parameters need to be passed using `x-www-form-urlencode` to the `Body`.

The API will be hosted on `http://localhost:3000/`\
To get all records, use -  `http://localhost:3000/records`\

![All](https://github.com/bernard0047/Bicameral-Minds/blob/master/Design/find_all.PNG) 

To get details of a single person, use - \
`http://localhost:3000/findrecord`  and pass parameter `name` as explained above and in the accompanying video.


![All](https://github.com/bernard0047/Bicameral-Minds/blob/master/Design/find_Modi.PNG)


Tanmay Gupta
