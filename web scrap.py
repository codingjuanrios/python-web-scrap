'''
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/")

res = BeautifulSoup(html.read());

print(res.title)
'''

import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

#print(results)
#print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    
    file = open("./registro.html", "w")
    file.write(str(title_elem))
    file.write(str(company_elem))
    file.write(str(location_elem))
    file.close()
    
    print()


#print(job_elem.prettify())