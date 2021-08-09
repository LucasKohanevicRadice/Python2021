# Tee ratkaisusi tähän:
class  Lukutilasto:

    def __init__(self):
        self.luvut = []

    def lisaa_luku(self, luku:int):
        self.luvut.append(luku)

    def lukujen_maara(self):

        return len(self.luvut)
    

    def summa(self):

        return sum(self.luvut)
    
    
    def keskiarvo(self):

        if len(self.luvut) == 0:
            return 0
        else:   
            return sum(self.luvut)/len(self.luvut)



print("Anna lukuja: ")
tilasto = Lukutilasto()
parilliset = Lukutilasto()
parittomat = Lukutilasto()


while True:

    syote = int(input(""))

    if syote == -1:

        print(f"Summa: {tilasto.summa()}")
        print(f"Keskiarvo: {tilasto.keskiarvo()}")
        print(f"Parillisten summa: {parilliset.summa()}")
        print(f"Parittomien summa: {parittomat.summa()}")

        break

    else:

        if syote % 2 == 0:
            parilliset.lisaa_luku(syote)
        
        elif syote % 2 != 0:
            parittomat.lisaa_luku(syote)

        tilasto.lisaa_luku(syote)


