# TEE RATKAISUSI TÄHÄN:




import pygame

pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))


robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()

# kerroin = 1

for i in range(0,10):

    naytto.blit(robo,((i+1)*robo_leveys ,robo_korkeus))

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

#   UNGHHHH WE GOOOOD



