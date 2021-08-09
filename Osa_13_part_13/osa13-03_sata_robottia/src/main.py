# TEE RATKAISUSI TÄHÄN:


pygame.init()

naytto = pygame.display.set_mode((640,480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))

robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()

rivin_leveys_kerroin = 0
rivin_leveys_circulating = 1
rivin_korkeus_kerroin = 1

for i in range(0,100):

    naytto.blit(robo,((rivin_leveys_kerroin + rivin_leveys_circulating) * robo_leveys, robo_korkeus*rivin_korkeus_kerroin))
    rivin_leveys_circulating += 0.8

    if i == 9:
        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2
    
    elif i == 19:

        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2
    
    elif i == 29:

        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2
    
    elif i == 39:

        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2      
    
    elif i == 49:

        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2   
    
    elif i == 59:

        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2   

    elif i == 69:

        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2  
    
    elif i == 79:


        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2   
    

    elif i == 89:

        rivin_leveys_circulating = 1
        rivin_leveys_kerroin += 0.2
        rivin_korkeus_kerroin += 0.2   


    # if i in range(0,10):
    #     naytto.blit(robo,((i + rivin_leveys_circulating) * robo_leveys, robo_korkeus*rivin_korkeus_kerroin))

    # elif i in range(11,20):
    #     a += 1
    #     naytto.blit(robo,((i + ) * robo_leveys, robo_korkeus))



pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()


#   IM foken proyd of meself cunt