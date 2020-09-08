'''
Returns list of lists of div/table text and related links
Date Created:  09/09/2020
Author: https://github.com/bernard0047
'''


from bs4 import BeautifulSoup
import requests

def sc_table(url, soup):
    tds = soup.findAll("td")
    if len(tds) == 0:
        return 0
    result = []
    for td in tds:
        content = td.text.strip().replace("\n", "")
        ##if name_model(content)==0:     ###PLUG IN NLP NAME CHECK
        ##  continue
        tags = td.findAll("a", href=True)
        links = [tag["href"] for tag in tags]
        if links:
            for i in range(len(links)):
                if "http" not in links[i]:
                    links[i] = url + links[i]
        result.append([content, links])
    return result


def sc_divs(url, soup):
    divs = soup.findAll("div")
    result = []
    for div in divs:
        content = div.text.strip().replace("\n", "")
        ##if name_model(content)==0:     ###PLUG IN NLP NAME CHECK
        ##  continue
        tags = div.findAll("a", href=True)
        links = [tag["href"] for tag in tags]
        if links:
            for i in range(len(links)):
                if "http" not in links[i]:
                    links[i] = url + links[i]
        content = div.text.strip().replace("\n", "")
        result.append([content, links])
    return result

def parse(url, soup):
    if sc_table(url, soup) is not 0:
        return sc_table(url, soup)
    return sc_divs(url, soup)

##for testing:
def main():
    urls = ["https://www.india.gov.in/my-government/whos-who/council-ministers", "https://www.gov.za/about-government/leaders", "https://uaecabinet.ae/en/cabinet-members", "https://www.india.gov.in/my-government/whos-who/chiefs-armed-forces", "https://www.india.gov.in/my-government/indian-parliament/lok-sabha"]
    site = requests.get(urls[0]).content
    soup = BeautifulSoup(site)
    print(parse(urls[0], soup))

if __name__=="__main__":
    main()
