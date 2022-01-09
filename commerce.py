from datetime import date
from config import *
from zipfile import ZipFile
import shutil


class Db_Commerce(Db_operacoes):
    PASTA_COM = 'dados_commerce/'
    PASTA_ZIP = 'dados_zip/'

    def __init__(self):
        self.__context = Commerce(Ms_sql.BANCO.value, Ms_sql.SERVIDOR.value, "COMMERCE", Ms_sql.USER.value, Ms_sql.PASSWORD.value)
        self.cursor = self.__context.conn.cursor()
        self.tabela = {}

    def close(self):
        self.cursor.close()
        self.__context.conn.close()

    def commit(self):
        self.__context.conn.commit()

    def arquivo_zip(self):
        return f'adventure_product_{self.data_atual()}.zip'
    
    def arquivo_dia(self):
        return f'{self.PASTA_COM}adventure_product_{self.data_atual()}.txt'

    def total_registros(self) -> int:
        self.cursor.execute("select count(*) as total from loja.produtos")
        total = self.cursor.fetchone()
        return total[0]
    
    def truncate(self) -> bool:
        if len(self.tabela) > 0:
            self.cursor.execute('truncate table loja.produtos')
            self.commit()
            return True

        return False

    def inserir(self, nome:str, produto_numero:str, level_estoque:int, ponto_reposicao:int,
    dt_modificacao:str):
        try:
            sql = 'insert into loja.produtos(nome, produto_numero, level_estoque, ponto_reposicao, dt_modificacao) values(?, ?, ?, ?, ?)'
            self.cursor.execute(sql, (nome, produto_numero, level_estoque, ponto_reposicao, dt_modificacao))
            self.commit()
        except Exception as e:
            return e
        
        return True

    def copy_arquivos(self) -> bool:
        try:
            arquivo_zip = self.arquivo_zip()
            self.limpar_pastas(self.PASTA_COM)
            zip_destino = os.path.join(self.PASTA_COM, arquivo_zip)
            for file in os.listdir(self.PASTA_ZIP):
                if file == arquivo_zip:
                    shutil.copy(os.path.join(self.PASTA_ZIP, arquivo_zip),
                    zip_destino)

                    with ZipFile(zip_destino, 'r') as zip:
                        zip.extractall(self.PASTA_COM)

                    shutil.move(f'{self.PASTA_COM}adventure_product.txt', self.arquivo_dia())
        except Exception as e:
            return e

        return True

    def importar(self) -> int:
        try:
            count = 1        
            with open(self.arquivo_dia(), 'r') as file:
                for linha in file:
                    produto = eval(linha)
                    self.tabela[count] = {
                        'produto_id': produto['ProductID'],
                        'nome': produto['Name'],
                        'produto_numero': produto['ProductNumber'],
                        'level_estoque': produto['SafetyStockLevel'],
                        'ponto_reposicao': produto['ReorderPoint'],
                        'dt_modificacao': produto['ModifiedDate']
                    }
                    count += 1
        except Exception as e:
            return e
        finally:
            if len(self.tabela) > 0:
                if self.truncate():
                    for valor in self.tabela:
                        self.inserir(
                            self.tabela[valor]['nome'],
                            self.tabela[valor]['produto_numero'],
                            self.tabela[valor]['level_estoque'],
                            self.tabela[valor]['ponto_reposicao'],
                            self.tabela[valor]['dt_modificacao']
                        )
            else:
                raise ValueError("Houve um erro no processamento de dados do arquivo txt!")

        resultados = self.total_registros()
        self.close()
        return resultados
