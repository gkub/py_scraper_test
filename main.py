from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
        
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # f = open("test_file.txt", "w")
    
    for index, job in enumerate(jobs):
        
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if ('1 day' in published_date) or ('today' in published_date):  
            with open(f'posts/{index}.txt', 'w') as f:
                comp_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').replace('(MoreJobs)', '').strip()
                skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').strip()
                more_info = job.header.h2.a['href']
                test = f'''Company name: {comp_name}\nRequired Skills: {skills}\nMore Info: {more_info}\n\n'''
                #print(test)
                f.write(test)
            print(f'File saved: {index}')
            # print()

            # print('')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes!')
        time.sleep(time_wait * 60)