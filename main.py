from os import system
from tabella_statisztika import *
beolvasas('premier_tabella.csv')
beolvasas2('laliga_tabella.csv')

def main():
    while True:
        system('cls')
        match menu():
            case '0':
                pass
            case '1':
                pass
            case '2':
                pass
            case '3':
                    while True:
                        system('cls')
                        print('1 - Premier League jelenlegi csapatai helyezés sorrendben')
                        print('2 - Premier League csapat elemző')
                        print('3 - La Liga jelenlegi csapatai helyezés sorrendben')
                        print('4 - La Liga csapat elemző')
                        print('5 - Vissza')
                        valasztas = input('Választás: ')
                        match valasztas:
                            case '1':
                                csapat_listazas()
                            case '2':
                                bekeres()
                            case '3':
                                csapat_listazas2()
                            case '4':
                                bekeres2()
                            case '5':
                                break
                        input('Tovább...')
            case '4':
                pass
                


def menu()-> str:
    print('1 - Fogadás')
    print('2 - Kiértékelés')
    print('3 - Tabella statisztika')
    print('4 - Előzmények törlése')
    return input('Válasz: ')




    




main()