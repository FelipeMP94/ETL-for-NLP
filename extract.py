from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from urls.urls import infinitscroll



class Extractor:
    def __init__(self,):
        self.path_principal = infinitscroll
        self.driver = webdriver.Chrome()
        self.SCROLL_PAUSE_TIME = 2


    def extract_links_class(self):
        self.driver.get(self.path_principal)

        last_height = self.driver.execute_script("return document.body.scrollHeight")
        count = 0 
        while True:
            # Rola até o final da página
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Aguarda o carregamento da página
            time.sleep(self.SCROLL_PAUSE_TIME)

            # Calcula a nova altura da página e compara com a última altura da página
            new_height = self.driver.execute_script("return document.body.scrollHeight")
        
            if (new_height == last_height):
                count+=1
                if count ==3:
                    break
            else:
                count = 0

            last_height = new_height
         # Aqui você pode adicionar o código para extrair os dados necessários da página
        elems = self.driver.find_elements(By.XPATH,'//a[@class="gh-card-link"]')
        links = [] 
        for elem in elems:
            links.append(elem.get_attribute("href"))

        # Fecha o navegador quando terminar
        arq = open('Dados/linksTest.txt','w')
        for link in links:
            arq.write('\n'+link)
        self.driver.quit()

    def prepare_links(self):
        arq = open('Dados\linksTest.txt')
        links = []
        for line in arq.readlines():
            line = line.replace('\n','')
            links.append(line)
        links.pop(0)
        return links

#

