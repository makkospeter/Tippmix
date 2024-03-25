from os import system
from tabella_statisztika import *
from odds import keres_meccs, rand_meccs
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
                    while True:
                        melyik = 0
                        system('cls')
                        while melyik != 1 and melyik != 2:
                            melyik = int(input('Keresni szeretne a csapatok között vagy véletlen felajánlást kíván?(Keres - 1, Véletlen - 2):  '))
                            match melyik:
                                case 1:
                                    keres_meccs()
                                case 2:  
                                    rand_meccs()
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
    x = input('Válasz: ')
    return x
if __name__ == "__main__":
    main_()