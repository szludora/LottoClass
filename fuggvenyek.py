import random
from Lotto import Lotto

lottoszelvenyek = []
lotto = Lotto()


def szelvenyek_generalasa(ennyiszer):
    y = 0

    while y < ennyiszer:

        i = 0
        tippek = []

        while len(tippek) < 5:
            x = int(random.random()*10) + 1
            while x not in tippek:
                tippek.append(x)
            i += 1

        lotto.tipp(tippek)
        lottoszelvenyek.append(lotto)
        y += 1


def erretettek():
    i = 0
    while i < len(lottoszelvenyek):
        ezaszelveny = lottoszelvenyek[i]
        print(ezaszelveny.tippjeim(i))
        i += 1


def kiiratas():
    x = lotto.talalat()

    print(f"Nulla találatos: {x[0]}")
    print(f"Egy találatos: {x[1]}")
    print(f"Kettő találatos: {x[2]}")
    print(f"Három találatos: {x[3]}")
    print(f"Négy találatos: {x[4]}")
    print(f"Öt találatos: {x[5]}")
