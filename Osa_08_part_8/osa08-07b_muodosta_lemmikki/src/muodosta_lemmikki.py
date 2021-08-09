# Tee ratkaisusi tähän:




class Lemmikki:

    def __init__(self, nimi: str, laji: str, syntymavuosi: int) -> None:

        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi



        pass

def uusi_lemmikki(nimi : str, laji:str, syntymavuosi: int):

    koira = Lemmikki(nimi, laji, syntymavuosi)

    return koira

if __name__ == "__main__":
    uusi_lemmikki("musti", "besserwisser", 1723)



