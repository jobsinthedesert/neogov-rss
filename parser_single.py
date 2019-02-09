import logging
import argparse
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

    if (soup.find('tbody')):
        jobs_table_soup = soup.find('tbody')
        jobs_soup = jobs_table_soup.find_all('tr')

        for job in jobs_soup:
            job_title = job.find('td', {'class': 'job-table-title'}).find('a').text
            job_type = job.find('td', {'class': 'job-table-type'}).text

            if (job.find('td', {'class': 'job-table-jobnumber'})):
                job_number = job.find('td', {'class': 'job-table-jobnumber'}).text
            else:
                job_number = ''

            if (job_number == ''):
                title = job_title + ' - ' + job_type
            else:
                title = job_title + ' - ' + job_type + ' - ' + job_number

            link = urljoin('https://www.governmentjobs.com/', job.find('a').get('href'))
            logging.info(link + ',' + title)
            yield link, title
    else:
        print('no jobs found')

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-dom', required = True,
        help="path to dom.html")
    parser.add_argument('-output', required = True,
        help="name of RSS file (ex: feed.xml)")
    parser.add_argument('-title', required = True,
        help="name in RSS feed <title> tag")
    parser.add_argument('-link', required = True,
        help="url in RSS feed <link> tag")
    parser.add_argument('-log', required = True,
        help="location of .log")
    
    args = parser.parse_args()

    logging.basicConfig(filename=args.log, level=logging.INFO,
        format='%(asctime)s - %(message)s')

    dom = args.dom
    data = get_page_data(dom)
    jobs = search_jobs(data)

    jobs_xml = JobsRSSWriter.format_rss(jobs, args.title, args.link)

    with open(args.output, 'w+') as f:
        f.write(jobs_xml)

if __name__ == '__main__':
    main()

