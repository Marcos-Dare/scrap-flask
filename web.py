from flask import Flask
from flask import render_template
from BancoDeDados import MeuBanco
from multiprocessing import Process
import schedule
import time
import datetime
import uuid
import rank
from collections import Counter

banco = MeuBanco()

app = Flask(__name__)
application = app

t = None
job_timer = None

def run_job(id):
    """ sample job with parameter """
    global job_timer
    job_timer = time.time()

def run_schedule():
    """ infinite loop for schedule """
    global job_timer
    job_timer = time.time()
    while 1:
        schedule.run_pending()
        rank.scrap()
        time.sleep(180)

@app.route('/timer/<string:status>')
def mytimer(status, nsec=10):
    global t, job_timer
    if status=='on' and not t:
        schedule.every(nsec).seconds.do(run_job, str(uuid.uuid4()))
        t = Process(target=run_schedule)
        t.start()
        return "timer on with interval:{}sec\n".format(nsec)
    elif status=='off' and t:
        if t:
            t.terminate()
            t = None
            schedule.clear()
        return "timer off\n"
    return "timer status not changed\n"

@app.route("/", methods=["GET"])
def home():
    return render_template(
        "home.html",
    )

@app.route("/dados", methods=["GET"])
def dados():
    banco.abrir_conexao()
    dado = banco.recuperar_dados()
    banco.fechar_conexao()
    unique_data = list(set(dado))
    contador = Counter(ticker for ticker, date, carteira in unique_data)
    ranqueado = sorted(contador.items(), key=lambda item: item[1], reverse=False)
    ticker = []
    recomen = []
    for t,r in ranqueado:
        ticker.append(t)
        recomen.append(r)
    return [ticker[-6:-1],recomen[-6:-1]]

@app.route("/table", methods=["GET"])
def gerar_tabela():
    banco.abrir_conexao()
    dados = banco.recuperar_dados()
    banco.fechar_conexao()
    return render_template("tabela.html", dados=dados)


# PARA RODAR UM PROJETO FLASK: flask --app web run
