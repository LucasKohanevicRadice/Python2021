# TEE PELI TÄHÄN

import pygame
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP
import random
import math

class hirvio:

    def __init__(self) -> None:

        self.hirvio = pygame.image.load("hirvio.png")
        self.lattia = pygame.image.load("lattia.png")

        self.naytonkorkeus = self.lattia.get_height()*20
        self.naytonleveys = self.lattia.get_width()*20

        self.hirvio_x = 0
        self.hirvio_y = 0
        self.hirvio_kulma = 0

        self.suuntax_vaihtoehdot = [-2,2]
        self.suuntay_vaihtoehdot = [-2.5, 2.5]

        self.suuntax = random.choice(self.suuntax_vaihtoehdot)
        self.suuntay = random.choice(self.suuntay_vaihtoehdot)

        pass
    
    def aseta_hirvion_x_y_ja_kulma(self, kulma):

        self.hirvio_x = (naytonleveys/2)+math.cos(kulma)*300-self.hirvio.get_width()/2
        self.hirvio_y = (naytonkorkeus/2)+math.sin(kulma)*300-self.hirvio.get_height()/2
        self.hirvio_kulma = kulma



hirvi = hirvio()
naytonleveys = hirvi.naytonleveys
naytonkorkeus = hirvi.naytonkorkeus

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

hirviolista = [hirvi1,hirvi2,hirvi3,hirvi4,hirvi5,hirvi6,hirvi7,hirvi8,hirvi9,hirvi10]

class KymmenenHirviota:

    def __init__(self):

        pygame.init()
        self.lataa_kuvat()
        self.lattia = self.kuvat["lattia"]
        self.pelaaja = self.kuvat["kohderobo"]
        self.kolikko = self.kuvat["kolikko"]
        self.hirvio = self.kuvat["hirvio"]
        

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
        self.kolikko_X = random.randint(0, self.naytonleveys - self.kolikko.get_width()*2)
        self.kolikko_Y = random.randint(0 + self.kolikko.get_height()*2, self.naytonkorkeus-self.kolikko.get_height()*2)
        # self.hirvio_x = random.randint(0, self.naytonleveys - self.hirvio.get_width())
        # self.hirvio_y = random.randint(0, self.naytonleveys - self.hirvio.get_height())

        self.kello = pygame.time.Clock()

        self.havio = False

        self.pisteet = 0

        self.fontti = pygame.font.SysFont("Arial", 24)

        pygame.display.set_caption("10H")

        self.silmukka()



    def spawnaa_kolikko(self):

        if self.pelaaja_X + self.pelaaja.get_width() in range(self.kolikko_X, self.kolikko_X + self.kolikko.get_width()+48) and self.pelaaja_Y + self.pelaaja.get_height() in range(self.kolikko_Y, self.kolikko_Y + self.kolikko.get_height()+48):

            self.kolikko_X = random.randint(0, self.naytonleveys - self.kolikko.get_width())
            self.kolikko_Y = random.randint(0 + self.kolikko.get_height(), self.naytonkorkeus)

            self.pisteet += 1

            self.naytto.blit(self.kolikko, (self.kolikko_X, self.kolikko_Y))
        

        else:
            self.naytto.blit(self.kolikko, (self.kolikko_X, self.kolikko_Y))
    

    def spawnaa_hirviot(self, hirviot: list):


        for hirvio in hirviot:
            self.naytto.blit(hirvio.hirvio, (hirvio.hirvio_x, hirvio.hirvio_y))
    

    def häviö(self, hirviot):

        for hirvio in hirviot:
            if self.pelaaja_X + self.pelaaja.get_width() in range(hirvio.hirvio_x, hirvio.hirvio_x + hirvio.get_width()) and self.pelaaja_Y in range(hirvio.hirvio_y, hirvio.hirvio_y + hirvio.get_height()):

                self.pelaajan_liikutus_maara = 0 #  Pelaaja ei pysty liikkumaan
                hirvio.suuntax = 0  #   Hirviön x-akselin suuntainen liike nollaantuu
                hirvio.suuntay = 0  #   Hirviön y-akselin suuntainen liike nollaantuu

                self.havio = True


    
    def hävio_tekstit(self):

        häviöteksti = self.fontti.render("Jouduit hirviön runtelemaksi", True, (255,0,0))
        kolikkojenmäärä = self.fontti.render(f"Sait kerättyä {self.pisteet} kolikkoa", True (255,0,0))
        uusiyritys = self.fontti.render("Paina välilyöntiä yrittääksesi uudestaan tai 'esc' luovuttaaksesi.")

        if self.havio == True:

            self.naytto.blit(häviöteksti, (self.lattia*8, self.lattia*8))
            self.naytto.blit(kolikkojenmäärä, (self.lattia*8, self.lattia*9))
            self.naytto.blit(uusiyritys, (self.lattia*8, self.lattia*10))
    

    def pelataanko_uudestaan(self, hirviot: list):
        

        if self.havio == True:

            for tapahtuma in pygame.event.get():

                if tapahtuma.type == pygame.KEYDOWN:

                    if tapahtuma.key == K_SPACE:

                        self.pelaajan_liikutus_maara = 2
                        self.pisteet = 0
                        self.havio = False
                        self.pelaaja_Y = self.naytonkorkeus//2
                        self.pelaaja_X = self.naytonleveys//2
                        self.spawnaa_kolikko()
                        self.spawnaa_hirviot()

                        for hirvio in hirviot:
                            hirvio.suuntax = random.choice(hirvio.suuntax_vaihtoehdot)
                            hirvio.suuntay = random.choice(hirvio.suuntay_vaihtoehdot)
                    
                    if tapahtuma.key == K_ESCAPE:
                        exit()
                
                if tapahtuma.type == pygame.QUIT:
                    exit()
        





        
    def liikuta_hirviota(self, hirvio):

        # hirvio_y = hirvio.hirvio_y
        # hirvio_x = hirvio.hirvio_x
        # hirvio = hirvio.hirvio
        # suuntax = hirvio.suuntax
        # suuntay = hirvio.suuntay

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

        self.naytto.fill((200,0,0))
        self.naytto.blit(self.pelaaja, (self.pelaaja_X, self.pelaaja_Y))


        # Tuo hirviöt
        # Tuo kolikko




    def lataa_kuvat(self):

        self.kuvat = {}

        kuvat = ["hirvio", "kohde", "kohderobo", "kolikko", "laatikko", "lattia", "ovi", "robo", "seina"]

        for nimi in kuvat:
            self.kuvat[nimi] = pygame.image.load(nimi + ".png")
    



    def tutki_tapahtumat(self):


        for tapahtuma in pygame.event.get():

            if tapahtuma.type == pygame.KEYDOWN:

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
            # self.häviö(hirviolista)
            # self.hävio_tekstit()
            self.tutki_tapahtumat()
            self.piirra_naytto()    #   pelaaja blitataan täällä
            self.spawnaa_kolikko()
            self.spawnaa_hirviot(hirviolista)
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


# pygame.init()

# naytto = pygame.display.set_mode((640,480))

# naytto.fill((0,0,0))

# kuva = pygame.image.load("kohderobo.png")

# kuva_leveys = kuva.get_width()
# kuva_korkeus = kuva.get_height()

# for i in range(0,1000):

#     naytto.blit(kuva,(random.randint(0, 640-kuva_leveys), random.randint(0 , 480-kuva_korkeus)))

# pygame.display.flip()

# while True:
    
#     for tapahtuma in pygame.event.get():
#         if tapahtuma.type == pygame.QUIT:
#             exit()

