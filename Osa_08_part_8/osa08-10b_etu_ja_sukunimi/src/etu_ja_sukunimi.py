# Tee ratkaisusi tähän:

class Henkilo:

    def __init__(self, nimi: str) -> None:

        self.nimi = nimi

    def anna_etunimi(self):

        nimi = self.nimi.split(" ")
        etunimi = nimi[0]
        return etunimi
    
    def anna_sukunimi(self):

        nimi = self.nimi.split(" ")
        sukunimi = nimi[1]
        return sukunimi

if __name__ == "__main__":
    lucas = Henkilo("Lucas Lurkkinen")
    print(lucas.anna_etunimi())
    print(lucas.anna_sukunimi())













