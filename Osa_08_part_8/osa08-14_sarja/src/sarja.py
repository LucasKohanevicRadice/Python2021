# Tee ratkaisusi tähän:
class Sarja():

    def __init__(self, nimi: str, tuottarit_lkm: int, genret: list) -> None:

        self.nimi = nimi
        self.tuottarit_lkm = tuottarit_lkm
        self.genret = genret
        self.arvostelujenmäärä = 0
        self.arvosana = 0

    def arvostele(self, arvosana: int):

        if arvosana in range(0,6):
            self.arvosana += arvosana
            self.arvostelujenmäärä += 1
        else:
            print("Luku on arvosteluasteikon ulkopuolella, yritä uudstaan.")
            pass

    
    def __str__(self) -> str:

        degenreaatio = ", ".join(self.genret)

        if self.arvosana and self.arvostelujenmäärä == 0:
            return f"{self.nimi}({self.tuottarit_lkm} esityskautta)\nGenret: {degenreaatio}\nEi arvosteluja"

        else:
            return f"{self.nimi}({self.tuottarit_lkm} esityskautta)\nGenret: {degenreaatio}\nArvosteluja {self.arvostelujenmäärä}, keskiarvo on {self.arvosana/self.arvostelujenmäärä} pistettä"


        pass



# print(s3)
# for sarja in sarjat:
#     print(sarja)

def arvosana_vahintaan(arvosana:float, sarjat: list):

    for sarja in sarjat:
        if sarja.arvosana >= arvosana:
            print(f"{sarja.nimi}\nhuikeliskuikelis tää kannattaa kattoo\n")

def sisaltaa_genren(genre: str, sarjat:list):
    print(f"Genre {genre}\n")

    for sarja in sarjat:
        if genre in sarja.genret:
            print(f"{sarja.nimi}" )

    print("\n")
        


s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)

s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(4)

s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)

sarjat = [s1, s2, s3]

arvosana_vahintaan(4,sarjat)
sisaltaa_genren("Comedy", sarjat)