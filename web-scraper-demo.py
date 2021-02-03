import requests
from bs4 import BeautifulSoup
import time
# import urllib.request


#Remember to use your terminal for this, not the VScode terminal
url = 'https://www.monster.com/jobs/search/?q=software-engineer&where=Seattle__2C-WA&intcid=skr_navigation_nhpso_searchMain'
response = requests.get(url)

# print(response)
# print(dir(response))
# print(response.headers)

# get all the content and store it
# this is all the jumbled up html code
content = response.content
# print(content)

# Bring in our BeautifulSoup:
# Give BeautifulSoup the content from earlier and say html.parser
soup = BeautifulSoup(content, 'html.parser')
# Run dir() to see all the internal functions you can do with soup
#print(dir(soup))

# print(soup.prettify())

result = soup.find(id='SearchResults')
# print(result.prettify())
# class is a reserved word, you must add an underscore after class to make it work.
job_results = result.find_all('section', class_='card-content')
# print(job_results)

# Show the amount of sections with the class 'card-content' within job_results
# print(len(job_results))
# We can use this to iterate

# print(job_results[0])


for job in job_results:
    #print(job, end='\n' * 3)
    # use end='\n' * 3 to seperate the info each iteration
    # Find the company, location, and job name
    # get the parent element and assign it to a variable
    title = job.find('h2', class_='title')
    
    company = job.find('div', class_='company')
    
    location = job.find('div', class_='location' )
    if None in (title, company, location):
        continue
    # Now print just the text and remove the whitespace:
    # print(title.text.strip())
    # print(company.text.strip())
    # print(location.text.strip(), end='\n' * 3)


# Now parse out all the data as a dictionary and put it into final_result

final_result = []

for jobs in job_results:
    job_dict = {}

    if jobs.find('h2', class_='title'):
        title = jobs.find('h2', class_='title').text.strip()
        job_dict['Title'] = title

        company = jobs.find('div', class_='company').text.strip()
        job_dict['Company'] = company
        
        location = jobs.find('div', class_='location').text.strip()
        job_dict['Location'] = location
        final_result.append(job_dict)

print(final_result)



    
    
