# Tee ratkaisusi tähän:

class id:

    id = 0
    
    def kasvata_ja_tuo_id():
        id.id += 1

        return id.id




class Tehtava:


    def __init__(self, kuvaus: str, koodari: str, työmäärä: int,):

        id.kasvata_ja_tuo_id()

        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = työmäärä
        self.__valmis = False
        self.tunniste = id.id
        


    def merkkaa_valmiiksi(self):
        self.__valmis = True
    
    def on_valmis(self):

        if self.__valmis == False:
            return "Ei valmis"

        elif self.__valmis == True:
                return "Valmis"
    
    def __str__(self) -> str:
        return f"{self.tunniste}: {self.kuvaus} (aika-arvio: {self.tyomaara} tuntia), tekijä: {self.koodari}, status: {self.on_valmis()}"



class Tilauskirja:

    def __init__(self) -> None:

        self.__tilauskirja = {}
        self.koodaajat = []
    

    def lisaa_tilaus(self, tehtava: Tehtava):

        self.__tilauskirja[tehtava.tunniste] = f"{tehtava.tunniste}: {tehtava.kuvaus}, aika-arvio: ({tehtava.tyomaara} tuntia), tekijä: {tehtava.koodari}, status: {tehtava.on_valmis()} "
        
        if tehtava.koodari not in self.koodaajat:
            self.koodaajat.append(tehtava.koodari)
    

    # def merkkaa_valmiiksi(self, id: int):
        
    

    def kaikki_tilaukset(self):

        return  [arvo for avain, arvo in self.__tilauskirja.items()]

    def koodarit(self):

        return self.koodaajat
    



        


        
            
            






t1 = Tehtava("mooc tehtävä", "Lucas", 3,)
t1.merkkaa_valmiiksi()
# print(t1.on_valmis())
# print(t1)
t2 = Tehtava("peli", "lawrence", 4)
t3 = Tehtava("God of war", "Lucas", 8000)

# print(id.id)
# print(t1.tunniste)

tilaukset = Tilauskirja()
tilaukset.lisaa_tilaus(t1)
tilaukset.lisaa_tilaus(t2)
tilaukset.lisaa_tilaus(t3)

    
    
for tilaus in tilaukset.kaikki_tilaukset():   
    print(tilaus)

for koodari in tilaukset.koodarit():    
    print(koodari)
