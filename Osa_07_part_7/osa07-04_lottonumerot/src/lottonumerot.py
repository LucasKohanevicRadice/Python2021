# tee ratkaisu tänne

from random import sample, shuffle


def lottonumerot(maara: int, alaraja: int, ylaraja: int):

    #   Tehdään kaikilla annetuilla esimerkki tyyleillä.

    import random

    #   Tyyli #1, randint ja numeroitten läpikäynti

    # lottonumerot = []

    # for i in range(maara+1):
    #     uusi = random.randint(alaraja, ylaraja)
    #     if uusi not in lottonumerot:
    #         lottonumerot.append(uusi)
    
    # lottonumerot.sort()
    # return lottonumerot


    #   Tyyli #2, shuffle, luodaan ensin lista, jossa luvut alarajasta ylärajaan. Tämän jälkeen numerot sekoitetaan shufflen avulla, ja valitaan seitsemän ensimmäistä numeroa.
    #   Koska numerot ovat nyt sekoittuneet, ovat kaikki valitut numerot periaatteessa satunnaisesti valittuja. Taino satunnaisessa järjestyksessä esiintyviä ainakin. Vitun näsäviisas homo.

    # lottonumerot = list(range(alaraja,ylaraja))
    # shuffle(lottonumerot)
    # lottorivi = lottonumerot[:maara]
    
    # lottorivi.sort()

    # return lottorivi

    #   Tyyli #3, Sample, valitsee annetusta tietorakenteesta halutun määrän satunnaisia alkioita.

    lottonumerot = list(range(alaraja, ylaraja))
    lottorivi = sample(lottonumerot, maara)

    lottorivi.sort()

    return lottorivi
    

if __name__ == "__main__":
    lottonumerot(7,1,40)