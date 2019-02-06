import JobsRSSWriter
import bs4 as bs
from urllib.parse import urljoin

def get_page_data(dom):
    with open(dom, 'r', encoding="utf8") as f:
        dom_output = f.read()

    soup = bs.BeautifulSoup(dom_output, 'lxml')

    return soup

def search_jobs(soup):
    jobs_list = []

    for job in jobs(soup):
        jobs_list.append(job)

    return jobs_list

def jobs(soup):
    jobs_table_soup = soup.find('tbody')
    jobs_soup = jobs_table_soup.find_all('tr')

    for job in jobs_soup:
        job_title = job.find('td', {'class': 'job-table-title'}).find('a').text
        job_type = job.find('td', {'class': 'job-table-type'}).text
        job_number = job.find('td', {'class': 'job-table-jobnumber'}).text

        title = job_title + ' - ' + job_type + ' - ' + job_number
        link = urljoin('https://www.governmentjobs.com/', job.find('a').get('href'))
        
        yield link, title

def main():
    dom = "C:/jobsinthedesert_tools/parsers/neogov-rss/output/dom.html"
    data = get_page_data(dom)
    jobs = search_jobs(data)

    jobs_xml = JobsRSSWriter.format_rss(jobs, 'Sunline', 'https://jobsinthedesert.com/')

    with open('output.xml', 'w+') as f:
        f.write(jobs_xml)

if __name__ == '__main__':
    main()
