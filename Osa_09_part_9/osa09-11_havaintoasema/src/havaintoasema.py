# TEE RATKAISUSI TÄHÄN:


class Havaintoasema:

    def __init__(self, nimi) -> None:

        self.__nimi = nimi
        self.__havainnot = []

    def lisaa_havainto(self, havainto: str):

        self.__havainnot.append(havainto)
    

    def viimeisin_havainto(self):

        if len(self.__havainnot) == 0:
            return ""
        else:
            return self.__havainnot[-1]


    
    def havaintojen_maara(self):

        return len(self.__havainnot)
    
    def __str__(self) -> str:

        return f"{self.__nimi}, {len(self.__havainnot)} havaintoa"
        pass
    


if __name__ == "__main__": 
    asema = Havaintoasema("leppävaara")

    asema.lisaa_havainto("Happosadetta")

    asema.lisaa_havainto("With a slight chance of radioactive radiation")

    asema.lisaa_havainto("The toads have developed spines")

    asema.lisaa_havainto("They are walking now")

    asema.lisaa_havainto(" The toads have taken over. They took over all our capitol buildings.\n we've lost all hope... We havent seen a single survivor in months. The only survivors are on the concetration camps run by the toad overlords... \n My wife died yesterday. Im going to kill myself now. I hope there is something better in the afterlife. ")

    print(asema.viimeisin_havainto())

    print(asema)
