from os import system

def main():
    while  True:
        system('cls')
        match menu():
            case '0':
                pass
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
        input('Tovább...')
                


def menu()-> str:
    print('1 - Fogadás')
    print('2 - Kiértékelés')
    print('3 - Tabella statisztika')
    print('4 - Előzmények törlése')
    return input('Válasz: ')




    




main()