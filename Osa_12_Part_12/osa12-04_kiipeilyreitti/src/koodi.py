class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

# Tee ratkaisusi tähän:


def pituuden_mukaan(reitit: list):

    laskevassa_jarjestyksessa = []

    def maarittelyehto_LaskevaPituus(reitti: Kiipeilyreitti):

        return reitti.pituus
    
    reitit.sort(key = maarittelyehto_LaskevaPituus, reverse = True)

    return reitit


    

def vaikeuden_mukaan(reitit: list):

    nousevassa_jarjestyksessa = []

    def maarittelyehto_VaikeudenMukaan(reitti: Kiipeilyreitti):

        return reitti.grade
    
    reitit.sort(key = maarittelyehto_VaikeudenMukaan)
    
    for reitti in reitit:

        if len(nousevassa_jarjestyksessa) == 0:
            nousevassa_jarjestyksessa.append(reitti)

        elif reitti.grade == nousevassa_jarjestyksessa[len(nousevassa_jarjestyksessa)-1].grade:

            if reitti.pituus > nousevassa_jarjestyksessa[len(nousevassa_jarjestyksessa)-1].pituus:
                nousevassa_jarjestyksessa.insert(len(nousevassa_jarjestyksessa-1), reitti)
            else:
                nousevassa_jarjestyksessa.append(reitti)
        
        #   Well ive done fucked up
    

    return nousevassa_jarjestyksessa

    #   Dont work
    






    

if __name__ == "__main__":
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 11, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Pieniä askelia", 12, "6A+")

    reitit = [r1, r2, r3, r4]

    for reitti in pituuden_mukaan(reitit):
        print(reitti)

    for reitti in vaikeuden_mukaan(reitit):
        print(reitti)



    

        
