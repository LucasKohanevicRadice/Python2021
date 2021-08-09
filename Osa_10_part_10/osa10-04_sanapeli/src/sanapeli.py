# TEE RATKAISUSI TÄHÄN:
# TEE RATKAISUSI TÄHÄN:
import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):

        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
                print()
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
                print()
            else:
                pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")

class PisinSana(Sanapeli):

    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):       

        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1

        elif len(pelaaja2_sana) > len(pelaaja1_sana):
            return 2
        
        else:
            pass

#   Wöööks

class EnitenVokaaleja(Sanapeli):

    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        vokaalit = "aeiuoyöäå"
        vokaalit_p1 = 0
        vokaalit_p2 = 0

        for kirjain in pelaaja1_sana:
            if kirjain in vokaalit:
                vokaalit_p1 += 1
        
        for kirjain in pelaaja2_sana:
            if kirjain in vokaalit:
                vokaalit_p2 += 1
        
        if vokaalit_p1 > vokaalit_p2:
            return 1
        
        elif vokaalit_p1 < vokaalit_p2:
            return 2

        else:
            pass

#   v = EnitenVokaaleja(2)
#   v.pelaa()
#   foken wööks, kinda clumsy, but wööks. Not polished y' kno

class KiviPaperiSakset(Sanapeli):

    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)
    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):

        p1 = 0
        p2 = 0

        kelvot = ["kivi", "paperi", "sakset"]

        if pelaaja1_sana not in kelvot and pelaaja2_sana in kelvot:
            p2 += 1

        elif pelaaja1_sana in kelvot and pelaaja2_sana not in kelvot:
            p1 += 1
        
        elif pelaaja1_sana not in kelvot and pelaaja2_sana not in kelvot:
            pass
        
        elif pelaaja1_sana == pelaaja2_sana:
            pass
        

        elif pelaaja1_sana in kelvot and pelaaja2_sana in kelvot:

            if pelaaja1_sana == "kivi" and pelaaja2_sana == "sakset":
                p1 += 1
            
            elif pelaaja1_sana == "kivi" and pelaaja2_sana == "paperi":
                p2 += 1
            
            elif pelaaja1_sana == "sakset" and pelaaja2_sana == "paperi":
                p1 += 1
            
            elif pelaaja1_sana == "sakset" and pelaaja2_sana == "kivi":
                p2 += 1
            
            elif pelaaja1_sana == "paperi" and pelaaja2_sana == "kivi":
                p1 += 1
            
            elif pelaaja1_sana == "paperi" and pelaaja2_sana == "sakset":
                p2 += 1
            
            elif pelaaja1_sana == pelaaja2_sana:
                pass


        if p1 > p2:
            return 1
            
        elif p1 < p2:
            return 2

        else:
            pass
    


# p = PisinSana(2)
# p.pelaa()

# v = EnitenVokaaleja(2)
# v.pelaa()

# kps = KiviPaperiSakset(12)
# kps.pelaa()