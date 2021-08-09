# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def viiva(luku, merkkijono):

    if merkkijono == "":
        merkkijono = "*"
        print(luku*merkkijono)

    else:
        print(luku*merkkijono[0])


if __name__ == "__main__":
    viiva(5, "x")
