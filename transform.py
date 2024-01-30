import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

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
            cleaned_string = unidecode(string)
            if count == 1:
                text['autor'] = cleaned_string
            elif count > 3:
                text['content'] =text['content']+ cleaned_string +'/n'
            count+=1
        texts_in_jason.append(text)
    return texts_in_jason