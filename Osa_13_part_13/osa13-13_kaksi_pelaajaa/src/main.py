# TEE RATKAISUSI TÄHÄN:

import pygame
from pygame.constants import BUTTON_X1, KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo1 = pygame.image.load("robo.png")
robo2 = pygame.image.load("robo.png")

x1 = 320-robo1.get_width()
y1 = 240

x2 = 320+robo2.get_width()
y2 = 240

oikealle1 = False
vasemmalle1 = False
ylös1 = False
alas1 = False

oikealle2 = False
vasemmalle2 = False
ylös2 = False
alas2 = False

kello = pygame.time.Clock()


while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.KEYDOWN:

            if tapahtuma.key == pygame.K_RIGHT:
                oikealle1 = True
            
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle1 = True
            
            if tapahtuma.key == pygame.K_UP:
                ylös1 = True
            
            if tapahtuma.key == pygame.K_DOWN:
                alas1 = True
            
            if tapahtuma.key == pygame.K_d:
                oikealle2 = True
            
            if tapahtuma.key == pygame.K_a:
                vasemmalle2 = True
            
            if tapahtuma.key == pygame.K_s:
                alas2 = True
            
            if tapahtuma.key == pygame.K_w:
                ylös2 = True

        if tapahtuma.type == pygame.KEYUP:

            if tapahtuma.key == pygame.K_RIGHT:
                oikealle1 = False
            
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle1 = False
            
            if tapahtuma.key == pygame.K_UP:
                ylös1 = False
            
            if tapahtuma.key == pygame.K_DOWN:
                alas1 = False
            
            if tapahtuma.key == pygame.K_d:
                oikealle2 = False
            
            if tapahtuma.key == pygame.K_a:
                vasemmalle2 = False
            
            if tapahtuma.key == pygame.K_s:
                alas2 = False
            
            if tapahtuma.key == pygame.K_w:
                ylös2 = False
        

        if tapahtuma.type == pygame.QUIT:
            exit()
        

    if oikealle1 and x1+robo1.get_width() < 640:
        x1 += 2
    
    if vasemmalle1 and x1 >= 0:
        x1 -= 2
    
    if ylös1 and y1 > 0:
        y1 -= 2
    
    if alas1 and y1+robo1.get_height() < 480:
        y1 += 2
        


    if oikealle2 and x2+robo2.get_width() < 640:
        x2 += 2
    
    if vasemmalle2 and x2 >= 0:
        x2 -= 2
    
    if ylös2 and y2 > 0:
        y2 -= 2
    
    if alas2 and y2+robo2.get_height() < 480:
        y2 += 2
        

    naytto.fill((0,0,0))

    naytto.blit(robo1, (x1,y1))
    naytto.blit(robo2, (x2,y2))

    pygame.display.flip()

    kello.tick(200)




#   Good riddance m8
    
    


