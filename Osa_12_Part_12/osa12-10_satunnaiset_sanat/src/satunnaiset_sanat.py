# TEE RATKAISUSI TÄHÄN:

import random
import string


def sanageneraattori(kirjaimet: str, pituus: int, maara: int):


    sana = ""

    laskuri = 1

    while laskuri <= maara:

        for i in range(pituus):
            sana += random.choice(kirjaimet)
            if len(sana) == pituus:
                yield sana
                sana = ""
                laskuri += 1
                
if __name__ == "__main__":
    enkun_aakkoset = string.ascii_lowercase

    satun_sanat = sanageneraattori(string.ascii_lowercase,6,7)

    for sana in satun_sanat:
        print(sana)


