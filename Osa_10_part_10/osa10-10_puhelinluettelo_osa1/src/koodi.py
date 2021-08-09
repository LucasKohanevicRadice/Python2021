# Tee ratkaisusi tähän:
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            # henkilöön niittyy lista puhelinnumeroja
            self.__henkilot[nimi] = []
        self.__henkilot[nimi].append(numero)

    def hae_numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi]
    
    def hae_nimi(self, numero: str):

        for nimi, puh_nro in self.__henkilot.items():
            if numero == str(puh_nro):
                return nimi
            else:
                return None


    def kaikki_tiedot(self):
        return self.__henkilot

class Tiedostonkasittelija():
    def __init__(self, tiedosto):
        self.__tiedosto = tiedosto

    def lataa(self):
        nimet = {}
        with open(self.__tiedosto) as f:
            for rivi in f:
                osat = rivi.strip().split(';')
                nimi, *numerot = osat
                nimet[nimi] = numerot

        return nimet

    def talleta(self, luettelo: dict):
        with open(self.__tiedosto, "w") as f:
            for nimi, numerot in luettelo.items():
                rivi = [nimi] + numerot
                f.write(";".join(rivi) + "\n")

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()
        self.__tiedosto = Tiedostonkasittelija("luettelo.txt")

        # listään tiedostossa olevat nimet luetteloon
        for nimi, numerot in self.__tiedosto.lataa().items():
            for numero in numerot:
                self.__luettelo.lisaa_numero(nimi, numero)

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 lisäys")
        print("2 haku")

    def lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def numero_haku(self):
        nimi = input("nimi: ")
        numerot = self.__luettelo.hae_numerot(nimi)
        if numerot == None:
            print("numero ei tiedossa") 
            return 
        for numero in numerot:
            print(numero)     


    
    def nimi_haku(self):
        numero = input("Numero: ")
        name = self.__luettelo.hae_nimi(numero)
        if name == None:
            print("Nimi ei tiedossa")
            return
        else:
            print(name)



    def lopetus(self):
        self.__tiedosto.talleta(self.__luettelo.kaikki_tiedot())


    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                self.lopetus()
                break
            elif komento == "1":
                self.lisays()
            elif komento == "2":
                self.numero_haku()
            
            elif komento == "3":
                self.nimi_haku()

            else:
                self.ohje()

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()

# with open ("luettelo.txt") as tiedosto:
#     for rivi in tiedosto:
#         print(rivi)