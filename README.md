# Coleta de Dados de Teclados Gamer

Este repositório contém scripts para coletar informações sobre teclados gamer de diferentes sites de e-commerce. Os scripts utilizam técnicas de web scraping para extrair dados como nome, preço, loja e link dos produtos e armazenam os resultados em um arquivo CSV.

## Descrição Geral

Os scripts incluídos neste repositório fazem scraping dos seguintes sites:
- **Amazon**
- **Pichau**
- **Terabyte**
- **Kabum**

Cada script é projetado para acessar e coletar dados das páginas de resultados desses sites, lidando com a navegação e a extração de informações sobre teclados gamer. A coleta de dados é realizada com base na renderização das páginas e na análise do HTML.

### Funcionalidade

1. **Coleta de Dados**:
   - Os scripts acessam as páginas de resultados de teclados gamer em cada site e extraem informações como:
     - **Nome do Produto**: O título do teclado.
     - **Preço**: O preço do teclado, quando disponível.
     - **Link do Produto**: A URL do produto para mais detalhes.
     - **Loja**: O nome do site onde o produto foi encontrado.

2. **Armazenamento de Dados**:
   - Os dados extraídos são armazenados em um arquivo CSV, com as seguintes colunas:
     - `marca` (Nome do Produto)
     - `preco` (Preço)
     - `loja` (Nome do Site)
     - `link` (Link para o Produto)

3. **Dependências**:
   - `pandas`: Para manipulação e armazenamento dos dados em formato CSV.
   - `selenium`: Para automação da navegação e interação com as páginas web.
   - `beautifulsoup4`: Para análise e extração de dados do HTML.
   - `requests`: Para obter o conteúdo HTML das páginas (especificamente para o Kabum).
   - `termcolor`: Para formatação de saída no terminal.

4. **Navegação e Extração**:
   - **Amazon**: Utiliza o Selenium para acessar a página e o BeautifulSoup para extrair os dados dos produtos listados.
   - **Pichau**: Usa o Selenium para navegar por múltiplas páginas e extrair dados dos produtos.
   - **Terabyte**: Combina Selenium e BeautifulSoup para coletar informações de teclados na página da Terabyte.
   - **Kabum**: Usa Requests para obter o HTML da página e Selenium para extrair dados dos produtos listados em várias páginas.
