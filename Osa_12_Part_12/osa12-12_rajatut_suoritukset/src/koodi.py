def välitulostus():
    for i in range(3):
        print("")





class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"


def hyvaksytyt(suoritukset: list):

    hyväksytyt_suoritukset = filter(lambda suoritus: suoritus.arvosana > 0, suoritukset)

    # hyväksytyt_suoritukset = list(hyväksytyt_suoritukset)
    hyväksytyt_lista = list(hyväksytyt_suoritukset)

    return hyväksytyt_lista







def suoritus_arvosanalla(suoritukset: list, arvosana: int):

    arvosanalla_suoritetut = filter(lambda suoritus: suoritus.arvosana == arvosana, suoritukset)     #  This how it goes. Lambda, funktion sisään

    return arvosanalla_suoritetut


# print("JA HEFITO PAPITO AINOA JOKA TÄYTTÄÄ ODOTUKSET JA VAATIMUKSETTTTT MHMMMHMHMHMMM MASSIMOOO")
# välitulostus()



def kurssin_suorittajat(suoritukset: list, kurssi: str):

    kurssin_suorittaneet = filter(lambda suoritus: suoritus.kurssi == kurssi and suoritus.arvosana > 0, suoritukset)

    kurssin_suorittaneitten_nimet = list(map(lambda suorittaja: suorittaja.opiskelijan_nimi, kurssin_suorittaneet))

    kurssin_suorittaneitten_nimet.sort()

    return kurssin_suorittaneitten_nimet



if __name__ == "__main__":

    s1 = Suoritus("Hefito Papito", "Kohtuporaus ja klitoriksen stimulaatio", 1000)
    s2 = Suoritus("Late Latistunut", "Simppaus ja twitch donatet", 5)
    s3 = Suoritus("Late Latistunut", "elämänhallinta ja itsekunnioitus", 0)
    
    suoritukset =  [s1,s2,s3]

    # for suoritus in hyvaksytyt(suoritukset):
    #     print(suoritus)


    

    # for suoritus in kurssin_suorittajat([s1, s2, s3], "Tietoliikenteen perusteet"):
    #     print(suoritus)