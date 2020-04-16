import requests
from bs4 import BeautifulSoup
from test.badsyntax_future3 import result

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

#print(results)
#print(results.prettify())

job_elems = results.find_all('section', class_='card-content')



#===============================================================================
# PENDIENTE DE RESOLVER BUSCAR SOLO LOS ELEMENTOS DE PYTHON PERO TODA SU SECCION
#===============================================================================

# python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
# python_jobs = results.find_parent('h2', string=lambda text: 'python' in text.lower())


print(str(python_jobs))

file = open("./registro.html", "w")

for p_job in python_jobs:
    title_elem = p_job.find('h2', class_='title')
    company_elem = p_job.find('div', class_='company')
    location_elem = p_job.find('div', class_='location')
    link = p_job.find('a')['href']
    
    #--------------- if None in (title_elem, company_elem, location_elem, link):
        #-------------------------------------------------------------- continue
    
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
    
    file.write(str(title_elem.text).strip('\n'))
    file.write(str(company_elem.text).strip('\n'))
    file.write(str(location_elem.text).strip('\n'))
    file.write(f"Usa este link: {link}\n")

# for job_elem in job_elems: ---------------------------------------------------
    # # Each job_elem is a new BeautifulSoup object. ---------------------------
    # # You can use the same methods on it as you did before. ------------------
    # title_elem = job_elem.find('h2', class_='title') -------------------------
    # company_elem = job_elem.find('div', class_='company') --------------------
    # location_elem = job_elem.find('div', class_='location') ------------------
#  -----------------------------------------------------------------------------
    # if None in (title_elem, company_elem, location_elem): --------------------
        # continue -------------------------------------------------------------
#  -----------------------------------------------------------------------------
    # # print(title_elem.text) --------------------------------------------------- 
    # # print(company_elem.text) ------------------------------------------------- 
    # # print(location_elem.text) ------------------------------------------------ 
#  -----------------------------------------------------------------------------
    # file.write(str(title_elem.text).strip('\n')) -----------------------------
    # file.write(str(company_elem.text).strip('\n')) ---------------------------
    # file.write(str(location_elem.text).strip('\n')) --------------------------
    
file.close()

#print(job_elem.prettify())