# TEE RATKAISUSI TÄHÄN:


import pygame

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")
robo2 = pygame.image.load("robo.png")

x = 0
y = robo.get_height()
suunta = 0.5

x2 = 0
y2 = robo2.get_height()*2
suunta2 = 1

kello = pygame.time.Clock()
kello2 = pygame.time.Clock()


while True:

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    
    naytto.fill((0,0,0))
    naytto.blit(robo, (x,y))
    naytto.blit(robo2, (x2,y2))
    pygame.display.flip()
    kello2.tick(420)
    

    if suunta > 0 and x+robo.get_width() >= 640:
        suunta = -suunta
        x += suunta
           
    elif suunta < 0 and x <= 0:
        suunta = -suunta
        x += suunta
            
    else:
        x += suunta
                 
    if suunta2 > 0 and x2+robo2.get_width() >= 640:
        suunta2 = -suunta2
        x2 += suunta2
        
    elif suunta2 < 0 and x2 <= 0:
        suunta2 = -suunta2
        x2 += suunta2
        
    else:
        x2 += suunta2
        
    
# TOIMII VITTU SAATANA