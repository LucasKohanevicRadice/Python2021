import pygame
pygame.init()

naytto = pygame.display.set_mode((640,480))
robo = pygame.image.load("robo.png")

robo_x = 0
robo_y = 0
kohde_x = 0
kohde_y = 0

kello = pygame.time.Clock()

while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.MOUSEMOTION:

            kohde_x = tapahtuma.pos[0] - robo.get_width()/2
            kohde_y = tapahtuma.pos[1] - robo.get_height()/2
        
        if tapahtuma.type == pygame.QUIT:
            exit()

             
        
    if robo_x > kohde_x:
        robo_x -= 1
    
    if robo_x < kohde_x:
        robo_x += 1
    
    if robo_y > kohde_y:
        robo_y -= 1
    
    if robo_y < kohde_y:
        robo_y += 1
    
    naytto.fill((0,0,0))
    naytto.blit(robo,(robo_x,robo_y))
    pygame.display.flip()
    
    kello.tick(10000)