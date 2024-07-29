import pandas as pd
import os
from termcolor import colored
from terabyte_web import terabyte_web
from amazon_web import amazon_web
from kabum_web import kabum_web
from pichau_web import pichau_web

os.system('cls')
nome_arquivo = 'teclado_gamer_TEST'
diretorio = 'C:/Users/Leonardo/Documents/Python/webScraping/Hardware'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
dic_produtos = {'marca':[], 'preco':[],'loja':[],'link':[]}

print(colored("Iniciando o programa...","green"))
print(colored("Amazon", "red", attrs=["bold"]))
amazon_web(dic_produtos)
print(colored("Pichau", "red", attrs=["bold"]))
try:
    pichau_web(dic_produtos)
except:
    pass
print(colored("Terabyte", "red", attrs=["bold"]))
terabyte_web(dic_produtos)
print(colored("Kabum", "red", attrs=["bold"]))
kabum_web(dic_produtos, headers)
print(colored("Fim do programa!","green"))

df = pd.DataFrame(dic_produtos)
df.to_csv(f'{diretorio}/{nome_arquivo}.csv', encoding='utf-8', sep=';', index=False)