# tee ratkaisu tänne

import json

def tulosta_henkilot(tiedosto: str):

    with open(tiedosto) as file:

        data = file.read()
    
    henkilot = json.loads(data)

    for sanakirja in henkilot:

        print(f"{sanakirja['nimi']} {sanakirja['ika']} vuotta ({sanakirja})")



        



tulosta_henkilot("tiedosto1.json")



