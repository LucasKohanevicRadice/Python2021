# kopioi edellisestä tehtävästä funktion viiva koodi tänne



def viiva(luku, merkkijono):

    if merkkijono == "":
        merkkijono = "*"
        print(luku*merkkijono)

    else:
        print(luku*merkkijono[0])



def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla

    for i in range(0, korkeus):
        viiva(10, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
