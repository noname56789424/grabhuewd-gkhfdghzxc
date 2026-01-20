import sys

# ===== WPROWADZANIE NAZWY =====
nazwa_uzytkownika = input("Wpisz nazwę: ")

# Zakazane nazwy
if nazwa_uzytkownika == "nie lubie piesków":
    print("Złamałeś zasady")
    sys.exit()

elif nazwa_uzytkownika == "dev":
    print("Nie możesz iść dalej")
    sys.exit()

else:
    print("Świetna nazwa")

# ===== PĘTLA KOMEND =====
while True:
    cmd = input("Wpisz komendę (wpisz /help aby zobaczyć komendy): ")

    if cmd == "sprawdz":
        print(nazwa_uzytkownika)

    elif cmd == "zmien":
        nowa_nazwa = input("Podaj nową nazwę: ")

        if nowa_nazwa == nazwa_uzytkownika:
            print("Nowa nazwa nie może być taka sama jak obecna")

        elif nowa_nazwa == "nie lubie piesków":
            print("Ta nazwa jest zabroniona")

        elif nowa_nazwa == "dev":
            print("Ta nazwa jest zarezerwowana")

        else:
            nazwa_uzytkownika = nowa_nazwa
            print("Nazwa zmieniona")

    elif cmd == "/help":
        print("Komendy:")
        print("sprawdz    - pokazuje nazwę")
        print("zmien      - zmienia nazwę")
        print("nazwa gry  - pokazuje nazwę gry")
        print("exit       - kończy program")

    elif cmd == "nazwa gry":
        print("NIE WIEM")

    elif cmd == "dev tools":
        print("############################")
        haslo = input("Wpisz hasło: ")

        if haslo == "unlock dev tools":
            print("Nie ma żadnych dev tools narazie")
        else:
            print("Błędne hasło")

    elif cmd == "exit":
        print("Koniec programu")
        break

    else:
        print("Nieznana komenda")


