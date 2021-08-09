# TEE RATKAISUSI TÄHÄN:

import pygame

pygame.init()

naytto = pygame.display.set_mode((640,480))
robo = pygame.image.load("robo.png")

x = 0
y = 0

suuntax = 1
suuntay = 1

kello = pygame.time.Clock()

while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0,0,0))
    naytto.blit(robo,(x,y))
    pygame.display.flip()
    
    kello.tick(800)

    if x+robo.get_width() <= 640 and y == 0:
        x += 1
 
    if x+robo.get_width() >= 640 and y+robo.get_height() <= 480:
        y += 1
    
    if y+robo.get_height() >= 480: #    Tässä kohtaa robon pitäis alkaa liikkumaan vasemmalleppäin alareunaa pitkin
        x += -1
    
    if y >= 0 and x < 0:
        y += -1
    
    # kello.tick(420)


    

    # if x+robo.get_width() >= 640 and y+robo.get_height() <= 480:
    #     y += 1
    
    # if y+robo.get_height() >= 480: #    Tässä kohtaa robon pitäis alkaa liikkumaan vasemmalleppäin alareunaa pitkin
    #     x += -1
    
    # x += suuntax
    # y += suuntay

    kello.tick(420)