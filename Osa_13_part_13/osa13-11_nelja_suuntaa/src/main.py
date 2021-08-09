# TEE RATKAISUSI TÄHÄN:


import pygame
from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")

x = 320-robo.get_width()
y = 240-robo.get_height()

oikealle = False
vasemmalle = False
ylös = False
alas = False

kello = pygame.time.Clock()


while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.KEYDOWN:

            if tapahtuma.key == K_RIGHT:
                oikealle = True
            
            if tapahtuma.key == K_LEFT:
                vasemmalle = True
            
            if tapahtuma.key == K_UP:
                ylös = True
            
            if tapahtuma.key == K_DOWN:
                alas = True
        
        if tapahtuma.type == pygame.KEYUP:

            if tapahtuma.key == K_RIGHT:
                oikealle = False
            
            if tapahtuma.key == K_LEFT:
                vasemmalle = False
            
            if tapahtuma.key == K_UP:
                ylös = False
            
            if tapahtuma.key == K_DOWN:
                alas = False
        
        if tapahtuma.type == pygame.QUIT:
            exit()
    
    if oikealle and x+robo.get_width() < 640:
        x += 2
    
    if vasemmalle and x >= 0:
        x -= 2
    
    if ylös and y > 0:
        y -= 2
    
    if alas and y+robo.get_height() < 480:
        y += 2
    

    naytto.fill((0,0,0))
    naytto.blit(robo,(x,y))
    pygame.display.flip()
    
    kello.tick(200)

            

