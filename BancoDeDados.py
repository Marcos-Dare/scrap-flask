import sqlite3

# conn = sqlite3.connect("banco.db",check_same_thread=False)
# conn.execute("drop table acoes")

class MeuBanco:

    def __init__(self):
        self.conn = None

    def abrir_conexao(self):
        self.conn = sqlite3.connect("banco.db",check_same_thread=False)
        self.conn.execute("""
            Create Table if not exists acoes(
            Ticker Varchar(7) not null,
            Data Varchar(9) not null,
            Cod_Carteira int not null
            );
        """)
        self.cursor = self.conn.cursor()
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()

    def recuperar_dados(self):
        self.cursor.execute("Select * from acoes")
        dados = self.cursor.fetchall()
        return dados

    def salvar(self,dicionario, cod):
        dados = self.recuperar_dados()
        tuplas = dicionario.items()
        for tupla in tuplas:
            tupla = list(tupla)
            tupla.append(cod)
            tupla = tuple(tupla)
            if tupla not in dados:
                self.cursor.execute("insert into acoes values(?,?,?)",(tupla[0],dicionario[tupla[0]],cod))
        self.conn.commit()


class MeuBancoTeste:

    def __init__(self):
        self.conn = None

    def abrir_conexao(self):
        self.conn = sqlite3.connect("banco_teste.db",check_same_thread=False)
        self.conn.execute("""
            Create Table if not exists acoes(
            Ticker Varchar(7) not null,
            Data Varchar(9) not null,
            Cod_Carteira int not null
            );
        """)
        self.cursor = self.conn.cursor()
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()

    def recuperar_dados(self):
        self.cursor.execute("Select * from acoes")
        dados = self.cursor.fetchall()
        return dados

    def salvar(self,dicionario):
        dados = dicionario
        for dado in dados:
            self.cursor.execute("insert into acoes values(?,?,?)",(dado[0],dado[1],dado[2]))
        self.conn.commit()


