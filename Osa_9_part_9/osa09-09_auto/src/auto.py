# TEE RATKAISUSI TÄHÄN:



class Auto():

    def __init__(self, bensa: int in range(0,61), kilsat: int) -> None:

        self.__täystankki = 60
        self.__bensa = bensa
        self.__kilsat = kilsat

    def tankkaa(self):
        if self.__bensa == self.__täystankki:
            pass
        else:
            self.__bensa += self.__täystankki - self.__bensa

    def aja(self, km :int):
        
        if km <= self.__bensa:
            self.__bensa -= km
            self.__kilsat += km

        elif km > self.__bensa:
            self.__kilsat += self.__bensa
            self.__bensa -= self.__bensa
            
        
    def __str__(self) -> str:

        return f"Auto: ajettu {self.__kilsat} km, bensaa {self.__bensa}"

        pass

auto = Auto(0,0)

print(auto) #   0 km, 0 l

auto.tankkaa()  

print(auto) #   0 km, 60 l

auto.aja(30)

print(auto) #   30 km, 30 l

auto.tankkaa()

print(auto) #   30 km, 60 l

auto.aja(100)  

print(auto) # 30 km, 0 l ?

