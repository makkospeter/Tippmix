class Fogadasok:
    def __init__(self, row) -> None:
        splitted = row.split(',')
        self.sorszam = int(splitted[0])
        self.merkozes = splitted[1]
        self.tipp = splitted[2]
        self.tet = int(splitted[3])
        self.nyertel_vagy_sem = splitted[4]
