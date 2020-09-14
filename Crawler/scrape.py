'''
Returns list of lists of div/table text and related links after
checking if name is present in text.
Date Created:  09/09/2020
Author: https://github.com/bernard0047
'''


from bs4 import BeautifulSoup
import requests
from functions import *
import pandas as pd
from csv import writer
count=0
Glob_Dict={'name':[],
        'prefix':[],
        'ministry':[],
        'gender':[],
        'links':[]}

def returner(string):
    doc = nlp_Name(string)
    name=""
    stop_words=['Shri','Smt','Smt.','Dr.','Dr','Mr','Mrs','Cabinet','Minister','Prime','Deputy','Ministry','of','Technology','Defence',
                'Contact','Facebook','Account']
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

    return ret_name,ministry,prefix

def has_name(text):
    doc = nlp_Name(text)
    prefs = nlp_Pref(text)
    count_n=0
    count_p=0
    # plist = []
    for pref in prefs.ents:
        count_p+=1
        # plist.append(pref.text)
    for ent in doc.ents:
        if ent.label_=='PERSON':
            #print(ent.text)
            count_n+=1
    if count_p==1: #salutation is present
        return 1
    if count_n in range(1,3): #max name intities from a single name <fn>+<ln>=2
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
    for items in content:
        prefix,ret_name,ministry=returner(items[0])
        l1 = [ret_name,ministry,prefix]
        l1.append(' '.join(items[1]))
        print(l1)
        with open("trial.csv", 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(l1)
    # for items in content:
    #     ret_name,ministry,prefix=returner(items[0])
    #     Glob_Dict['name'].append(ret_name)
    #     Glob_Dict['prefix'].append(prefix)
    #     Glob_Dict['ministry'].append(ministry)
    #     Glob_Dict['links'].append(' '.join(items[1]))
    # if count%5==0:
    #     df = pd.DataFrame()
    #     df['Prefix'] = Glob_Dict['prefix']
    #     df['Name'] = Glob_Dict['name']
    #     df['Ministry'] = Glob_Dict['ministry']
    #     df['urls'] = Glob_Dict['links']
    #     df.to_csv(f"trial{count}.csv")



# #for testing:
# def main():
#     urls = ["https://www.india.gov.in/my-government/whos-who/council-ministers", "https://www.gov.za/about-government/leaders", "https://uaecabinet.ae/en/cabinet-members", "https://www.india.gov.in/my-government/whos-who/chiefs-armed-forces", "https://www.india.gov.in/my-government/indian-parliament/lok-sabha"]
#     url2 = "https://www.india.gov.in/my-government/whos-who/chief-ministers"
#     site = requests.get(urls[0]).content
#     soup = BeautifulSoup(site,"html.parser")
#     parse_soup(urls[0], soup)

# if __name__=="__main__":
#     main()
#     # df = pd.DataFrame()
#     # df['Prefix'] = Glob_Dict['prefix']
#     # df['Name'] = Glob_Dict['name']
#     # df['Ministry'] = Glob_Dict['ministry']
#     # df['urls'] = Glob_Dict['links']
#     # df.to_csv("submission.csv")
    

