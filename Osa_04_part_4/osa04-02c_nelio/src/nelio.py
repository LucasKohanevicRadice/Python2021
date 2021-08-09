# kopioi edellisestä tehtävästä funktion viiva koodi tänne


def viiva(luku, merkkijono):

    if merkkijono == "":
        merkkijono = "*"
        print(luku*merkkijono)

    else:
        print(luku*merkkijono[0])




def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla

    for i in range(0, koko):
        viiva(koko, merkki)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
