from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import time
import os
from bs4 import BeautifulSoup 

os.system('cls')

def terabyte_web(dic_produtos):
    url_page = f'https://www.terabyteshop.com.br/hardware/placas-de-video'
    browser_options = Options()
    browser_options.add_argument('--headless')
    driver = webdriver.Firefox(options=browser_options)

    try:
        driver.get(url_page)
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        for item in soup.find_all('div', class_='pbox'):
            try:
                nome = item.find('a', class_=re.compile('prod-name')).get_text().strip()
                valor = item.find('div', class_=re.compile('prod-new-price')).get_text().strip('  à vista')
                link = item.find('a', class_=re.compile('prod-name')).get('href')

                if ',' in valor:
                    dic_produtos['Nome'].append(nome)
                    dic_produtos['Valor'].append(valor)
                    dic_produtos['Loja'].append('Terabyte')
                    dic_produtos['Link'].append(link)
                    print(f'Nome: {nome} Valor: {valor}')
            except AttributeError:
                continue

    except Exception as e:
        print(f'Erro ao carregar a página com Selenium: {e}')

    driver.quit()
    print(url_page)
    return dic_produtos

