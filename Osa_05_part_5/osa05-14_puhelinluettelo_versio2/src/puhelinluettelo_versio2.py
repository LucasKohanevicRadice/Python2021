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
            
            for nimi, numerot in luutelo.items():

                for numero in numerot:
                    print(numero)
                


        elif komento == 2:

            nimi = input("nimi: ")
            numero = input("numero: ")
                
            if nimi not in luutelo:
                luutelo[nimi] = [numero]
            
            else:
                luutelo[nimi].append(numero)

            print("ok!")

        elif komento == 3:
            print("lopetetaan...")
            return luutelo


luettelo()





