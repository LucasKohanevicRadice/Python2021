#   Tehtävänanto tähän tehtävään löytyy osoitteesta https://ohjelmointi-21.mooc.fi/osa-12/4-saannolliset-lausekkeet
#   Tehtävän nimi on Tilastot ojennukseen.

import json

class datantallennin:

    def __init__(self,) -> None:

        self.kaikki = []
        self.pelaajat = []
        self.joukkueet = []
        self.maat = []
        self.pelaajien_maara = 0
    
    def tiedostonpurkaja(self, tiedoston_nimi: str):

        pelaajamaara = 0

        try:
            with open(tiedoston_nimi) as tiedosto:
                data = tiedosto.read()
            
            purettu_tiedosto = json.loads(data)

            for pelaajatiedot in purettu_tiedosto:
                self.kaikki.append(pelaajatiedot)
                self.pelaajat.append(pelaajatiedot["name"])
                self.joukkueet.append(pelaajatiedot["team"])
                self.maat.append(pelaajatiedot["nationality"])
                pelaajamaara += 1
            self.pelaajien_maara = pelaajamaara

        except:
            raise ValueError(f"Ei löytynyt tiedostoa nimellä {tiedoston_nimi}")
            # print(f"Ei löytynyt tiedostoa nimellä {tiedoston_nimi}")


data = datantallennin()

def joukkueet_aakkosjarjestyksessa():

    return sorted(data.joukkueet)

def maat_aakkosjarjestyksessa():  

    return sorted(data.maat)




def joukkueen_pelaajat(joukkue: str):

    pelaajat_joukkueessa = []

    try:

        for tiedot in data.kaikki:
            if tiedot["team"].lower() == joukkue.lower():
                pelaajat_joukkueessa.append(tiedot["name"])
        return pelaajat_joukkueessa
    
    except:
        print(f"Joukkuetta ei löytynyt lyhtenteellä {joukkue}.")
    

def maan_pelaajat(maa : str):


    maajoukkupelaajat = []

    try:

        for tiedot in data.kaikki:
            if tiedot["nationality"].lower() == maa.lower():
                maajoukkupelaajat.append(tiedot["name"])
        return maajoukkupelaajat
    
    except:
        print(f"Maata ei löytynyt lyhtenteellä {maa}.")



def eniten_pisteitä():

    pistekuningas = data.kaikki[0]

    for pelaaja in data.kaikki:
        if (pelaaja["goals"] + pelaaja["assists"]) > (pistekuningas["goals"] + pistekuningas["assists"]):
            pistekuningas = pelaaja
    
    return pistekuningas["name"]

def eniten_maaleja():

    maalikuningas = data.kaikki[0]

    for pelaaja in data.kaikki:
        if pelaaja["goals"] > maalikuningas["goals"]:
            maalikuningas = pelaaja
    
    return maalikuningas["name"]


def pelaajatiedot(pelaaja: str):

    pelaaja_nimi = ""
    pelaaja_maa = ""
    pelaaja_syotot = 0
    pelaaja_maalit = 0
    pelaaja_joukkue = ""
    plussa = "+"
    yht = "="
    väli = " "

    try:
        for pelaajatiedot in data.kaikki:
            if pelaajatiedot["name"].lower() == pelaaja.lower():
                pelaaja_nimi = pelaajatiedot["name"]
                pelaaja_maa = pelaajatiedot["nationality"]
                pelaaja_syotot = pelaajatiedot["assists"]
                pelaaja_maalit = pelaajatiedot["goals"]
                pelaaja_joukkue = pelaajatiedot["team"]
    except:
        print(f"Nimellä {pelaaja} ei löytynyt mitään tilastoja")
    
    pelaaja_yht_pisteet = pelaaja_syotot + pelaaja_maalit

    muotoiltu = f"{pelaaja_nimi:22}{pelaaja_joukkue:4}{str(pelaaja_maalit):>3}{plussa:>3}{str(pelaaja_syotot):>4}{yht:>3}{pelaaja_yht_pisteet:>4}"

    return muotoiltu





def komennot():

    komentolista = ("""0 lopeta
1 hae pelaajaa
2 joukkueet
3 maat
4 joukkueen pelaajat
5 maan pelaajat
6 eniten pisteitä
7 eniten maaleja""")

    return komentolista


def sovellus_main():

    tiedosto = input("Haettava tiedosto: ")
    data.tiedostonpurkaja(tiedosto)
    
    print(f"luettiin {data.pelaajien_maara} pelaajan tiedot")

    print("")
    print("komennot:")
    print(komennot())

    while True:
        komento = int(input("komento: "))

        if komento == 0:
            break

        elif komento == 1:
            pelaajan_nimi = input("nimi: ")
            print(pelaajatiedot(pelaajan_nimi))
        
        elif komento == 2:
            for joukkue in joukkueet_aakkosjarjestyksessa():
                print(joukkue)
        
        elif komento == 3:
            for maa in maat_aakkosjarjestyksessa():
                print(maa)
        
        elif komento == 4:
            joukkue = input("Haettava joukkue: ")
            for pelaaja in joukkueen_pelaajat(joukkue):
                print(pelaaja)
        
        elif komento == 5:
            maa = input("Maajoukkueen pelaajat: ")
            for pelaaja in maan_pelaajat(maa):
                print(pelaaja)
        
        elif komento == 6:
            print(eniten_pisteitä())
        
        elif komento == 7:
            print(eniten_maaleja())




# sovellus_main()


"""     Ainoo mikä puuttuu on tulostuksen muotoilu        """


# print(komennot())

# Esimerkkitulostus
# Leon Draisaitl       EDM  43 + 67 = 110
# Connor McDavid       EDM  34 + 63 =  97
# Travis Zajac         NJD   9 + 16 =  25
# Mike Green           EDM   3 +  8 =  11
# Markus Granlund      EDM   3 +  1 =   4
# 123456789012345678901234567890123456789


data.tiedostonpurkaja("kaikki.json")
sovellus_main()

# print(pelaajatiedot("Travis Zajac"))
# print(pelaajatiedot("Leon Draisaitl"))
# print(pelaajatiedot("Connor McDavid"))
# print(pelaajatiedot("Mike Green"))
# print(pelaajatiedot("Markus Granlund"))
# print(pelaajatiedot("Mark Jankowski"))
# print(pelaajatiedot("Buddy Robinson"))
# print(pelaajatiedot("John Klingberg"))
# print(pelaajatiedot("Taylor Fedun"))