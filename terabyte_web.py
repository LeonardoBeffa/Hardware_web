from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import time
import os
from bs4 import BeautifulSoup 

os.system('cls')

def terabyte_web(dic_produtos):
    url_page = f'https://www.terabyteshop.com.br/perifericos/teclado'
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
                titulo = item.find('a', class_=re.compile('prod-name')).get_text().strip()
                preco_a_vista = item.find('div', class_=re.compile('prod-new-price')).get_text().strip('  à vista')
                link = item.find('a', class_=re.compile('prod-name')).get('href')

                if ',' in preco_a_vista:
                    dic_produtos['marca'].append(titulo)
                    dic_produtos['preco'].append(preco_a_vista)
                    dic_produtos['loja'].append('Terabyte')
                    dic_produtos['link'].append(link)

                    print(f'Título: {titulo}, Preço: {preco_a_vista}, Link: {link}')
            except AttributeError:
                continue

    except Exception as e:
        print(f'Erro ao carregar a página com Selenium: {e}')

    driver.quit()
    print(url_page)
    return dic_produtos

