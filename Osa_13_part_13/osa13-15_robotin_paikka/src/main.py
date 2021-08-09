# TEE RATKAISUSI TÄHÄN:

import pygame
import random

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")

kello = pygame.time.Clock()

robo_x = random.randint(0, 640-robo.get_width())
robo_y = random.randint(0, 480-robo.get_height())


while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:

            klikkaus_x = tapahtuma.pos[0]-robo.get_width()/2
            klikkaus_y = tapahtuma.pos[1]-robo.get_height()/2

            print(tapahtuma.pos)
            print(robo_x, robo_y)

            if klikkaus_x in range(robo_x-20, robo_x+20) and klikkaus_y in range(robo_y-45, robo_y+42):
                robo_x = random.randint(0, 640-robo.get_width())
                robo_y = random.randint(0, 480-robo.get_height())
        
        if tapahtuma.type == pygame.QUIT:
            exit()
    
    naytto.fill((0,0,0))
    naytto.blit(robo,(robo_x,robo_y))
    pygame.display.flip()
    kello.tick(100)
            
