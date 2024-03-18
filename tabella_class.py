class Tabella:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(',')
        # Helyezés,Csapat,Mérkőzések,Győzelmek,Döntetlenek,Veszteségek,Pontok,Átlagos gólok,Átlagos szögletszám,Átlagos sárgalapok száma,Átlagos piros lapok száma,Legsikeresebb játékos 
        self.helyezes = splitted[0]
        self.csapat = splitted[1]
        self.merkozesek = splitted[2]
        self.gyozelmek = splitted[3]
        self.dontetlenek = splitted[4]
        self.vesztesegek = splitted[5]
        self.pontok = splitted[6]
        self.golok = splitted[7]
        self.szoglet = splitted[8]
        self.sargalap = splitted[9]
        self.piroslap = splitted[10]
        self.jatekos = splitted[11]


class Tabella2:
    def __init__(self, row: str) -> None:
        splitted = row.strip().split(',')
        self.helyezes = splitted[0]
        self.csapat = splitted[1]
        self.merkozesek = splitted[2]
        self.gyozelmek = splitted[3]
        self.dontetlenek = splitted[4]
        self.vesztesegek = splitted[5]
        self.pontok = splitted[6]
        self.golok = splitted[7]
        self.szoglet = splitted[8]
        self.sargalap = splitted[9]
        self.piroslap = splitted[10]
        self.jatekos = splitted[11]
        