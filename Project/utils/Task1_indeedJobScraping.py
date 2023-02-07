import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

def extract_job_title_from_result(soup): 
  jobs = []
  for div in soup.find_all(name="div", attrs={"class":"row"}):
      for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
        jobs.append(a["title"])
  return(jobs)

def extract_company_from_result(soup): 
  companies = []
  for div in soup.find_all(name="div", attrs={"class":"row"}):
    company = div.find_all(name="span", attrs={"class":"company"})
    if len(company) > 0:
      for b in company:
        companies.append(b.text.strip())
    else:
      sec_try = div.find_all(name="span", attrs={"class":"result-link-source"})
      for span in sec_try:
        companies.append(span.text.strip())
  return(companies)

def extract_location_from_result(soup): 
  locations = []
  spans = soup.findAll('span', attrs={'class': 'location'})
  for span in spans:
    locations.append(span.text)
  return(locations)

def extract_salary_from_result(soup): 
  salaries = []
  for div in soup.find_all(name="div", attrs={"class":"row"}):
    try:
      salaries.append(div.find('nobr').text)
    except:
      try:
        div_two = div.find(name="div", attrs={"class":"sjcl"})
        div_three = div_two.find("div")
        salaries.append(div_three.text.strip())
      except:
        salaries.append("Nothing_found")
  return(salaries)

def extract_jobdesc(soup): 
  jobdesc = []
  #spans = soup.findAll('span', attrs={'class': 'summary'})
  for item in soup.findAll('div',{'class':'summary'}):
    sub_items = item.findAll('li')
    for sub_item in sub_items:
        #print(sub_item.text)
        jobdesc.append(sub_item.text)
  return(jobdesc)

# max_results_per_city = 100
# city_set = ['New+York','Chicago','San+Francisco', 'Austin', 'Seattle', 'Los+Angeles', 'Philadelphia', 'Atlanta', 'Dallas', 'Pittsburgh', 'Portland', 'Phoenix', 'Denver', 'Houston', 'Miami', 'Washington+DC', 'Boulder']
# #columns = ["city", "job_title", "company_name", "location", "summary", "salary"]


def fetch_jobs(q):
  job_post = []
  q = q.replace(" ", "+").lower()
  url = "https://in.indeed.com/jobs?q="+q+"&l="
  page = requests.get(url)
  time.sleep(1)  #ensuring at least 1 second between page grabs
  #soup = BeautifulSoup(page.text, "lxml", from_encoding="utf-8")
  soup = BeautifulSoup(page.text, "html.parser", from_encoding="utf-8")
  job_title = extract_job_title_from_result(soup)
  #job_post.append(city)
  job_post.append('')
  job_post.append(job_title)
  job_company = extract_company_from_result(soup)
  job_post.append(job_company)
  job_location = extract_location_from_result(soup)
  job_post.append(job_location)
  job_salary = extract_salary_from_result(soup)
  job_post.append(job_salary)
  job_descr = extract_jobdesc(soup)
  job_post.append(job_descr)
    #saving sample_df as a local csv file — define your own local path to save contents 
    #print(sample_df)
  #sample_df = sample_df.append(job_post)
  columns = ["job_title", "company_name", "location", "summary", "salary"]
  sample_df = pd.DataFrame(columns = columns)
  print(len(job_title), len(job_company), len(job_location))
  sample_df['job_title'] = job_title
  sample_df['company_name'] = job_company
  # sample_df['location'] = job_location
  sample_df['summary'] = pd.Series(job_descr)
  sample_df['salary'] = job_salary

  print("*******************************************************")
  return sample_df.to_json(orient="records")

# fetch_jobs("data scientist")