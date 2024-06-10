from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import math
import os
import time

os.system('cls')

url_pag = f'https://www.pichau.com.br/hardware/placa-de-video'
browser_options = Options()
browser_options.add_argument('--headless')
driver = webdriver.Firefox(options=browser_options) 
driver.get(url_pag)
time.sleep(2)

def pichau_ultima_pag():
    results_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[1]/div/div/div[1]/div').text
    qtd = results_xpath
    ultima_pagina = math.ceil(int(qtd)/ 36)
    return ultima_pagina

def pichau_web(dic_produtos):
    end = 0
    for num in range(1,pichau_ultima_pag()):
        if num == 1:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            for i in range(1, 37):
                prod_finds = driver.find_elements(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]')
                for prod in prod_finds:
                    nome = prod.find_element(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/h2').text
                    valor = prod.find_element(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/div/div[1]/div/div[2]').text
                    link = prod.find_element(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a').get_attribute('href')
                    dic_produtos['Nome'].append(nome)
                    dic_produtos['Valor'].append(valor)
                    dic_produtos['Loja'].append('Pichau')
                    dic_produtos['Link'].append(link)
                    print(f'nome: {nome} valor: {valor} link: {link} Pag: 1')
            driver.quit()
        else:
            browser_options = Options()
            browser_options.add_argument('--headless')
            driver1 = webdriver.Firefox(options=browser_options)
            driver1.get(f'https://www.pichau.com.br/hardware/placa-de-video?page={num}')
            time.sleep(3)
            driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            for i in range(1, 37):
                prod_finds = driver1.find_elements(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]')
                for prod in prod_finds:
                    nome = prod.find_element(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/h2').text
                    try:
                        valor = prod.find_element(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/div/div[1]/div/div[2]').text
                    except:
                        valor = None
                    link = prod.find_element(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a').get_attribute('href')
                    if valor == None:
                        end = 1
                        break
                    else:
                        dic_produtos['Nome'].append(nome)
                        dic_produtos['Valor'].append(valor)
                        dic_produtos['Loja'].append('Pichau')
                        dic_produtos['Link'].append(link)
                        print(f'Nome: {nome} Valor: {valor}')
            driver1.quit()
            if end == 1:
                break
            else:
                continue
        if end == 1:
            break
        else:
            continue
    return dic_produtos