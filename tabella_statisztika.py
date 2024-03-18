
from tabella_class import Tabella, Tabella2
tabella_adatai : list[Tabella] = []
tabella2_adatai : list[Tabella2] = []

def beolvasas(faljnev):
    file = open(faljnev, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        tabella_adatai.append(Tabella(sor))
    file.close()

def beolvasas2(faljnev):
    file = open(faljnev, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        tabella2_adatai.append(Tabella2(sor))
    file.close()

def bekeres():
    print('Premier League csapatelemző')
    bekeres = input('Csapat neve: ')
    for cs in tabella_adatai:
        if bekeres in cs.csapat:
            print(f'\tNév: {cs.csapat} ')
            print(f'\tHelyezés: {cs.helyezes}.')
            print(f'\tMérkőzések (W/D/L): {cs.merkozesek} Mérkőzés, {cs.gyozelmek}/{cs.dontetlenek}/{cs.vesztesegek}')
            print(f'\tPontok: {cs.pontok}')
            print(f'\tÁtlagos gólok száma: {cs.golok}')
            print(f'\tÁtlagos szögletszám: {cs.szoglet}')
            print(f'\tÁtlagos sárgalap szám: {cs.sargalap}')
            print(f'\tÁtlagos piroslap szám: {cs.piroslap}')
            print(f'\tLegdrágább játékos: {cs.jatekos}')
            break
    if bekeres not in cs.csapat:
        print('A keresett csapat nem található!')


def csapat_listazas():
    print('A Premier League Jelenlegi csapatai:')
    for cs in tabella_adatai:
        print(f'\t{cs.helyezes} - {cs.csapat}')


def bekeres2():
    print('La Liga csapatelemző')
    bekeres = input('Csapat neve: ')
    for cs in tabella2_adatai:
        if bekeres in cs.csapat:
            print(f'\tNév: {cs.csapat} ')
            print(f'\tHelyezés: {cs.helyezes}.')
            print(f'\tMérkőzések (W/D/L): {cs.merkozesek} Mérkőzés, {cs.gyozelmek}/{cs.dontetlenek}/{cs.vesztesegek}')
            print(f'\tPontok: {cs.pontok}')
            print(f'\tÁtlagos gólok száma: {cs.golok}')
            print(f'\tÁtlagos szögletszám: {cs.szoglet}')
            print(f'\tÁtlagos sárgalap szám: {cs.sargalap}')
            print(f'\tÁtlagos piroslap szám: {cs.piroslap}')
            print(f'\tLegdrágább játékos: {cs.jatekos}')
            break
    if bekeres not in cs.csapat:
        print('A keresett csapat nem található!')


def csapat_listazas2():
    print('A Premier League Jelenlegi csapatai:')
    for cs in tabella2_adatai:
        print(f'\t{cs.helyezes} - {cs.csapat}')