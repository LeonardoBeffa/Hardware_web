from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
from bs4 import BeautifulSoup
import requests

def kabum_web(dic_produtos,headers):
    url = f'https://www.kabum.com.br/perifericos/teclado-gamer?page_number=1&page_size=100&facet_filters=&sort=most_searched'
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    qtd_itens = soup.find('div', id='listingCount').get_text().strip()

    index = qtd_itens.find(' ')
    qtd = qtd_itens[:index]

    ultima_pagina = math.ceil(int(qtd)/ 100)
    condicional_opc = ultima_pagina

    for i in range(1,condicional_opc):
        url_page = f'https://www.kabum.com.br/perifericos/teclado-gamer?page_number={i}&page_size=100&facet_filters=&sort=most_searched'
        browser_options = Options()
        browser_options.add_argument('--headless')
        driver = webdriver.Firefox(options=browser_options)
        driver.get(url_page)
        
        try:
            wait = WebDriverWait(driver, 10)

            # Inicia a extração das informações
            try:
                html = driver.find_elements(By.TAG_NAME, 'main')[0]
            except IndexError as ie:
                driver.refresh()
                continue

            html = html.get_attribute("innerHTML")

            sopa = BeautifulSoup(html, 'html5lib')

            num = 1

            for item in sopa.find_all('article', {'class': 'productCard'}):
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'priceCard')))
                
                titulo = item.find('span', class_='nameCard').text
                preco_a_vista = item.find('span', class_='priceCard').text
                link = driver.find_element(By.XPATH,f'//*[@id="listing"]/div[3]/div/div/div[2]/div[1]/main/article[{num}]/a').get_attribute('href')
                num = num+1 

                if ',' in preco_a_vista:
                    print(titulo, preco_a_vista) 
                    dic_produtos['marca'].append(titulo)
                    dic_produtos['preco'].append(preco_a_vista)
                    dic_produtos['loja'].append('Kabum')
                    dic_produtos['link'].append(link)                     
        
        except Exception as e:
            print("Exceção:", e)
            break
            
        driver.close()
        print(url_page)
    
    return dic_produtos