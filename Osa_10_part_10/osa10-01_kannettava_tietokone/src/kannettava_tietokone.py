# TEE RATKAISUSI TÄHÄN:
class Tietokone:
    def __init__(self, malli: str, nopeus: int):
        self.__malli = malli
        self.__nopeus = nopeus

    @property
    def malli(self):
        return self.__malli

    @property
    def nopeus(self):
        return self.__nopeus


class KannettavaTietokone(Tietokone):

    def __init__(self, malli: str, nopeus: int, paino:float):
        super().__init__(malli, nopeus)
        self.__paino = paino
     

    
    def __str__(self) -> str:
        return (f"{self.malli}, {self.nopeus} MHz, {self.__paino} kg")
    
if __name__ == "__main__":
    läppäri =  KannettavaTietokone("Lenovo", 6000, 2.4)

    print(läppäri)

