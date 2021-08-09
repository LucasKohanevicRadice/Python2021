# Tämän osan tehtävissä ei ole automaattisia testejä, vaan testi antaa pisteet
# automaattisesti, kun lähetät ratkaisun palvelimelle. Lähetä ratkaisu vasta
# sitten, kun se on valmis ja vastaa tehtävänannon vaatimuksia. Vaikka tehtävissä
# ei ole testejä, kurssin henkilökunta näkee lähetetyt ratkaisut.

# TEE RATKAISUSI TÄHÄN:

import pygame   #   Tuo pygame moduulin

pygame.init()   #   Käynnistää pygamen

naytto = pygame.display.set_mode((640, 480))    #   Asettaa ikkunan leveyden ja korkeuden pikseleissä

robo = pygame.image.load("robo.png")    #   Lataa annetun kuvan ohjelmaan

naytto.fill((0,0,0))    #   Täyttää näytön annetuilla värikoodeilla

# naytto.blit(robo,(0,0))
# naytto.blit(robo,(300,0))
# naytto.blit(robo,(100,200)) # Tämä toimii, miksei alempi ?

robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()

naytto.blit(robo,(0,0))
naytto.blit(robo,(640-robo_leveys,480-robo_korkeus))
naytto.blit(robo,(630-robo_leveys,0))
naytto.blit(robo,(0,480-robo_korkeus))     #   Lisää robon ikkunaan

pygame.display.flip()   #   Päivittää näytön sisällön

while True:
    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.QUIT:
            exit()