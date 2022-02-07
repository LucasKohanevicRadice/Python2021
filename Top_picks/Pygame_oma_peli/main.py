# TEE PELI TÄHÄN

# from curses import KEY_DOWN
from sre_constants import ANY, ANY_ALL
from winreg import KEY_ALL_ACCESS
import pygame
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP
import random
import math

class hirvio:

    def __init__(self) -> None:

        self.hirvio = pygame.image.load("Top_picks\Pygame_oma_peli\images\monstis.png")
        self.lattia = pygame.image.load("Top_picks\Pygame_oma_peli\images\lattia.png")

        self.naytonkorkeus = self.lattia.get_height()*20
        self.naytonleveys = self.lattia.get_width()*20

        self.hirvio_x = 0
        self.hirvio_y = 0
        self.hirvio_kulma = 0

        self.hirvio_leveys = self.hirvio_x + self.hirvio.get_width()
        self.hirvio_korkeus = self.hirvio_y + self.hirvio.get_height()

        self.suuntax_vaihtoehdot = [-2,2]
        self.suuntay_vaihtoehdot = [-2.5, 2.5]

        self.suuntax = random.choice(self.suuntax_vaihtoehdot)
        self.suuntay = random.choice(self.suuntay_vaihtoehdot)

        pass
    
    def aseta_hirvion_x_y_ja_kulma(self, kulma):

        self.hirvio_x = (naytonleveys/2)+math.cos(kulma)*300-self.hirvio.get_width()/2
        self.hirvio_y = (naytonkorkeus/2)+math.sin(kulma)*300-self.hirvio.get_height()/2
        self.hirvio_kulma = kulma



# Luodaan olio joilla määrittää näytönleveys ja näytönkorkeus

hirvi = hirvio()
naytonleveys = hirvi.naytonleveys
naytonkorkeus = hirvi.naytonkorkeus


# Luodaan hirviö-oliot

hirvi1 = hirvio()
hirvi2 = hirvio()
hirvi3 = hirvio()
hirvi4 = hirvio()
hirvi5 = hirvio()
hirvi6 = hirvio()
hirvi7 = hirvio()
hirvi8 = hirvio()
hirvi9 = hirvio()
hirvi10 = hirvio()

# Määrittää käytettävät kulmat aloitusympyrässä

kulma = 0.628
kulma2 = 1.256
kulma3 = 1.884
kulma4 = 2.512
kulma5 = 3.14
kulma6 = 3.768
kulma7 = 4.396
kulma8 = 5.024
kulma9 = 5.652
kulma10 = 6.28

# Asettaa hirviön omalle paikalleen aloitusympyrässä, perustuen hirviölle asetetun "kulma"- arvon mukaan.

hirvi1.aseta_hirvion_x_y_ja_kulma(kulma)
hirvi2.aseta_hirvion_x_y_ja_kulma(kulma2)
hirvi3.aseta_hirvion_x_y_ja_kulma(kulma3)
hirvi4.aseta_hirvion_x_y_ja_kulma(kulma4)
hirvi5.aseta_hirvion_x_y_ja_kulma(kulma5)
hirvi6.aseta_hirvion_x_y_ja_kulma(kulma6)
hirvi7.aseta_hirvion_x_y_ja_kulma(kulma7)
hirvi8.aseta_hirvion_x_y_ja_kulma(kulma8)
hirvi9.aseta_hirvion_x_y_ja_kulma(kulma9)
hirvi10.aseta_hirvion_x_y_ja_kulma(kulma10)

# Hirviöt asetettu listaan.

hirviolista = [hirvi1,hirvi2,hirvi3,hirvi4,hirvi5,hirvi6,hirvi7,hirvi8,hirvi9,hirvi10]

