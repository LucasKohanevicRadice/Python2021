# TEE RATKAISUSI TÄHÄN:

class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta
    


    def suurempi(self, verrattava):

        if self.nelioita > verrattava.nelioita:
            return True
        
        else:
            return False
    

    def hintaero(self, verrattava):

        hintaero = (self.nelioita*self.neliohinta) - (verrattava.nelioita * verrattava.neliohinta)

        if hintaero < 0:
            hintaero = -hintaero
        
        return hintaero
    

    def kalliimpi(self, verrattava):

        if (self.nelioita*self.neliohinta) > (verrattava.nelioita * verrattava.neliohinta):
            return True
        
        else:
            return False

if __name__ == "__main__":
    yksio = Asunto(1,30,100)
    kaksio = Asunto(2,40,100)


    print(yksio.hintaero(kaksio))
            

