class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

class Kiipeilykallio:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.__reitit = []

    def lisaa_reitti(self, reitti: Kiipeilyreitti):
        self.__reitit.append(reitti)

    def reitteja(self):
        return len(self.__reitit)

    def vaikein_reitti(self):
        def vaikeuden_mukaan(reitti):
            return reitti.grade

        reitit_jarjestyksessa = sorted(self.__reitit, key=vaikeuden_mukaan)
        # otetaan reiteistä viimeinen
        return reitit_jarjestyksessa[-1]

    def __str__(self):
        vaikein_reitti = self.vaikein_reitti()
        return f"{self.nimi} {self.reitteja()} reittiä, vaikein {vaikein_reitti.grade}"
    


def reittien_maaran_mukaan(reitit: list):

    def maarittelyehto_ReittienMaara(reitti: Kiipeilykallio):

        return reitti.reitteja()
        
    reitit.sort(key = maarittelyehto_ReittienMaara)
        
    return reitit


def vaikeimman_reitin_mukaan(reitit: list):


    def maarittelyehto_ReittienVaikeus(reitti: Kiipeilyreitti):

        return Kiipeilykallio.vaikein_reitti(reitti) #    Palaa tähän jos tulee hämminkiä, tää on tod näk se ongelma
    
    reitit.sort(key = maarittelyehto_ReittienVaikeus, reverse = True)
    
    return reitit

# Dont fucking getcha.
        




k1 = Kiipeilykallio("Olhava")
k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

k2 = Kiipeilykallio("Nummi")
k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

k3 = Kiipeilykallio("Nalkkilan släbi")
k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))


kalliot = [k1, k2, k3]
# for reitti in kalliot:
#     print(reitti)
for reitti in kalliot:
    print(Kiipeilykallio.vaikein_reitti(reitti))

# for kallio in reittien_maaran_mukaan(kalliot):
#     print(kallio)


kalliot = [k1, k2, k3]
for kallio in vaikeimman_reitin_mukaan(kalliot):
    print(kallio)




