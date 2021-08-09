# tee ratkaisu tänne
def muistava_sanakijra():

    while True:

        print("1 - Lisää sanapari, 2- Hae sanaa, 3 - Poistu")
        valinta = int(input("Valinta: "))

        if valinta == 1:
            sana = input("Anna sana suomeksi: ")
            word = input("Give a word in english: ")
            with open("sanakirja.txt", "a") as tiedosto:
                tiedosto.write(f"{str(sana)} - {str(word)}\n")
            print("sanapari lisätty")
        
        elif valinta == 2:
            anna = input("Anna sana: ")

            with open("sanakirja.txt") as tiedosto:

                for rivi in tiedosto:
                    if anna.lower() in rivi.lower():
                        rivi = rivi.strip()
                        print(rivi)
        

        elif valinta == 3:
            print("Moi!")
            break


muistava_sanakijra()