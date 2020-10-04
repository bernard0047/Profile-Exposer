'''
Returns list of lists of div/table text and related links after
checking if name is present in text.
Writes the list to csv
Date Created:  09/09/2020
Author: https://github.com/bernard0047
'''


from bs4 import BeautifulSoup
import requests
from functions import *
import pandas as pd
from csv import writer


def returner(string):
    doc = nlp_Name(string)
    name=""
    stop_words=['Shri','Smt','Smt.','Dr.','Dr','Mr','Mrs','Cabinet','Minister','Prime','Deputy','Ministry','of','Technology','Defence',
                'Contact','Facebook','Account'] #some very common stop-words
    for count,ent in enumerate(doc.ents):
        name+=ent.text+" "
        if count==0:
            break
    ret_name=""
    for words in name.split(" "):
        if words not in stop_words:
            ret_name+=words+" "

    doc =nlp_Min(string)
    ministry=""
    for ent in doc.ents:
        ministry+=ent.text+" "
    
    doc =nlp_Pref(string)
    prefix=""
    for ent in doc.ents:
        prefix+=ent.text+" "

    return prefix, ret_name, ministry

def has_name(text):  #  //cleaner fn
    doc = nlp_Name(text)
    prefs = nlp_Pref(text)
    names = []
    plist = []
    for pref in prefs.ents:
        plist.append(pref.text)
    for ent in doc.ents:
        if ent.label_=='PERSON':
            names.append(ent.text)
    names = ' '.join(names).strip()
    spaces = names.count(' ')
    if len(plist)==1: #1 salutation is present
        return 1
    if names.isnumeric(): #clean numeric preds manually
        return 0
    if spaces<6:  #spaces check for filtering
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
        content =  sc_table(url, soup)
    else:
        content =  sc_divs(url, soup)
    #return content
    write_obj = open("database.csv", 'a+', newline='')
    csv_writer = writer(write_obj)
    for items in content:
        prefix,ret_name,ministry=returner(items[0])
        l1 = [prefix.strip(),ret_name.strip(),ministry.strip()]
        if l1[0] == '' and l1[1] == '': #no name no salutation //cleaner step
            continue
        if l1[1] in l1[2]:   #name found in ministry //cleaner step
            continue
        l1.append(' '.join(items[1])) #urls
        csv_writer.writerow(l1)
    write_obj.close()


# for hacktoberfest
# #for testing:
# def main():
#     urls = ["https://www.india.gov.in/my-government/whos-who/council-ministers", "https://www.gov.za/about-government/leaders", "https://uaecabinet.ae/en/cabinet-members", "https://www.india.gov.in/my-government/whos-who/chiefs-armed-forces", "https://www.india.gov.in/my-government/indian-parliament/lok-sabha"]
#     url2 = "https://www.india.gov.in/my-government/whos-who/chief-ministers"
#     site = requests.get(urls[0]).content
#     soup = BeautifulSoup(site,"html.parser")
#     return(parse_soup(urls[0], soup.body))
    

# if __name__=="__main__":
#     res = main()
#     print(res)

    

