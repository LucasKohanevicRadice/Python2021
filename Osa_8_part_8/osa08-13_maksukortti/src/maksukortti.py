# Tee ratkaisusi tähän:
class Maksukortti:

    def __init__(self, alkusaldo: float) -> None:

        alkusaldo = float(alkusaldo)
        self.saldo = alkusaldo
    
    def syo_edullisesti(self):
        paskaruoka = 2.60
        if (self.saldo - paskaruoka) < 0:
            pass
        else:
            self.saldo -= paskaruoka
    
    def syo_maukkaasti(self):
        ParasMakuRavintola = 4.60
        if (self.saldo - ParasMakuRavintola) < 0:
            pass
        else:
            self.saldo -= ParasMakuRavintola
        
    def lataa_rahaa(self, rahemäärä: int):
        if rahemäärä < 0:
            raise ValueError("Ois tarkotuksen niiku vittu lataa rahaa eikä pössäyttää sitä tuusan helvettiin vitun apina")
        else:
            self.saldo += rahemäärä
    
    
    def __str__(self) -> str:
        stringitjalas = "{:.1f}".format(self.saldo)
        return f"Kortilla on rahaa {stringitjalas} euroa"
        pass
    

saldo = Maksukortti(50)


Pekan_kortti = Maksukortti(20)
Matin_kortti = Maksukortti(30)
Pekan_kortti.syo_maukkaasti()
Matin_kortti.syo_edullisesti()
print(f"Pekka: {Pekan_kortti} ")
print(f"Matti: {Matin_kortti}")
Pekan_kortti.lataa_rahaa(20)
Matin_kortti.syo_maukkaasti()
print(f"Pekka: {Pekan_kortti}")
print(f"Matti: {Matin_kortti} ")
Pekan_kortti.syo_edullisesti()
Pekan_kortti.syo_edullisesti()
Matin_kortti.lataa_rahaa(50)
print(f"Pekka: {Pekan_kortti}")
print(f"Matti: {Matin_kortti} ")



