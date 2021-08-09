# tee ratkaisu tänne

def luettelo():

    luutelo = {}

    while True:

        komento = int(input("komento ( 1 hae, 2 lisää, 3 lopeta): "))

        if komento == 1:

            nimi = input("nimi: ")
            if nimi not in luutelo:
                print("ei numeroa")
                continue
            print(luutelo[nimi])


        elif komento == 2:

            nimi = input("nimi: ")
            numero = input("numero: ")
            luutelo.update([(nimi, numero)])
            print("ok!")

        elif komento == 3:
            print("lopetetaan...")
            return luutelo


luettelo()