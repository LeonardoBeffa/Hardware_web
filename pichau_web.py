from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import os

os.system('cls')

url_pag = 'https://www.pichau.com.br/perifericos/teclado'
browser_options = Options()
browser_options.add_argument('--headless')
driver = webdriver.Firefox(options=browser_options) 
driver.get(url_pag)

def pichau_ultima_pag():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[1]/div/div/div[1]/div')))
    results_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[1]/div/div/div[1]/div').text
    qtd = results_xpath
    ultima_pagina = math.ceil(int(qtd)/ 36)
    return ultima_pagina

def pichau_web(dic_produtos):
    end = 0
    for num in range(1, pichau_ultima_pag() + 1):
        if num == 1:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[1]')))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[36]')))
            for i in range(1, 37):
                prod_finds = driver.find_elements(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]')
                for prod in prod_finds:
                    nome = prod.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/h2').text
                    try:
                        preco = prod.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/div/div[1]/div/div[2]').text
                    except:
                        preco = 'Não encontrado'
                    link = prod.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a').get_attribute('href')
                    dic_produtos['marca'].append(nome)
                    dic_produtos['preco'].append(preco)
                    dic_produtos['loja'].append('Pichau')
                    dic_produtos['link'].append(link)
                    print(f'nome: {nome} valor: {preco} link: {link} Pag: 1')
            driver.quit()
        else:
            browser_options = Options()
            browser_options.add_argument('--headless')
            driver1 = webdriver.Firefox(options=browser_options)
            driver1.get(f'https://www.pichau.com.br/perifericos/teclado?page={num}')
            WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[1]')))
            driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[36]')))
            for i in range(1, 37):
                prod_finds = driver1.find_elements(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]')
                for prod in prod_finds:
                    nome = prod.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/h2').text
                    try:
                        preco = prod.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a/div/div[3]/div/div[1]/div/div[2]').text
                    except:
                        preco = None
                    link = prod.find_element(By.XPATH, f'/html/body/div[1]/div[1]/main/div[2]/div/div[1]/div[3]/div[{i}]/a').get_attribute('href')
                    if preco is None:
                        end = 1
                        break
                    else:
                        dic_produtos['marca'].append(nome)
                        dic_produtos['preco'].append(preco)
                        dic_produtos['loja'].append('Pichau')
                        dic_produtos['link'].append(link)
                        print(f'nome: {nome} valor: {preco} link: {link} Pag: {num}')
            driver1.quit()
            if end == 1:
                break
    return dic_produtos