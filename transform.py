import requests
from bs4 import BeautifulSoup


def _get_html(link):
    while True:
        try:
            response = requests.get(link)
            return response
        except ConnectionError:
            pass
            
def create_objects(links):
    texts_in_jason = []
    for link in links:
        response = _get_html(link)
        soup = BeautifulSoup(response.text)
        tag = soup.section
        count = 0
        text = {'autor':0,
            'content': ''}
        for string in tag.stripped_strings:
            if count == 1:
                text['autor'] = string
            elif count > 3:
                text['content'] =text['content']+ string +'/n'
            count+=1
        texts_in_jason.append(text)
    return texts_in_jason