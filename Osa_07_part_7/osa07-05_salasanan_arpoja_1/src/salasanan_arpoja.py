# tee ratkaisu tänne

from random import sample
import random
from string import ascii_letters


def luo_salasana(pituus: int):

    from random import sample
    from string import ascii_letters

    engkirjaimet = ascii_letters.lower()

    salasana = ""

    kirjaimet = random.sample(engkirjaimet,pituus)

    for kirjain in kirjaimet:
        salasana += kirjain

    return salasana
if __name__ == "__main__":
    print(luo_salasana(2))