from anytree import Node, RenderTree

ROZMIAR = 4

def mozliwe_pozycje_zera(pozycja, poprzednia_pozycja):
    pozycje = []

    if pozycja - ROZMIAR != poprzednia_pozycja:
        if pozycja - ROZMIAR >= 0:
            pozycje.append(pozycja - ROZMIAR)

    if pozycja + ROZMIAR != poprzednia_pozycja:
        if pozycja + ROZMIAR < ROZMIAR**2:
            pozycje.append(pozycja + ROZMIAR)

    if pozycja + 1 != poprzednia_pozycja:
        if int(pozycja / ROZMIAR) == int((pozycja + 1) / ROZMIAR) and pozycja + 1 < ROZMIAR**2:
            pozycje.append(pozycja + 1)

    if pozycja - 1 != poprzednia_pozycja:
        if int(pozycja / ROZMIAR) == int((pozycja - 1) / ROZMIAR) and pozycja - 1 >= 0:
            pozycje.append(pozycja - 1)

    return pozycje

def print_pozycje(pozycja):
    print(pozycja, " - ", mozliwe_pozycje_zera(pozycja, pozycja))

def dodaj_galezie(pien, licznik):
    if licznik == 0:
        return
    for pozycja in mozliwe_pozycje_zera(pien.name, pien.parent.name):
        galaz = Node(pozycja, parent=pien)
        dodaj_galezie(galaz, licznik-1)


if __name__ == '__main__':
    pola = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print("0  1  2  3  \n"
          "4  5  6  7  \n"
          "8  9  10 11 \n"
          "12 13 14 15 \n")

    start = 0
    poczatek = Node(start, parent=Node(start))

    dodaj_galezie(poczatek, 5) # glebokosc drzewa

    for pre, fill, node in RenderTree(poczatek):    # podjebane ze stacka drukowanie drzewa xd
        print("%s%s" % (pre, node.name))
