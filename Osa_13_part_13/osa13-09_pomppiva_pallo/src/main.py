# TEE RATKAISUSI TÄHÄN:


import pygame
import math
import random

pygame.init()

naytto = pygame.display.set_mode((640,480))

pallo = pygame.image.load("pallo.png")

# kulma = 0

suuntax_vaihtoehdot = [-1, 1]
suuntay_vaihtoehdot = [-1.25, 1,25]

suuntax = random.choice(suuntax_vaihtoehdot)
suuntay = random.choice(suuntay_vaihtoehdot)

# randomx = []
# randomy = []

# for i in range(10,640-pallo.get_width()):
#     randomx.append(i)

# for i in range(10,480-pallo.get_height()):
#     randomy.append(i)


# x = random.choice(randomx)
# y = random.choice(randomy)

x = random.randint(10, 640-pallo.get_width())
y = random.randint(10, 480-pallo.get_height())



kello = pygame.time.Clock()

while True:

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0,0,0))
    
    naytto.blit(pallo, (x,y))
    pygame.display.flip()

    x += suuntax
    y += suuntay

    if y+pallo.get_height() >= 480:
        suuntax = suuntax
        suuntay = -suuntay
    
    if x+pallo.get_width() >= 640:
        suuntax = -suuntax
        suuntay = suuntay
    
    if y+pallo.get_height() <= 45:
        suuntax = suuntax
        suuntay = -suuntay
    
    if x+pallo.get_width() <= 45:
        suuntax = -suuntax
        suuntay = suuntay

    kello.tick(300)
