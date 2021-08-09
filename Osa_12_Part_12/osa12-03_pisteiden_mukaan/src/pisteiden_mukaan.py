# TEE RATKAISUSI TÄHÄN:

def jarjesta_pisteiden_mukaan(elokuvat: list):

    jarjestetty_laskevasti_pisteiden_mukaan = []

    def maarittelyehto(pisteet: dict):

        return pisteet["pisteet"]
    
    # elokuvat.sort(key = maarittelyehto, reverse = True )

    for elokuva in elokuvat:
        jarjestetty_laskevasti_pisteiden_mukaan.append(elokuva)
    
    jarjestetty_laskevasti_pisteiden_mukaan.sort(key = maarittelyehto, reverse = True )
    
    return jarjestetty_laskevasti_pisteiden_mukaan

if __name__ == "__main__":
    sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 },  { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }  ]

    for sarja in jarjesta_pisteiden_mukaan(sarjat):
        print(f"{sarja['nimi']} {sarja['pisteet']}")