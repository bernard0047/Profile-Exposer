'''
Returns list of lists of div/table text and related links after
checking if name is present in text.
Date Created:  09/09/2020
Author: https://github.com/bernard0047
'''


from bs4 import BeautifulSoup
import requests
from functions import *

def has_name(text):
    doc = nlp(text)
    count=0
    for ent in doc.ents:
        if ent.label_=='PERSON':
            count+=1
    if count in range(1,3):  #max name intities from a single name <fn>+<ln>=2
        return 1
    return 0

def sc_table(url, soup):
    tds = soup.findAll("td")
    if len(tds) == 0:
        return 0

    result = []
    repeat_check = []
    for td in tds:
        content = td.text.strip().replace("\n", " ")
        if content in repeat_check:
            continue
        repeat_check.append([content])

        if has_name(content) == 0:
            continue
        
        tags = td.findAll("a", href=True)
        links = [tag["href"] for tag in tags]
        if links:
            for i in range(len(links)):
                if "http" not in links[i]:
                    links[i] = url + links[i]

        result.append([content, links])

    #print(len(repeat_check),repeat_check)
    return result


def sc_divs(url, soup):
    divs = soup.findAll("div")

    result = []
    repeat_check = []
    for div in divs:
        content = div.text.strip().replace("\n", " ")
        if content in repeat_check:
            continue
        repeat_check.append(content)

        if has_name(content) == 0:
            continue

        tags = div.findAll("a", href=True)
        links = [tag["href"] for tag in tags]
        if links:
            for i in range(len(links)):
                if "http" not in links[i]:
                    links[i] = url + links[i]

        result.append([content, links])
        
    #print(len(repeat_check),repeat_check)
    return result

def parse(url, soup):
    if sc_table(url, soup) is not 0:
        return sc_table(url, soup)
    return sc_divs(url, soup)


# #for testing:
# def main():
#     urls = ["https://www.india.gov.in/my-government/whos-who/council-ministers", "https://www.gov.za/about-government/leaders", "https://uaecabinet.ae/en/cabinet-members", "https://www.india.gov.in/my-government/whos-who/chiefs-armed-forces", "https://www.india.gov.in/my-government/indian-parliament/lok-sabha"]
#     site = requests.get(urls[2]).content
#     soup = BeautifulSoup(site,"html.parser")
#     return(parse(urls[2], soup))

# if __name__=="__main__":
#     result = main()
#     print(len(result))
#     print(result)
#     with open('new.txt','w') as f:
#         for r in result:
#             for rr in r:
#                 for res in rr:
#                     f.write(res)
#                 f.write("\n")
#             f.write("\n")
#     f.close()

