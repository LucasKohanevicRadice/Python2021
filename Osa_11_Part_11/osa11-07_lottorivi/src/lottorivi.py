# TEE RATKAISUSI TÄHÄN:
class Lottorivi():

    def __init__(self, kierrosnumero: int, lottonumerot: list) -> None:

        if len(lottonumerot) != 7:
            raise ValueError("Lottonumeroita pitää olla 7 kpl")
            


        self.__kierrosnumero = kierrosnumero
        self.__lottonumerot = lottonumerot
        

    def osumien_maara(self, pelattu_rivi: list):

        # return []
        return sum([pelattu_rivi.count(osuma) for osuma in pelattu_rivi if osuma in self.__lottonumerot])
    


    def osumat_paikoillaan(self, pelattu_rivi):

        # return [pelattu_rivi for indeksi ,numero in enumerate(pelattu_rivi) if pelattu_rivi[indeksi] != self.__lottonumerot[indeksi] ]
        return [pelattu_rivi[indeksi] if pelattu_rivi[indeksi] in self.__lottonumerot else -1 for indeksi, numero in enumerate(pelattu_rivi)]

if __name__ == "__main__":
    oikea = Lottorivi(5, [1,2,3,4,5,6,7])
    oma_rivi = [1,4,7,11,13,19,24]

    print(oikea.osumien_maara(oma_rivi))
    print(oikea.osumat_paikoillaan(oma_rivi))
    #   Katos vittu onnistu ku onnistuki, tai ainaki niitten numeroitten iterointi, summaa ei saatu vielä. Kokeillaas... jaa ei oikeen onnistu
