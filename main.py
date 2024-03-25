from os import system
from tabella_statisztika import *
import odds
import tabella_main
beolvasas('premier_tabella.csv')
beolvasas2('laliga_tabella.csv')

def main_():
    while True:
        system('cls')
        x = menu()
        match x:
            case '0':
                pass
            case '1':
                    system('cls')
                    odds.main()
            case '2':
                pass
            case '3':   
                    tabella_main.tabella_main_fugv()
            case '4':
                pass
                

def menu()-> str:
    print('Tippmix PRO\n')
    print('1 - Fogadás')
    print('2 - Kiértékelés')
    print('3 - Tabella statisztika')
    print('4 - Előzmények törlése')
    x = input('Válasz: ')
    return x
if __name__ == "__main__":
    main_()