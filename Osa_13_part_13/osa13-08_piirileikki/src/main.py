# TEE RATKAISUSI TÄHÄN:


import pygame
import math

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")

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

kello = pygame.time.Clock()

while True:

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    
    x = 320+math.cos(kulma)*140-robo.get_width()/2
    y = 240+math.sin(kulma)*140-robo.get_height()/2
    x2 = 320+math.cos(kulma2)*140-robo.get_width()/2
    y2 = 240+math.sin(kulma2)*140-robo.get_height()/2
    x3 = (320)+math.cos(kulma3)*140-robo.get_width()/2
    y3 = (240)+math.sin(kulma3)*140-robo.get_height()/2
    x4 = (320)+math.cos(kulma4)*140-robo.get_width()/2
    y4 = (240)+math.sin(kulma4)*140-robo.get_height()/2
    x5 = (320)+math.cos(kulma5)*140-robo.get_width()/2
    y5 = (240)+math.sin(kulma5)*140-robo.get_height()/2
    x6 = (320)+math.cos(kulma6)*140-robo.get_width()/2
    y6 = (240)+math.sin(kulma6)*140-robo.get_height()/2
    x7 = (320)+math.cos(kulma7)*140-robo.get_width()/2
    y7 = (240)+math.sin(kulma7)*140-robo.get_height()/2
    x8 = (320)+math.cos(kulma8)*140-robo.get_width()/2
    y8 = (240)+math.sin(kulma8)*140-robo.get_height()/2
    x9 = (320)+math.cos(kulma9)*140-robo.get_width()/2
    y9 = (240)+math.sin(kulma9)*140-robo.get_height()/2
    x10 = (320)+math.cos(kulma10)*140-robo.get_width()/2
    y10 = (240)+math.sin(kulma10)*140-robo.get_height()/2




    naytto.blit(robo,(x,y))
    naytto.blit(robo, (x2,y2))
    naytto.blit(robo, (x3,y3))
    naytto.blit(robo, (x4,y4))
    naytto.blit(robo, (x5,y5))
    naytto.blit(robo, (x6,y6))
    naytto.blit(robo, (x7,y7))
    naytto.blit(robo, (x8,y8))
    naytto.blit(robo, (x9,y9))
    naytto.blit(robo, (x9,y9))
    naytto.blit(robo, (x10,y10))



    pygame.display.flip()

    kulma += 0.01
    kulma2 += 0.01
    kulma3 += 0.01
    kulma4 += 0.01
    kulma5 += 0.01
    kulma6 += 0.01
    kulma7 += 0.01
    kulma8 += 0.01
    kulma9 += 0.01
    kulma10 += 0.01

    kello.tick(500)



#   Close enough m8