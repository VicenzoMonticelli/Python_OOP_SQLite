import sqlite3

class Database:
    conexao = None
    cursor = None

  #Métudo construtor
    def __init__(self):
        #global conexao, cursor
        self.conexao = sqlite3.connect("database/imdb.db")
        self.cursor = self.conexao.cursor()

    def __del__(self):
        conexao.commit()
      