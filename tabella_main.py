from tabella_statisztika import *
def tabella_main_fugv():
    beolvasas('premier_tabella.csv')
    beolvasas2('laliga_tabella.csv')
    while True:
        match tabella_menu():
            case '1':
                csapat_listazas()
            case '2':
                bekeres()
            case '3':
                csapat_listazas2()
            case '4':
                bekeres2()
        input('Vissza...')

def tabella_menu() -> str:
    print('1 - Premier League jelenlegi csapatai helyezés sorrendben')
    print('2 - Premier League csapat elemző')
    print('3 - La Liga jelenlegi csapatai helyezés sorrendben')
    print('4 - La Liga csapat elemző')
    return input('Választás: ')
tabella_main_fugv()