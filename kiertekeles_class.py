class Fogadasok:
    def __init__(self, row) -> None:
        # Fogadás sorszáma,Mérkőzés,Tipp,Fogadott összeg,Win/Lose
        splitted = row.strip().split(',')
        self.sorszam = int(splitted[0])
        self.merkozes = str(splitted[1])
        self.tipp = str(splitted[2])
        self.tet = int(splitted[3])
        self.nyertel_vagy_sem = str(splitted[4])
