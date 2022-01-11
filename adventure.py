from config import *
import os
from zipfile import ZipFile


class Db_Adventure(Db_operacoes):
    PASTA_ADV = 'dados_adventure/'
    PASTA_ZIP = 'dados_zip/'

    def __init__(self):
        self.__context = Adventure(Ms_sql.BANCO.value, Ms_sql.SERVIDOR.value, "AdventureWorks2019", Ms_sql.USER.value, Ms_sql.PASSWORD.value)
        self.cursor = self.__context.conn.cursor()
        self.tabela = []
        self.arquivo = ''

    def close(self):
        self.cursor.close()
        self.__context.conn.close()

    def arquivo_dia(self):
        return f'{self.PASTA_ADV}adventure_product_{self.data_atual()}.txt'

    def arquivo_zip(self):
        return f'adventure_product_{self.data_atual()}.zip'

    def consulta(self) -> bool:
        try:
            self.cursor.execute('''
        SELECT
            ProductID
            ,Name
            ,ProductNumber
            ,SafetyStockLevel
            ,ReorderPoint
            ,format(ModifiedDate, 'yyyy-MM-dd') as ModifiedDate
        FROM AdventureWorks2019.Production.Product
        ''')
            colunmNames = [colunm[0] for colunm in self.cursor.description]
            self.product = self.cursor.fetchall()
            for dados in self.product:
                self.tabela.append(dict(zip(colunmNames, dados)))
        except Exception as e:
            return e
        finally:
            self.close()
        
        return True

    def exportar(self, lista) -> bool:
        try:
            self.arquivo = self.arquivo_dia()
            self.limpar_pastas(self.PASTA_ADV)
            with open(self.arquivo, 'w') as adv:
                for dados in lista:
                    adv.write(str(dados)+"\n")
        except Exception as e:
            return e

        return True

    def compactar(self) -> bool:
        try:
            arquivo_dia = self.arquivo_dia()
            self.limpar_pastas(self.PASTA_ZIP)
            arquivo_zip = f'{self.PASTA_ZIP}{self.arquivo_zip()}'
            with ZipFile(arquivo_zip, 'w') as zip:
                zip.write(arquivo_dia, 'adventure_product.txt')
        except Exception as e:
            return e
        
        return True


    def verificar_arquivo(self) -> bool:
        arquivo_dia = self.arquivo_dia()
        if os.path.exists(arquivo_dia):
            return True

        return False