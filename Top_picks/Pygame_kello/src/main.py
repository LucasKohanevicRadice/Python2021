# TEE RATKAISUSI TÄHÄN:

import pygame
import datetime
import math

pygame.init()


nyt = datetime.datetime.now()
sekunnit_nyt = int(nyt.strftime("%S"))
minuutit_nyt = int(nyt.strftime("%M"))
tunnit_nyt =  int(nyt.strftime("%H"))

naytto = pygame.display.set_mode((640,480))

kello = pygame.time.Clock()


kulma_sekuntti = -1.58 + ((sekunnit_nyt/60)*(2*math.pi))
kulma_minuutti = -1.58 + ((minuutit_nyt/60)*(2*math.pi))
kulma_tunti = -1.58 + ((tunnit_nyt/12)*(2*math.pi)) + ((minuutit_nyt/60) * (2*math.pi/12))



while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.QUIT:
            exit()

    aika_nyt = datetime.datetime.now()
    aika_nyt_muotoiltu = aika_nyt.strftime("%H.%M.%S")

    # sekunnit_nyt = int(aika_nyt.strftime("%S"))
    # minuutit_nyt = int(aika_nyt.strftime("%M"))
    # tunnit_nyt =  int(aika_nyt.strftime("%H"))


    naytto.fill((0,0,0))
    pygame.display.set_caption(f"{aika_nyt_muotoiltu}")

    pygame.draw.circle(naytto, (255,0,0), (320,240), 200)
    pygame.draw.circle(naytto, (0,0,0), (320,240), 195)
    pygame.draw.circle(naytto, (255,0,0), (320,240), 10)

    keskipiste_x = 320
    keskipiste_y = 240
    sekuntti_loppu_x = 320+math.cos(kulma_sekuntti)*185
    sekuntti_loppu_y = 240+math.sin(kulma_sekuntti)*185
    minuutti_loppu_x = 320+math.cos(kulma_minuutti)*165
    minuutti_loppu_y = 240+math.sin(kulma_minuutti)*165
    tunti_loppu_x = 320+math.cos(kulma_tunti)*145
    tunti_loppu_y = 240+math.sin(kulma_tunti)*145


    pygame.draw.line(naytto, (255,0,255), (keskipiste_x,keskipiste_y), (sekuntti_loppu_x,sekuntti_loppu_y), 2)
    pygame.draw.line(naytto, (0,0,255), (keskipiste_x,keskipiste_y), (minuutti_loppu_x,minuutti_loppu_y), 4)
    pygame.draw.line(naytto, (255,100,180), (keskipiste_x,keskipiste_y), (tunti_loppu_x,tunti_loppu_y), 8)

    # pygame.draw.line(Surface, color, start_pos, end_pos, width=1)

    kulma_sekuntti += (2*math.pi)/60
    kulma_minuutti += (2*math.pi)/3600
    kulma_tunti += (((2*math.pi)/60)/60)/12

        
    pygame.display.flip()

    kello.tick(1)




