from main import *
from os import system
from kiertekeles_class import Fogadasok

fogadasok_listaja: list[Fogadasok] = []

def main_2():
    file_open('eddigi_fogadasok.csv')
    while  True:
        system('cls')
        match al_menu():
            case '1':
                winek_szama = winekszama()
                loseok_szama = loseokszama()
                print(f'Az eddigi fogadások során Win/Lose arány: {winek_szama}:{loseok_szama}')
            case '2':
                osszes_penz = osszes_felrakott_penz()
                print(f'Eddigi összes felrakott pénz: {osszes_penz} Ft')
            case '3':
                total_lose_money = osszes_elbukott_penz()
                print(f'Eddgig összes elbukott pénz fogadásokon: {total_lose_money} Ft')
            case '4':
                legnagyobb_fogadas_osszege = legnagyobb_fogadas()
                print(f'Az eddigi fogadásaid közül a legnagyobb tét az  Ft volt.')
            case '5':
                pass
            case '6':
                pass
            case '7':
                osszes = osszes_fogadas_szama()
                print(f'Eddigi fogadásaid száma: {osszes} db')
        input('Tovább...')


def al_menu()-> str:
    print('1 - Win/Lose arány')
    print('2 - Összes felrakott pénz összege')
    print('3 - Összesen elbukott pénz összege')
    print('4 - Legnagyobb fogadás')
    print('5 - Legnagyobb Win')
    print('6 - Legnagyobb Lose')
    print('7 - Összes fogadás száma')
    return input('Válasz: ')


def file_open(filename):
    file = open(filename, 'r', encoding='UTF-8')
    for row in file:
        fogadasok_listaja.append(Fogadasok(row))
    file.close()

def winekszama():
    winek_szama = 0
    for f in fogadasok_listaja:
        if f.nyertel_vagy_sem == 'Win':
            winek_szama += 1
    return winek_szama

def loseokszama():
    loseok_szama = 0
    for f in fogadasok_listaja:
        if f.nyertel_vagy_sem == 'Win':
            loseok_szama += 1
    return loseok_szama

def osszes_felrakott_penz()-> int:
    osszes_penz = 0
    for f in fogadasok_listaja:
        osszes_penz += f.tet
    return osszes_penz

def osszes_elbukott_penz():
    total_lose_money = 0
    for f in fogadasok_listaja:
        if f.nyertel_vagy_sem == 'Lose':
            total_lose_money += f.tet
    return total_lose_money

def legnagyobb_fogadas():
    legnagyobb_fogadas_osszege = 0
    for f in fogadasok_listaja:
        if f.tet > legnagyobb_fogadas_osszege:
            legnagyobb_fogadas_osszege = f
    return legnagyobb_fogadas_osszege


def legnagyobb_win():
    legnagyobb_gyozelem = 0

def legnagyobb_lose():
    legnagyobb_vestes = 0


def osszes_fogadas_szama()->int:
    osszes = 0
    for f in fogadasok_listaja:
        if f.sorszam > osszes:
            osszes = f.sorszam
    return osszes

main_2()