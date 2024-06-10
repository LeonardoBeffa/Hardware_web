from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import os
import time
import re

os.system('cls')

def amazon_page():    
    url_page = f'https://www.amazon.com.br/s?k=placa+de+video&i=computers&rh=n%3A16339926011%2Cp_n_feature_twelve_browse-bin%3A58373571011%2Cp_6%3AA1ZZFT5FULY4LN&dc&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1717808342&rnid=15137643011&ref=sr_pg_1'
    browser_options = Options()
    browser_options.add_argument('--headless')
    driver = webdriver.Firefox(options=browser_options)
    driver.get(url_page)
    time.sleep(2)
    page_source = driver.page_source
    driver.quit()
    return page_source

def amazon_web(dic_produtos):
    for i in range(0,1):
        site_content = amazon_page()
        soup = BeautifulSoup(site_content, 'html.parser')
        produtos = soup.find_all('div', class_=re.compile('sg-col-4-of-20'))
        time.sleep(1)
        idx = 0
        for produto in produtos:
            try:
                nome = produto.find('span', class_=re.compile('a-text-normal')).get_text().strip()
            except:
                nome = None
            
            try:
                if nome == None:
                    preco = None
                else:
                    preco = produto.find('span', class_=re.compile('a-offscreen')).get_text().strip()
            except:
                preco = None

            try:
                link = produto.find('a', class_=re.compile('a-link-normal')).get('href')
                link_tratado = 'https://www.amazon.com.br/' + link
            except:
                link = None

            if preco == None:
                nome = None
            else:
                idx += 1
                dic_produtos['marca'].append(nome)
                dic_produtos['preco'].append(preco)
                dic_produtos['loja'].append('Amazon')
                dic_produtos['link'].append(link_tratado)
                print(f'idx {idx} nome: {nome} valor: {preco}')
    return dic_produtos
