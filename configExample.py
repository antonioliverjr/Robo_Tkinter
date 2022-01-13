import pyodbc
from abc import ABC, abstractmethod
from datetime import datetime
import os
import enum


class Context(ABC):
    def __init__(self, banco:str, servidor:str, database:str, uid:str, pwd:str):
        self.conn = pyodbc.connect(
            'DRIVER='+'{'+banco+'}'+';SERVER='+servidor+';DATABASE='+database+';UID='+uid+';PWD='+pwd            
        )


class Ms_sql(enum.Enum):
    BANCO = "ODBC Driver 17 for SQL Server"
    SERVIDOR = "localhost\\SQLEXPRESS"
    USER = ""
    PASSWORD = ""


class Commerce(Context):
    def __init__(self, banco: str, servidor: str, database: str, uid: str, pwd: str):
        super().__init__(banco, servidor, database, uid, pwd)


class Adventure(Context):
    def __init__(self, banco: str, servidor: str, database: str, uid: str, pwd: str):
        super().__init__(banco, servidor, database, uid, pwd)

    
class Db_operacoes(ABC):
    def data_atual(self) -> str:
        return datetime.now().strftime('%Y%m%d')
    
    @abstractmethod
    def close(self): pass

    def limpar_pastas(self, path) -> None:
        date_atual = self.data_atual()
        for root, dirs, files in os.walk(path):
            for file in files:
                if not date_atual in file:
                    os.remove(os.path.join(path, file))


class Color(enum.Enum):
    BACKGROUND_BG = "Black"
    BACKGROUND_IT = "White"
    FONTE_TEXT = "SteelBlue"
    LABEL_BG = "DarkGreen"

    