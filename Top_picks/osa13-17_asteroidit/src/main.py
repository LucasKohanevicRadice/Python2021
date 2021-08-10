import pygame
import random
from pygame.constants import K_RIGHT

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")
pisteet = 0

fontti = pygame.font.SysFont("Arial", 24)
pisteteksti = fontti.render(f"Pisteet: {pisteet}", True, (255,0,0))
häviöteksti = fontti.render("You're an absolute fucking disappointment", True, (255,0,0))



asteroidi = pygame.image.load("kivi.png")
asteroidi2 = pygame.image.load("kivi.png")
asteroidi3 = pygame.image.load("kivi.png")
asteroidi4 = pygame.image.load("kivi.png")
asteroidi5 = pygame.image.load("kivi.png")

asteroidivauhti = 1
robovauhti = 6
# asteroidivauhti2 = 1
# asteroidivauhti3 = 1
# asteroidivauhti4 = 1
# asteroidivauhti5 = 1



randomy = [-20,-40,-60,-100,-140,-180,-200]

robo_x = 320
robo_y = 480-robo.get_height()

asteroidi_x = random.randint(0, 480-asteroidi.get_width())
asteroidi_y = random.choice(randomy)
asteroidi_x2 = random.randint(0, 480-asteroidi.get_width())
asteroidi_y2 = random.choice(randomy)
asteroidi_x3 = random.randint(0, 480-asteroidi.get_width())
asteroidi_y3 = random.choice(randomy)
asteroidi_x4 = random.randint(0, 480-asteroidi.get_width())
asteroidi_y4 = random.choice(randomy)
asteroidi_x5 = random.randint(0, 480-asteroidi.get_width())
asteroidi_y5 = random.choice(randomy)

kello = pygame.time.Clock()

oikealle = False
vasemmalle = False




while True:


    for tapahtuma in pygame.event.get():

        # naytto.blit(asteroidi, (asteroidi_x,asteroidi_y))

        if tapahtuma.type == pygame.KEYDOWN:

            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
            
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
        
        if tapahtuma.type == pygame.KEYUP:

            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
            
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
        
        if tapahtuma.type == pygame.QUIT:
            exit()

    if oikealle and robo_x+robo.get_width() < 640:
        robo_x += robovauhti
    
    if vasemmalle and robo_x >= 0:
        robo_x -= robovauhti

    naytto.fill((0,0,0))

    naytto.blit(pisteteksti,(550, 20))
    naytto.blit(robo, (robo_x,robo_y))

    naytto.blit(asteroidi, (asteroidi_x,asteroidi_y))
    naytto.blit(asteroidi2, (asteroidi_x2,asteroidi_y2))
    naytto.blit(asteroidi3, (asteroidi_x3,asteroidi_y3))
    naytto.blit(asteroidi4, (asteroidi_x4,asteroidi_y4))
    naytto.blit(asteroidi5, (asteroidi_x5,asteroidi_y5))

    asteroidi_y += asteroidivauhti
    asteroidi_y2 += asteroidivauhti
    asteroidi_y3 += asteroidivauhti
    asteroidi_y4 += asteroidivauhti
    asteroidi_y5 += asteroidivauhti

    
    if asteroidi_y in range(robo_y, robo_y + robo.get_height()+100) and asteroidi_x in range(robo_x-25, robo_x + 25):

        asteroidi_x = random.randint(0, 480-asteroidi.get_width())
        asteroidi_y = random.choice(randomy)
        pisteet += 1
        pisteteksti = fontti.render(f"Pisteet: {pisteet}", True, (255,0,0))
    
    elif asteroidi_y >= 480:
        
        naytto.blit(häviöteksti,(600, 240))
        asteroidi_y  = -50
        asteroidivauhti = 0
        robovauhti = 0
        
    
    if asteroidi_y2 in range(robo_y, robo_y + robo.get_height()+100) and asteroidi_x2 in range(robo_x-25, robo_x + 25):

        asteroidi_x2 = random.randint(0, 480-asteroidi.get_width())
        asteroidi_y2 = random.choice(randomy)
        pisteet += 1
        pisteteksti = fontti.render(f"Pisteet: {pisteet}", True, (255,0,0))
    
    elif asteroidi_y2 >= 480:
        
        naytto.blit(häviöteksti,(600, 240))
        asteroidi_y2  = -50
        asteroidivauhti = 0
        robovauhti = 0
        
    
    if asteroidi_y3 in range(robo_y, robo_y + robo.get_height()+100) and asteroidi_x3 in range(robo_x-25, robo_x + 25):

        asteroidi_x3 = random.randint(0, 480-asteroidi.get_width())
        asteroidi_y3 = random.choice(randomy)
        pisteet += 1
        pisteteksti = fontti.render(f"Pisteet: {pisteet}", True, (255,0,0))
    
    elif asteroidi_y3 >= 480:
        
        naytto.blit(häviöteksti,(600, 240))
        asteroidi_y3  = -50
        asteroidivauhti = 0
        robovauhti = 0
        
    
    if asteroidi_y4 in range(robo_y, robo_y + robo.get_height()+100) and asteroidi_x4 in range(robo_x-25, robo_x + 25):

        asteroidi_x4 = random.randint(0, 480-asteroidi.get_width())
        asteroidi_y4 = random.choice(randomy)
        pisteet += 1
        pisteteksti = fontti.render(f"Pisteet: {pisteet}", True, (255,0,0))
    
    elif asteroidi_y4 >= 480:
        
        naytto.blit(häviöteksti,(600, 240))
        asteroidi_y4  = -50
        asteroidivauhti = 0
        robovauhti = 0
        
    
    if asteroidi_y5 in range(robo_y, robo_y + robo.get_height()+100) and asteroidi_x5 in range(robo_x-25, robo_x + 25):

        asteroidi_x5 = random.randint(0, 480-asteroidi.get_width())
        asteroidi_y5 = random.choice(randomy)
        pisteet += 1
        pisteteksti = fontti.render(f"Pisteet: {pisteet}", True, (255,0,0))
    

    elif asteroidi_y5 >= 480:
        
        naytto.blit(häviöteksti,(600, 240))
        asteroidi_y5  = -50
        asteroidivauhti = 0
        robovauhti = 0
        




    kello.tick(100)

    pygame.display.flip()



    # naytto.blit(roidi, (asteroidi_x,asteroidi_y))
    # asteroidi_x = asteroidi_x
    # asteroidi_y += 2
    # asteroidilista.append(roidi)
    # pygame.display.flip()
    # kello.tick(100)