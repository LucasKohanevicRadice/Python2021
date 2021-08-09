# TEE RATKAISUSI TÄHÄN:



import pygame
import random

pygame.init()

naytto = pygame.display.set_mode((640,480))

naytto.fill((0,0,0))

kuva = pygame.image.load("robo.png")

kuva_leveys = kuva.get_width()
kuva_korkeus = kuva.get_height()

for i in range(0,1000):

    naytto.blit(kuva,(random.randint(0, 640-kuva_leveys), random.randint(0 , 480-kuva_korkeus)))

pygame.display.flip()

while True:
    
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

