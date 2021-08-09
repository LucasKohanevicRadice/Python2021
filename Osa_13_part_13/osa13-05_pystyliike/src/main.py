# TEE RATKAISUSI TÄHÄN:


import pygame

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")


x = 0
y = 0

suunta = 1

kello = pygame.time.Clock()

while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.QUIT:
            exit()
    
    naytto.fill((0,0,0))
    naytto.blit(robo, (x,y))
    pygame.display.flip()

    y += suunta

    if suunta > 0 and y+robo.get_height() >= 480:
        suunta = -suunta
    
    if suunta < 0 and y <=0:
        suunta = -suunta

    kello.tick(420)