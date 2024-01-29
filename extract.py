from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from urls.urls import infinitscroll

# Inicializa o WebDriver do Chrome
def extract_links():
    driver = webdriver.Chrome()

    # Abre a página desejada
    driver.get(infinitscroll)

    # Define um tempo de espera entre as rolagens
    SCROLL_PAUSE_TIME = 2

    # Obter a altura inicial da página
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Rola até o final da página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Aguarda o carregamento da página
        time.sleep(SCROLL_PAUSE_TIME)

        # Calcula a nova altura da página e compara com a última altura da página
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Aqui você pode adicionar o código para extrair os dados necessários da página
    elems = driver.find_elements(By.XPATH,'//a[@class="gh-card-link"]')
    cont = 0
    links = [] 
    for elem in elems:
        links.append(elem.get_attribute("href"))

    # Fecha o navegador quando terminar
    arq = open('Dados/links.txt','w')
    for link in links:
        arq.write('\n'+link)
    driver.quit()


def prepare_links():
    arq = open('Dados\links.txt')
    links = []
    for line in arq.readlines():
        line = line.replace('\n','')
        links.append(line)
    links.pop(0)
    return links


