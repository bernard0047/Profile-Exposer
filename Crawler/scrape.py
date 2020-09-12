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
    doc = nlpN(text)
    prefs = nlpS(text)
    count=0
    plist = []
    for pref in prefs.ents:
        #print(pref.text)
        plist.append(pref.text)
    for ent in doc.ents:
        if ent.label_=='PERSON':
            #print(ent.text)
            count+=1
    if len(plist)>0: #salutation is present
        return 1
    if count in range(1,4): #max name intities from a single name <fn>+<ln>=2
        return 1
    return 0

def sc_table(url, soup):
    tds = soup.findAll("td")
    if len(tds) == 0:
        return 0

    result = []
    repeat_check = []
    for td in tds:
        content = td.text.strip().replace("\n", "")
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
        content = div.text.strip().replace("\n","")
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

def parse_soup(url, soup):
    if sc_table(url, soup) is not 0:
        return sc_table(url, soup)
    return sc_divs(url, soup)


# #for testing:
# def main():
#     urls = ["https://www.india.gov.in/my-government/whos-who/council-ministers", "https://www.gov.za/about-government/leaders", "https://uaecabinet.ae/en/cabinet-members", "https://www.india.gov.in/my-government/whos-who/chiefs-armed-forces", "https://www.india.gov.in/my-government/indian-parliament/lok-sabha"]
#     url2 = "https://www.india.gov.in/my-government/whos-who/chief-ministers"
#     site = requests.get(url2).content
#     soup = BeautifulSoup(site,"html.parser")
#     return(parse_soup(url2, soup))

# if __name__=="__main__":
#     result = main()
#     print(len(result))
#     print(result)
#     # with open('new.txt','w') as f:
#     #     for r in result:
#     #         for rr in r:
#     #             for res in rr:
#     #                 f.write(res)
#     #             f.write("\n")
#     #         f.write("\n")
#     # f.close()

