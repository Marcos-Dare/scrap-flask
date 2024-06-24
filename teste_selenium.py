from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from BancoDeDados import MeuBanco

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

driver.get("https://br.advfn.com/jornal/2024/06/carteira-recomendada-semanal-com-ranking-carteiras-de-03-a-07-de-junho-de-2024")
time.sleep(2)
time.sleep(1)
html = driver.page_source
soup=BeautifulSoup(html,'html.parser')
data1 = soup.select_one("#afnmainbodidContainer > div.m.header-default-size > div.main-wrap > div.main.wrap.cf > div > div > article > header > div.post-meta.cf > span.posted-on > time").get_text()
div = soup.select_one("#afnmainbodidContainer > div.m.header-default-size > div.main-wrap > div.main.wrap.cf > div > div > article > div > div:nth-child(5) > table:nth-child(6)")
time.sleep(2)
table=pd.read_html(str(div))
dados1 = pd.DataFrame(table[0])
data1 = parse_date(str(data1))

time.sleep(1)
driver.get("https://www.moneytimes.com.br/tag/carteira-recomendada/")
try:
    pop_up = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#onesignal-slidedown-dialog")))
    botao_fechar = driver.find_element(By.CSS_SELECTOR, "#onesignal-slidedown-cancel-button")
    botao_fechar.click()
except:
    pass
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[8]/main/div/div[1]/div/h2/a").click()
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
data2 = soup.select_one("body > article > div.single_meta > div.single_meta_author > div.single_meta_author_infos > div.single_meta_author_infos_date > span.single_meta_author_infos_date_time").get_text()
div = soup.select_one("body > article > div.single_block > div.single_block_news > div.single_block_news_text")
table = pd.read_html(str(div))
dados2 = pd.DataFrame(table[0])
data2 = str(data2.replace("\t",""))[1:12]
data2 = parse_date(data2)

time.sleep(1)
driver.get("https://www.infomoney.com.br/cotacoes/b3/acao/")
time.sleep(3)
html = driver.page_source
soup=BeautifulSoup(html,'html.parser')
data3 = soup.select_one("body > div.layout-container.grid.grid--aside > article > div.ds-table > div.ds-table-header > span").get_text()
div = soup.select_one("body > div.layout-container.grid.grid--aside > article > div.ds-table")
time.sleep(1)
table=pd.read_html(str(div))
dados = table[4]
time.sleep(1)
dados3 = pd.DataFrame(dados)
data3 = str(data3)[0:6] + " 2024"
data3 = parse_date(data3)

driver.get("https://infograficos.valor.globo.com/carteira-valor/")
time.sleep(2)
html = driver.page_source
soup=BeautifulSoup(html,'html.parser')
data4 = soup.select_one("body > article > div.bx-container.indicadas > div > p.descricao > span:nth-child(3)").get_text()
div = soup.select_one("body > article > div.bx-container.indicadas > div")
time.sleep(2)
table=pd.read_html(str(div))
dados4 = pd.DataFrame(table[0])
data4 = str(data4) + "/2024"
data4 = parse_date(data4)

driver.get("https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm")
driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/main/div[4]/div/div[1]/div[1]/div/form/section/div/div/div/iframe"))
time.sleep(2)
html = driver.page_source
soup=BeautifulSoup(html,'html.parser')
data5 = soup.select_one("#divContainerIframeB3 > div > div.col-lg-9.col-12.order-2.order-lg-1 > form > h2").get_text()
div = soup.select_one("#divContainerIframeB3 > div > div.col-lg-9.col-12.order-2.order-lg-1 > form > div:nth-child(4) > div > table")
time.sleep(2)
table=pd.read_html(str(div))
dados5 = pd.DataFrame(table[0])
data5 = str(data5)[-8:-3] + "/2024"
data5 = parse_date(data5)


def mandar_salvar(lista,data,cod):
    dicionario = {}
    for dado in lista:
        for item in dado:
            dicionario[item] = data
    obj.salvar(dicionario,cod)

lista = []
dados1 = list(dados1[0])
novaLista = []
for dado in dados1:
    dados = dado[-6:-1]
    novaLista.append(dados)
novaLista.remove('presa')
lista.append(novaLista)
mandar_salvar(lista,data1,1)
lista = []

try:
    lista.append(list(dados2.Ticker))
except:
    lista.append(list(dados2[1][1::]))
mandar_salvar(lista,data2,2)
lista = []

dados3 = list(dados3.Nome)
lista2 = []
for acao in dados3:
    lista2.append(acao[0:5])
lista.append(lista2)
mandar_salvar(lista,data3,3)
lista = []

lista_de_manipulacao = list(dados4["NomeNome/Código"])
lista2 = []
for item in lista_de_manipulacao:
    lista2.append(item[-5:])
lista2.pop(-1)
lista.append(lista2)
mandar_salvar(lista,data4,4)
lista = []

lista_de_manipulacao = list(dados5.Código)
lista_de_manipulacao.pop(-1)
lista_de_manipulacao.pop(-1)
lista.append(lista_de_manipulacao)
mandar_salvar(lista,data5,5)

driver.quit()


