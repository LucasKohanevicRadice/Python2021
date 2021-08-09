# tee ratkaisu tänne


def paivakirja():

    while True:

        print("1 - lisää merkintä, 2 - lue merkintä, 0 - lopeta ")
        valinta = int(input("Valinta: "))

        if valinta == 1:
            merkinta = input("Anna merkintä: ")
            with open("paivakirja.txt", "a") as tiedosto:
                tiedosto.write(f"{merkinta}\n")
            print("Päiväkirja tallennettu")

        elif valinta == 2:
            print("Merkinnät: ")
            with open("paivakirja.txt") as tiedosto:
                print(tiedosto.read())
    
        elif valinta == 0:
            print("Heippa!")
            break

paivakirja()