# tee ratkaisu tänne



# lukulista = []

# with open("matriisi.txt") as tiedosto:


#     for rivi in tiedosto:

#         rivi = rivi.replace("\n", "")
#         luvut = rivi.split(",")

#         lukulista.append(luvut)

# #   Tässä yks tapa
# lukulista = [[int(luku) for luku in luvut] for luvut in lukulista]

# #   Toinen tapa, joka PITÄÄ OTTAA HALTUUN. On enumerate

# for luvut in lukulista:

#     for indeksi, arvo in enumerate(luvut):

#         luvut[indeksi] = int(arvo)
      

from os import name


def pura_tiedosto():

    kaikki_tarvittava = {}
    lukulista = []

    kaikki_alkiot = []
    rivisummat = []

    with open("matriisi.txt") as tiedosto:

        for rivi in tiedosto:
            
            rivi = rivi.replace("\n", "")
            luvut = rivi.split(",")

            lukulista.append(luvut)
    

    lukulista = [[int(luku) for luku in luvut] for luvut in lukulista]

    for luvut in lukulista:

        rivisummat.append(sum(luvut))
    
    for luvut in lukulista:

        for alkio in luvut:
            kaikki_alkiot.append(alkio)
    

    kaikki_tarvittava["maksimi"] = max(kaikki_alkiot)
    kaikki_tarvittava["rivisummat"] = rivisummat
    kaikki_tarvittava["summa"] = sum(kaikki_alkiot)

    return kaikki_tarvittava
    



def summa():

    kaikki_data = pura_tiedosto()

    return kaikki_data["summa"]

def maksimi():

    kaikki_data = pura_tiedosto()

    return kaikki_data["maksimi"]

def rivisummat():

    kaikki_data = pura_tiedosto()

    return kaikki_data["rivisummat"]




if __name__ == "__main__":

    summa()
    maksimi()
    rivisummat()




