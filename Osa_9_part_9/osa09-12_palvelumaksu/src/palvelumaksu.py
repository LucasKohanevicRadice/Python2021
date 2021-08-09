# TEE RATKAISUSI TÄHÄN:


class Pankkitili:

    def __init__(self, omistaja: str, tilinro: str, saldo: float) -> None:

        if saldo < 0:
            raise ValueError("Saldo ei voi olla negatiivinen")
        else:
            self.__omistaja = omistaja
            self.__tilinro = tilinro
            self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo: float):
        if saldo <0:
            raise ValueError("Saldo ei voi olla negatiivinen")
        else:
            self.__saldo = saldo


    
    def __palvelumaksu(self):

        self.__saldo *= 0.99
        pass

    def talleta(self, summa: float):

        if summa > 0:
            self.__saldo += summa
            self.__palvelumaksu()

    def nosta(self, summa: float):

        if summa < self.__saldo:
            self.__saldo -= summa
            self.__palvelumaksu()



if __name__ == "__main__":
    kortti = Pankkitili("Lotta", "FI123466", 476.99)

    print(kortti.saldo)
    kortti.nosta(100)
    print(kortti.saldo)
    kortti.talleta(100)
    print(kortti.saldo)


