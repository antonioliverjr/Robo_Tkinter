from gui_app import GuiApp
from commerce import Db_Commerce
from adventure import Db_Adventure


def main():
    #menu = GuiApp()
    #menu.main.mainloop()

    '''
    Manipulação das classe Adventure e do GUI para adquirir os dados e gerar os arquivos txt e zip...
    '''
    adventure = Db_Adventure()

    if adventure.consulta():
        print("Arquivos selecionados!")
    else:
        print("Houve um erro ao selecionar os dados...")

    if adventure.exportar(adventure.tabela):
        print("Arquivos exportados com sucesso!")
        if adventure.verificar_arquivo():
            print("Aguarde a compactação...")
            if adventure.compactar():
                print("Arquivo compactado com sucesso!")
            else:
                print("Houve um erro ao compactar...")

    '''
    Manipulação das classe Commerce e do GUI para copiar o arquivo zip e inserir os dados do txt...
    '''

    commerce = Db_Commerce()
    commerce.copy_arquivos()
    result = commerce.importar()
    if result > 0:
        print(f'Foram importados {result} Registro(s).')


if __name__ == '__main__':
    main()