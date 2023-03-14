import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(filename='wiki_search.log', level=logging.INFO)

path = [str() for i in range(4)]
logging.basicConfig(filename='wiki_search.log', level=logging.INFO)

def p_links(ls_links):
    new_links = []
    for i in ls_links:
        for n in i:
            new_links.append(n)
    return new_links


def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    p_tags = soup.find_all('p')
    links = [p_tag.find_all('a', href=True) for p_tag in p_tags]
    links = p_links(links)
    urls = [link['href'] for link in links if link['href'].startswith('/wiki/') and ':' not in link['href']]
    urls = list(set(urls))
    urls = ['https://ru.wikipedia.org{}'.format(url) for url in urls]
    return urls


def create_graph(html1, url2):
    graph = {}
    links1 = get_links(html1)                           # https://ru.wikipedia.org/wiki/Electronic_Entertainment_Expo
    for link1 in links1:
        html_page1 = requests.get(link1).text           # https://ru.wikipedia.org/wiki/Virtual_Boy
        links2 = get_links(html_page1)
        logging.info(f"Visiting {link1}")
        for link2 in links2:
            html_page2 = requests.get(link2).text       # https://ru.wikipedia.org/wiki/Nintendo_3DS
            links3 = get_links(html_page2)
            logging.info(f"Visiting {link2}")
            if str(url2) in links3:
                path[1], path[2] = link1, link2
                return path


def new_data(new_path):
    data_new = {1: [], 2: [], 3: []}
    if new_path:
        for i in range(len(new_path) - 1):
            current_url = new_path[i]
            next_url = new_path[i + 1].replace("https://ru.wikipedia.org", "")
            html = requests.get(current_url).text
            soup = BeautifulSoup(html, 'html.parser')
            p_tags = soup.find_all('p')
            for p_tag in p_tags:
                a_tags = p_tag.find_all('a', href=True)
                d = []
                for a_tag in a_tags:
                    href = a_tag['href']
                    d.append(href)
                if next_url in d:
                    data_new[i+1].append(p_tag.text.strip())
                    data_new[i + 1].append(str("https://ru.wikipedia.org")+str(next_url))
                    break
        return data_new


def main(url1, url2):

    path[0], path[-1] = url1, url2
    html1 = requests.get(url1).text

    new_path = create_graph(html1, url2)

    return new_data(new_path)

