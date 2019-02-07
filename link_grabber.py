def read_links(file):
    with open(file, 'r') as f:
        contents = f.read()

    return contents.splitlines()

def remove_tags(element):
    remove_open = element.replace('<link>', '')
    remove_close = remove_open.replace('</link>', '')
    clean_link = remove_close.replace(' ', '')

    return clean_link

def grab_links(data):
    links = []

    for line in data:
        if line.find('<link>') > 0:
            url = remove_tags(line)
            links.append(url)
    
    links.pop(0)
    print(links)
    return links

def main():
    data = read_links('output.xml')
    links = grab_links(data)
    #print(data)

    with open('links.txt', 'w') as f:
        for link in links:
            f.write('%s \n' % link)

if __name__ == '__main__':
    main()