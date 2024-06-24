from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BancoDeDados import MeuBanco
import csv

# obj = MeuBanco()

# obj.abrir_conexao()

# driver = webdriver.Edge()

# i = 0
# while i < 3:
#     time.sleep(2)
#     driver.get("https://content.btgpactual.com/research/carteiras-recomendadas/carteira-recomendada/65e9abb3220d230ce4d3b262/Analise-Tecnica-Swing-Trade")
#     time.sleep(3)
#     html = driver.page_source
#     soup = BeautifulSoup(html,"html.parser")
#     div = soup.select_one("body > app-root > app-portfolios-home > app-portfolio-page > div > div.cell-9-desktop.cell-8-tablet.cell-4-phone.ng-tns-c273-6.ng-star-inserted")
#     time.sleep(3)
#     table = pd.read_html(str(div))
#     dados1 = pd.DataFrame(table[0])

#     time.sleep(1)
#     driver.get("https://www.moneytimes.com.br/tag/carteira-recomendada/")
#     try:
#         pop_up = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#onesignal-slidedown-dialog")))
#         botao_fechar = driver.find_element(By.CSS_SELECTOR, "#onesignal-slidedown-cancel-button")
#         botao_fechar.click()
#     except:
#         pass
#     time.sleep(1)
#     driver.find_element(By.XPATH,"/html/body/div[8]/main/div/div[1]/div/h2/a").click()
#     time.sleep(1)
#     html = driver.page_source
#     soup = BeautifulSoup(html,"html.parser")
#     div = soup.select_one("body > article > div.single_block > div.single_block_news > div.single_block_news_text")
#     table = pd.read_html(str(div))
#     dados2 = pd.DataFrame(table[0])

#     time.sleep(1)
#     driver.get("https://www.infomoney.com.br/cotacoes/b3/acao/")
#     time.sleep(3)
#     html = driver.page_source
#     soup=BeautifulSoup(html,'html.parser')
#     div = soup.select_one("body > div.layout-container.grid.grid--aside > article > div.ds-table")
#     time.sleep(1)
#     table=pd.read_html(str(div))
#     dados = table[4]
#     time.sleep(1)
#     dados3 = pd.DataFrame(dados)

#     driver.get("https://infograficos.valor.globo.com/carteira-valor/")
#     time.sleep(2)
#     html = driver.page_source
#     soup=BeautifulSoup(html,'html.parser')
#     div = soup.select_one("body > article > div.bx-container.indicadas > div")
#     time.sleep(2)
#     table=pd.read_html(str(div))
#     dados4 = pd.DataFrame(table[0])

#     driver.get("https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm")
#     driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/main/div[4]/div/div[1]/div[1]/div/form/section/div/div/div/iframe"))
#     time.sleep(2)
#     html = driver.page_source
#     soup=BeautifulSoup(html,'html.parser')
#     div = soup.select_one("#divContainerIframeB3 > div > div.col-lg-9.col-12.order-2.order-lg-1 > form > div:nth-child(4) > div > table")
#     time.sleep(2)
#     table=pd.read_html(str(div))
#     dados5 = pd.DataFrame(table[0])

#     lista = []
#     lista.append(list(dados1.Ticker))
#     lista.append(list(dados2.Ticker))
#     dados3 = list(dados3.Nome)

#     lista2 = []
#     for acao in dados3:
#         lista2.append(acao[0:5])
#     lista.append(lista2)

#     lista_de_manipulacao = list(dados4["NomeNome/Código"])
#     lista2 = []
#     for item in lista_de_manipulacao:
#         lista2.append(item[-5:])
#     lista2.pop(-1)
#     lista.append(lista2)

#     lista_de_manipulacao = list(dados5.Código)
#     lista_de_manipulacao.pop(-1)
#     lista_de_manipulacao.pop(-1)
#     lista.append(lista_de_manipulacao)

#     print(lista)

#     dicionario = {}

#     for sublista in lista:
#         for acao in sublista:
#             if isinstance(acao, list):
#                 acao = tuple(acao)
#             if acao in dicionario:
#                 dicionario[acao] += 1
#             else:
#                 dicionario[acao] = 1

#     dicionario2 = {}
#     for chave in sorted(dicionario, key=dicionario.get):
#         dicionario2[chave] = dicionario[chave]

#     obj.salvar(dicionario2)

#     i +=1
# with open("dados.csv", "w", newline="") as arquivo:
#     escritor_csv = csv.writer(arquivo)
#     for chave, valor in dicionario2.items():
#         escritor_csv.writerow([chave, valor])

# import sqlite3

# class MeuBanco:

#     def __init__(self):
#         pass

#     def abrir_conexao(self):
#         self.conn = sqlite3.connect("banco.db")
#         self.conn.execute("""
#             Create Table if not exists acoes(
#             Ticker Varchar(7) Primary Key not null,
#             Recomendacao integer not null
#             );
#         """)
#         self.cursor = self.conn.cursor()

#     def recuperar_dados(self):
#         self.cursor.execute("Select Tickers from acoes")
#         tickers = self.cursor.fetchall()
#         return tickers

#     def salvar(self,dicionario):
#         tickers = self.recuperar_dados()
#         for chave in dicionario.keys():
#             if (chave,) in tickers:
#                 self.cursor.execute("""
#                     update acoes set recomendacao = recomendacao + ?
#                                     where Ticker == ?
#                 """,(int(dicionario[chave]), chave))
#             else:
#                 self.cursor.execute("insert or ignore into acoes values(?,?)",(chave,int(dicionario[chave])))
#         self.conn.commit()
from datetime import datetime
def parse_date(date_str):
    formats = [
        "%Y-%m-%d",     # Exemplo: 2023-06-01
        "%d/%m/%Y",     # Exemplo: 01/06/2023
        "%m-%d-%Y",     # Exemplo: 06-01-2023
        "%d %b %Y",     # Exemplo: 01 Jun 2023
        "%b %d, %Y",    # Exemplo: Jun 01, 2023
    ]
    
    for fmt in formats:
        try:
            return str(datetime.strptime(date_str, fmt).date())
        except ValueError:
            continue
obj = MeuBanco()

obj.abrir_conexao()

driver = webdriver.Edge()

time.sleep(1)
driver.get("https://www.moneytimes.com.br/5-acoes-para-investir-na-primeira-semana-do-mes-segundo-a-mycap-jcav/")
try:
    pop_up = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#onesignal-slidedown-dialog")))
    botao_fechar = driver.find_element(By.CSS_SELECTOR, "#onesignal-slidedown-cancel-button")
    botao_fechar.click()
except:
    pass
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
data2 = soup.select_one("body > article > div.single_meta > div.single_meta_author > div.single_meta_author_infos > div.single_meta_author_infos_date > span.single_meta_author_infos_date_time").get_text()
div = soup.select_one("body > article > div.single_block > div.single_block_news > div.single_block_news_text")
table = pd.read_html(str(div))
dados2 = pd.DataFrame(table[0])
data2 = str(data2.replace("\t",""))[1:12]
data2 = parse_date(data2)

def mandar_salvar(lista,data,cod):
    dicionario = {}
    for dado in lista:
        for item in dado:
            dicionario[item] = data
    obj.salvar(dicionario,cod)

lista = []
try:
    lista.append(list(dados2.Ticker))
except:
    lista.append(list(dados2[1][1::]))
mandar_salvar(lista,data2,2)
lista = []




 

