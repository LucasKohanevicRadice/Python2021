# TEE RATKAISUSI TÄHÄN:


class Lahja:

    def __init__(self, nimi:str, paino: int):

        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"

class Pakkaus:

    def __init__(self):

        self.paketti = []

        pass

    def lisaa_lahja(self, lahja:Lahja):

        self.paketti.append(lahja)

        pass
    
    def yhteispaino(self):

        self.paino = 0

        for lahja in self.paketti:
            self.paino += lahja.paino
        return self.paino




if __name__ == "__main__":
    kirja = Lahja("Aapiskukko", 2)
    kirja1 = Lahja("piiepo", 3)
    paketti = Pakkaus()
    paketti.lisaa_lahja(kirja)
    print(paketti.yhteispaino())

    print("Lahjan nimi:", kirja.nimi)
    print("Lahjan paino:" ,kirja.paino)
    print("Lahja:", kirja)


