import random


class Lotto:
    def __init__(self):
        self.__nyeroszamok = []
        self.lottoszamok_generalasa()
        self.tippek = []

    def __str__(self):
        return f"Nyerőszámok: {self.__nyeroszamok}\nTippek:{self.tippek}\n"

    def get_nyeroszamok(self):
        return f"{self.__nyeroszamok}"

    def lottoszamok_generalasa(self):
        while len(self.__nyeroszamok) < 5:
            x = int(random.random()*10) + 1
            while x not in self.__nyeroszamok:
                self.__nyeroszamok.append(x)

    def tipp(self, tipp):

        if len(tipp) != 5:
            raise Exception("Öt találatot írj")

        db = 0
        i = 0
        while i < len(tipp) and db < 2:
            vizsgalt = tipp[i]
            x = 0
            db = 0
            while x < len(tipp):
                if vizsgalt == tipp[x]:
                    db += 1
                x += 1
            i += 1
        if i < 5:
            raise Exception("Hiba, kétszer szerepel egy érték")
        else:
            self.tippek.append(tipp)

    def tippjeim(self, asd):
        tippek = ""

        x = asd
        i = 0
        while i < len(self.tippek[x]):
            tippek += str(self.tippek[x][i]) + ", "
            i += 1
        return tippek

    def talalat(self):
        talalatok = []
        otos = 0
        negyes = 0
        harmas = 0
        kettes = 0
        egyes = 0
        nullas = 0

        i = 0
        while i < len(self.tippek):
            x = 0
            db = 0

            vizsgalt = self.tippek[i]
            while x < len(vizsgalt):
                if vizsgalt[x] in self.__nyeroszamok:
                    db += 1
                x += 1
            if db == 5:
                otos += 1
            elif db == 4:
                negyes += 1
            elif db == 3:
                harmas += 1
            elif db == 2:
                kettes += 1
            elif db == 1:
                egyes += 1
            else:
                nullas += 1

            i += 1

        talalatok.append(nullas)
        talalatok.append(egyes)
        talalatok.append(kettes)
        talalatok.append(harmas)
        talalatok.append(negyes)
        talalatok.append(otos)

        return talalatok
