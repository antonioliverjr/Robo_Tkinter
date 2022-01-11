from tkinter import Tk, StringVar
from config import Commerce
from gui_app import GuiApp, N, S, E, W
from commerce import Db_Commerce
from adventure import Db_Adventure
from datetime import datetime

''' Execução de JOB para extração e importação de dados '''
def main():
    def data_log():
        return datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    def start(add_result, registros, importacao):
        '''
        Manipulação das classe Adventure e do GUI para adquirir os dados e gerar os arquivos txt e zip...
        '''
        adventure = Db_Adventure()

        if adventure.consulta():
            add_result(f'{data_log()}: Arquivos selecionados!')
        else:
            add_result(f'{data_log()}: Houve um erro ao selecionar os dados...')

        if adventure.exportar(adventure.tabela):
            add_result(f'{data_log()}: Arquivos exportados com sucesso!')
            if adventure.verificar_arquivo():
                add_result(f'{data_log()}: Aguarde a compactação...')
                if adventure.compactar():
                    add_result(f'{data_log()}: Arquivo compactado com sucesso!')
                else:
                    add_result(f'{data_log}: Houve um erro ao compactar...')

        '''
        Manipulação das classe Commerce e do GUI para copiar o arquivo zip e inserir os dados do txt...
        '''
        commerce = Db_Commerce()
        commerce.copy_arquivos()
        importados = commerce.importar()
        if importados > 0:
            add_result(f'{data_log()}: Foram importados {str(importados)} Registro(s).')
            registros.set(f'{str(importados)}')
            importacao.set(f'{data_log()}')


    menu = Tk()
    menu.gui = GuiApp(menu)
    result = []
    resultados = StringVar(value=result)

    def add_result(texto):
       result.append(texto)
       resultados.set(result)

    add_result("Console de Operações")
    add_result(f"{data_log()}: Aguardando Iniciar...")

    registros = StringVar()
    importacao = StringVar()
    menu.gui.total_registros['textvariable'] = registros
    menu.gui.data_importacao['textvariable'] = importacao
    menu.gui.iniciar['command'] = lambda: start(add_result, registros, importacao)
    menu.gui.console['listvariable'] = resultados
    menu.mainloop()

if __name__ == '__main__':
    main()