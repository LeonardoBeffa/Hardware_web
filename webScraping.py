import pandas as pd
import os
from terabyte_web import terabyte_web
from amazon_web import amazon_web
from kabum_web import kabum_web
from pichau_web import pichau_web

os.system('cls')
nome_arquivo = 'preco_placa_de_video'
diretorio = 'SEU DIRETORIO DE SALVAMENTO'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
dic_produtos = {'Nome':[], 'Valor':[],'Loja':[],'Link':[]}

print("Iniciando o programa...")
print("Amazon")
amazon_web(dic_produtos)
print("Pichau")
pichau_web(dic_produtos)
print("Terabyte")
terabyte_web(dic_produtos)
print("Kabum")
kabum_web(dic_produtos, headers)
print("Fim do programa!")

df = pd.DataFrame(dic_produtos)
df.to_csv(f'{diretorio}/{nome_arquivo}.csv', encoding='utf-8', sep=';', index=False)
