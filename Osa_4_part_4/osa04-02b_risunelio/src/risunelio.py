# kopioi edellisestä tehtävästä funktion viiva koodi tänne



def viiva(luku, merkkijono):

    if merkkijono == "":
        merkkijono = "*"
        print(luku*merkkijono)

    else:
        print(luku*merkkijono[0])



def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    for i in range(0,koko):
        viiva(koko, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
