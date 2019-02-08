import os
import datetime
import argparse

def read_links(file):
    with open(file, 'r') as f:
        contents = f.read()

    return contents.splitlines()

def remove_link_tags(element):
    remove_open = element.replace('<link>', '')
    remove_close = remove_open.replace('</link>', '')
    clean_link = remove_close.replace(' ', '')

    return clean_link

def remove_title_tags(element):
    remove_open = element.replace('<title>', '')
    remove_close = remove_open.replace('</title>', '')
    remove_lead_spaces = remove_close.lstrip()
    remove_space = remove_lead_spaces.replace(' ', '_')
    pdf_title = remove_space + '_' + datetime.date.today().isoformat() + '.pdf'

    return pdf_title

def grab_links(data):
    links = []

    for line in data:
        if line.find('<link>') > 0:
            url = remove_link_tags(line)
            links.append(url)
    
    links.pop(0)
    #print(links)
    return links

def grab_titles(data):
    titles = []

    for line in data:
        if line.find('<title>') > 0:
            title = remove_title_tags(line)
            titles.append(title)

    titles.pop(0)
    #print(titles)
    return titles

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-output_directory', required = True,
        help="path to store output")
    parser.add_argument('-feed_location', required = True,
        help="location of xml file")

    args = parser.parse_args()

    data = read_links(args.feed_location)
    links = grab_links(data)
    titles = grab_titles(data)
    #print(data)

    with open(os.path.join(args.output_directory, 'links.txt'), 'w') as f:
        for link in links:
            f.write('%s\n' % link)

    with open(os.path.join(args.output_directory, 'pdf_titles.txt'), 'w') as f:
        for title in titles:
            f.write('%s\n' % title)

if __name__ == '__main__':
    main()

'''
Project Manager Assistant - Full-time - 1800054

Project_Manager_Assistant_-_Full-time_-_1800054
'''