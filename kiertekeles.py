from main import *
from kiertekeles_class import Fogadasok

fogadasok_listaja: list[Fogadasok] = []

def main():
    file_open()  #A FILE NEVE MÉG KELL
    while  True:
        system('cls')
        match menu():
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
        input('Tovább...')

def file_open(filename):
    file = open(filename, 'r', encoding='UTF-8')
    for row in file:
        fogadasok_listaja.append(Fogadasok(row))
    
    file.close()




def menu()-> str:
    print('1 - Win/Lose arány')
    print('2 - Összes felrakott pénz összege')
    print('3 - Összesen elbukott pénz összege')
    print('4 - Legnagyobb fogadás')
    print('5 - Legnagyobb Win')
    print('6 - Legnagyobb Lose')
    print('7 - Összes fogadás száma')
    return input('Válasz: ')