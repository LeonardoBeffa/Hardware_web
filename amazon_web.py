from bs4 import BeautifulSoup
import requests
import re
import time

def amazon_web(dic_produtos,headers):
    itens_not = 0
    for i in range(0,1):

        url_page = f'https://www.amazon.com.br/s?k=placa+de+video&page={i}&crid=2NF2JBIWKESI6&qid=1717527616&sprefix=placa+d%2Caps%2C241&ref=sr_pg_{i}'
        site = requests.get(url_page, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        produtos = soup.find_all('div', class_=re.compile('sg-col-4-of-20'))
        time.sleep(1)

        if site.status_code != 200:
            print("Erro Amazon.")
            break
        
        else:
            for produto in produtos:   
                
                try:
                    marca = produto.find('span', class_=re.compile('a-text-normal')).get_text().strip()
                    if 'F' in marca or 'KF' in marca or 'K' in marca or 'Desbloqueado' in marca:
                        marca_tratada = marca
                    else:
                        marca = 'None'
                except:
                    marca = 'None'
                
                try:
                    if marca == 'None':
                        preco = 0
                    else:
                        preco = produto.find('span', class_=re.compile('a-offscreen')).get_text().strip()
                except:
                    preco = 0

                try:
                    link = produto.find('a', class_=re.compile('a-link-normal')).get('href')
                    link_tratado = 'https://www.amazon.com.br/' + link
                except:
                    link = 'None'

                if preco == 0:
                    marca = 'None'
                    itens_not = itens_not + 1
                else:
                    print(marca, preco)
                    
                    dic_produtos['marca'].append(marca_tratada)
                    dic_produtos['preco'].append(preco)
                    dic_produtos['loja'].append('Amazon')
                    dic_produtos['link'].append(link_tratado)

            print(url_page)
    
    return dic_produtos
            