from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

# Tee ratkaisusi tähän:


def kaikkien_opintopisteiden_summa(suoritukset: list):

    opintopisteita_yhteensa = reduce(lambda yhteensa, alkio: yhteensa + alkio.opintopisteet, suoritukset,0)

    return opintopisteita_yhteensa



def hyvaksyttyjen_opintopisteiden_summa(suoritukset:list):


    hyvaksytyt_filtteroity = filter(lambda suoritus: suoritus.arvosana >= 1, suoritukset)

    hyvaksyttyjen_summa = reduce(lambda yhteensa, alkio: yhteensa + alkio.opintopisteet,hyvaksytyt_filtteroity, 0)

    return hyvaksyttyjen_summa



def keskiarvo(suoritukset: list):


    hyvaksytyt_filtteroity = list(filter(lambda suoritus: suoritus.arvosana >= 1, suoritukset))

    arvosanojen_summa = reduce(lambda yhteensa, alkio: yhteensa + alkio.arvosana,hyvaksytyt_filtteroity, 0)

    hyvaksyttyjen_maara = len(hyvaksytyt_filtteroity)



    return arvosanojen_summa / hyvaksyttyjen_maara



if __name__ == "__main__":
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 4, 5)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = kaikkien_opintopisteiden_summa([s1, s2, s3])
    print(summa)

    print("")
    print("")

    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3])
    print(summa)

    print("")
    print("")


    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 0, 4)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = keskiarvo([s1, s2, s3])
    print(summa)

