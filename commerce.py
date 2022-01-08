from config import *


class Db_Commerce(Db_operacoes):
    def __init__(self):
        self.__context = Commerce(Ms_sql.BANCO.value, Ms_sql.SERVIDOR.value, "COMMERCE", Ms_sql.USER.value, Ms_sql.PASSWORD.value)
        self.cursor = self.__context.conn.cursor()

    def inserir(self):
        pass

    def truncate(self):
        pass

    def importar(self):
        pass

    def exportar(self):
        pass
