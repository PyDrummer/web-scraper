import requests
from bs4 import BeautifulSoup
import time

def get_citations_needed_count(entered_url):
    response = requests.get(entered_url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    all_results = len(result)
    return f'The total citations needed is: {all_results}'

def get_citations_needed_report(url_given):
    response = requests.get(url_given)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    p_tags = soup.find_all('p')
    li_tags = soup.find_all('li')

    all_cites = ''
    for cites in p_tags:
        if cites.find('sup', class_='noprint Inline-Template Template-Fact'):
            all_cites += f'Citation needed for: {cites.text.strip()} '

    for cites in li_tags:
        if cites.find('sup', class_='noprint Inline-Template Template-Fact'):
            all_cites += f'Citation needed for: {cites.text.strip()} '
            
    return all_cites


    ### The original way i did this, not quite what i needed
    #     result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    # all_cites = ''
    
    # #all the citations .find_all('sup', class_='noprint Inline-Template Template-Fact')

    # for cites in result:
    #     # print(cites.previousSibling)
    #     if cites.previousSibling:
    #         cite = cites.previousSibling.strip()
    #         all_cites += 'Citation needed for :' + cite + ' '

    # return all_cites

url = 'https://en.wikipedia.org/wiki/List_of_Roman_deities'

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))