class KymmenenHirviota:

    def __init__(self):

        # Käynnistä PyGame
        pygame.init()

        # Lataa kuvat tiedostoista
        self.lataa_kuvat()

        # Tee oliot haetuista kuvista.
        self.lattia = self.kuvat["lattia"]
        self.pelaaja = self.kuvat["kohderobo"]
        self.kolikko = self.kuvat["kolikko"]
        self.hirvio = self.kuvat["miniMonstro"]
        

        self.pelaajan_liikutus_maara = 2

        self.ylös = False
        self.alas = False
        self.vasemmalle = False
        self.oikealle = False

        self.naytonkorkeus = self.lattia.get_height()*20
        self.naytonleveys = self.lattia.get_width()*20

        self.naytto = pygame.display.set_mode((self.lattia.get_width()*20, self.lattia.get_height()*20))

        self.pelaaja_Y = self.naytonkorkeus//2
        self.pelaaja_X = self.naytonleveys//2

        self.pelaaja_leveys = self.pelaaja_X + self.pelaaja.get_width()
        self.pelaaja_korkeys = self.pelaaja_Y + self.pelaaja.get_height()

        self.kolikko_X = random.randint(0, self.naytonleveys - self.kolikko.get_width()*2)
        self.kolikko_Y = random.randint(0 + self.kolikko.get_height()*2, self.naytonkorkeus-self.kolikko.get_height()*2)

        self.kello = pygame.time.Clock()

        
        self.pisteet = 0

        self.peli_kaynnissa = False

        self.havio = False


        self.fontti = pygame.font.SysFont("Arial", 30)

        pygame.display.set_caption("MonsterMayhem")

        self.silmukka()

    
    def aloitus_teksti(self): # Poissa käytöstä at, kunnes saadaan toimimaan-

        if self.peli_kaynnissa == False:

            fontti = self.fontti
            pelataanko_teksti = fontti.render("Press any key to begin", True, (255,0,0))
            self.naytto.blit(pelataanko_teksti, (350,350))
        
        else:
            pass



    def onko_peli_käynnissä(self, hirviot: list): # Poissa käytöstä atm kunnes saadaan toimimaan

        if self.peli_kaynnissa == False:

            self.pelaajan_liikutus_maara = 0

            for hirvio in hirviot:
                hirvio.suuntax = 0
                hirvio.suuntay = 0
    
        elif self.peli_kaynnissa == True:

            self.pelaajan_liikutus_maara = 2

            for hirvio in hirviot:

                hirvio.suuntax = random.choice(self.suuntax_vaihtoehdot)
                hirvio.suuntay = random.choice(self.suuntay_vaihtoehdot)



    def spawnaa_kolikko(self):

        if self.pelaaja_X + self.pelaaja.get_width() in range(self.kolikko_X, self.kolikko_X + self.kolikko.get_width()+48) and self.pelaaja_Y + self.pelaaja.get_height() in range(self.kolikko_Y, self.kolikko_Y + self.kolikko.get_height()+48):

            self.kolikko_X = random.randint(0, self.naytonleveys - self.kolikko.get_width())
            self.kolikko_Y = random.randint(0 + self.kolikko.get_height(), self.naytonkorkeus)

            self.pisteet += 1
            print(f"Kolikko saatu, kolikoitten määrä on {self.pisteet}")

            self.naytto.blit(self.kolikko, (self.kolikko_X, self.kolikko_Y))
        

        else:
            self.naytto.blit(self.kolikko, (self.kolikko_X, self.kolikko_Y))


    def spawnaa_hirviot(self, hirviot: list):


        for hirvio in hirviot:
            self.naytto.blit(hirvio.hirvio, (hirvio.hirvio_x, hirvio.hirvio_y))


    def häviö(self, hirviot: list):

        if self.havio == True:

            self.pelaajan_liikutus_maara = 0
            

        for hirvio in hirviot:

            pyoristetty_hirvio_x = round(hirvio.hirvio_x) # Hirviön X pitää pyöristää kokonaisluvuksi, koska in range funktio ei pysty ottamaan floatteja parametriksi
            pyoristetty_hirvio_y = round(hirvio.hirvio_y)

            # Ehtoalauseet tarkistamaan osuuko robotti hirviöihin

            if self.pelaaja_X in range(pyoristetty_hirvio_x-5, (pyoristetty_hirvio_x + hirvio.hirvio.get_width())) and self.pelaaja_Y in range(pyoristetty_hirvio_y-5, (pyoristetty_hirvio_y + hirvio.hirvio.get_height()+5)):
                self.havio = True

            elif (self.pelaaja_X-5 + self.pelaaja.get_width()+5) in range(pyoristetty_hirvio_x, (pyoristetty_hirvio_x + hirvio.hirvio.get_width())) and (self.pelaaja_Y-5 + self.pelaaja.get_height()+5) in range(pyoristetty_hirvio_y-5, (pyoristetty_hirvio_y + hirvio.hirvio.get_height())):
                self.havio = True



    
    def tekstit(self):

        fontti = self.fontti

        if self.havio == True:

            häviöteksti = fontti.render(f"You managed to collect {self.pisteet} coins before meeting your demise", True, (255,0,0))
            pelataanko_uudestaan_teksti = fontti.render("Press SPACE to try again?", True, (255,0,0))

            self.naytto.blit(häviöteksti, (175, 300))
            # self.naytto.blit(pelataanko_uudestaan_teksti, (350,350)) # Poissa käytöstä, kunnes uudestaan aloitus ominaisuus saadaan toimimaan
        

        else:
            piste_teksti = fontti.render(f"Coins collected: {self.pisteet}", True, (255,0,0))
            self.naytto.blit(piste_teksti, (20, 20))


        
    def liikuta_hirviota(self, hirvio):

        hirvio.hirvio_x += hirvio.suuntax
        hirvio.hirvio_y += hirvio.suuntay


        if hirvio.hirvio_y + hirvio.hirvio.get_height() >= self.naytonkorkeus:

            hirvio.suuntax = hirvio.suuntax 
            hirvio.suuntay = -hirvio.suuntay 
        
        if hirvio.hirvio_x + hirvio.hirvio.get_width() >= self.naytonleveys:
            hirvio.suuntax = -hirvio.suuntax
            hirvio.suuntay = hirvio.suuntay
        
        if hirvio.hirvio_y + hirvio.hirvio.get_height() <= hirvio.hirvio.get_height() + 15:
            hirvio.suuntax = hirvio.suuntax
            hirvio.suuntay = -hirvio.suuntay
        
        if hirvio.hirvio_x + hirvio.hirvio.get_width() <= hirvio.hirvio.get_width() + 15:
            hirvio.suuntax = -hirvio.suuntax
            hirvio.suuntay = hirvio.suuntay





    def piirra_naytto(self):

        self.naytto.fill((0,0,0)) # Muuttaa näytön värin mustaksi
        self.naytto.blit(self.pelaaja, (self.pelaaja_X, self.pelaaja_Y))
  



    def lataa_kuvat(self):

        self.kuvat = {}

        kuvat = ["hirvio", "kohde", "kohderobo", "kolikko", "laatikko", "lattia", "ovi", "robo", "seina", "miniMonstro"]

        rootPath = "Top_picks/Pygame_oma_peli/images/"

        for nimi in kuvat:
            self.kuvat[nimi] = pygame.image.load(rootPath + nimi + ".png")
    



    def tutki_tapahtumat(self):


        for tapahtuma in pygame.event.get():

            if tapahtuma.type == pygame.KEYDOWN:

                # if tapahtuma.key == ANY_ALL:
                #     self.peli_kaynnissa = True

                if tapahtuma.key == K_RIGHT:
                    self.oikealle = True
                
                if tapahtuma.key == K_LEFT:
                    self.vasemmalle = True
                
                if tapahtuma.key == K_UP:
                    self.ylös = True
                
                if tapahtuma.key == K_DOWN:
                    self.alas = True
            
            if tapahtuma.type == pygame.KEYUP:

                if tapahtuma.key == K_RIGHT:
                    self.oikealle = False
                
                if tapahtuma.key == K_LEFT:
                    self.vasemmalle = False
                
                if tapahtuma.key == K_UP:
                    self.ylös = False
                
                if tapahtuma.key == K_DOWN:
                    self.alas = False
            
            if tapahtuma.type == pygame.QUIT:
                exit()

        if self.oikealle and self.pelaaja_X + self.pelaaja.get_width() < self.naytonleveys:
            self.pelaaja_X += self.pelaajan_liikutus_maara
            
        if self.vasemmalle and self.pelaaja_X >= 0:
            self.pelaaja_X -= self.pelaajan_liikutus_maara
            
        if self.ylös and self.pelaaja_Y > 0:
            self.pelaaja_Y -= self.pelaajan_liikutus_maara
            
        if self.alas and self.pelaaja_Y + self.pelaaja.get_height() < self.naytonkorkeus:
            self.pelaaja_Y += self.pelaajan_liikutus_maara
                        

    def silmukka(self):
        while True:

            self.tutki_tapahtumat()
            self.piirra_naytto()    #   pelaaja blitataan täällä
            # self.aloitus_teksti()
            # self.onko_peli_käynnissä(hirviolista)
            self.spawnaa_kolikko()
            self.spawnaa_hirviot(hirviolista)
            self.häviö(hirviolista)
            self.tekstit()
            self.liikuta_hirviota(hirvi1)
            self.liikuta_hirviota(hirvi2)
            self.liikuta_hirviota(hirvi3)
            self.liikuta_hirviota(hirvi4)
            self.liikuta_hirviota(hirvi5)
            self.liikuta_hirviota(hirvi6)
            self.liikuta_hirviota(hirvi7)
            self.liikuta_hirviota(hirvi8)
            self.liikuta_hirviota(hirvi9)
            self.liikuta_hirviota(hirvi10)
            pygame.display.flip()

            self.kello.tick(100)
            
            

peli = KymmenenHirviota()

