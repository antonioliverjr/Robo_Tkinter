from gui_app import GuiApp
from commerce import Db_Commerce
from adventure import Db_Adventure


def main():
    #menu = GuiApp()
    #menu.main.mainloop()

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

    


if __name__ == '__main__':
    main()