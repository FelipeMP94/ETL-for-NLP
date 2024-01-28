import requests
from bs4 import BeautifulSoup

def prepare_links():
    arq = open('Dados\links.txt')
    links = []
    for line in arq.readlines():
        line = line.replace('\n','')
        links.append(line)
    links.pop(0)
    return links

links = prepare_links()

response = requests.get(links[0])

soup = BeautifulSoup(response.text)

tag = soup.section

print(type(tag))