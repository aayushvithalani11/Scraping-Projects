from bs4 import BeautifulSoup
import requests

url = "https://www.freshersworld.com/jobs/jobsearch/python-jobs"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
#print(soup.prettify())

jobs = soup.find_all('div', class_="listing-block")
for job in jobs:
    job_title = job.find('span', class_="wrap-title seo_title").text
    education_required = job.find('span', class_="qualifications display-block modal-open pull-left job-details-span").text
    date_posted = job.find('span', class_="desc").text

    print(job_title)
    print(education_required)
    print(date_posted)