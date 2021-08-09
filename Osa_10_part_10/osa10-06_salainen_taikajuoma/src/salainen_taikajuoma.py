# TEE RATKAISUSI TÄHÄN:
class Taikajuoma:
    def __init__(self, nimi: str):
        self._nimi = nimi
        self._ainekset = []

    def lisaa_aines(self, ainesosa: str, maara: float):
        self._ainekset.append((ainesosa, maara))

    def tulosta_resepti(self):
        print(self._nimi + ":")
        for aines in self._ainekset:
            print(f"{aines[0]} {aines[1]} grammaa")

class SalainenTaikaJuoma(Taikajuoma):

    def __init__(self, nimi: str, salasana: str):

        super().__init__(nimi)
        self.__salasana = salasana

    def lisaa_aines(self, ainesosa: str, maara: float, salasana: str):
        
        if salasana != self.__salasana:
            raise ValueError ("SAAAAATANAN NULIKKA EMÄSNUSSIJA NYT KURKISTIT VÄÄRÄN NOIDAN KEITOKSIIN KJÄÄÄÄÄHÄHÄHÄ")
        
        else:
            # ainekset_ja_maarat = [ainesosa, maara]
            self._ainekset.append(ainesosa + " " + str(maara))
    
    def tulosta_resepti(self, salasana: str):

        if salasana != self.__salasana:
            raise ValueError("SAAAATANAN EMÄSNUSSIJA AI ETTÄ YRITIT KURKISTELLA NOITA-AKAN KEITTOKIRJAAN??!? HÄÄÄÄHÄHÄ LIPASEPPAS VÄHÄN RÖNTTÖSTÄ")
        
        else:
            print(self._nimi)
            for ainekset in self._ainekset:
                print(ainekset, "grammaa")


kutistus = SalainenTaikaJuoma("Kutistus maksimus", "hokkuspokkus")
kutistus.lisaa_aines("Kärpässieni", 1.5, "hokkuspokkus")
kutistus.lisaa_aines("Taikahiekka", 3.0, "hokkuspokkus")
kutistus.lisaa_aines("Sammakonkutu", 4.0, "hokkuspokkus")
kutistus.tulosta_resepti("hokkuspokkus")

kutistus.tulosta_resepti("JEEEKULISPEEKULIS")

