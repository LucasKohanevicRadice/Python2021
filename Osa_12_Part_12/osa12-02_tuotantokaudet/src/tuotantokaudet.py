# TEE RATKAISUSI TÄHÄN:
def jarjesta_tuotantokausien_mukaan(alkiot: list):
    
    jarjestetty_tuotantokausien_mukaan = []

    def tuottarit(sarjat: dict):

        return (sarjat["kausia"])

    # alkiot.sort(key = tuottarit)

    for rivi in alkiot:
        jarjestetty_tuotantokausien_mukaan.append(rivi)
    
    jarjestetty_tuotantokausien_mukaan.sort(key = tuottarit)
    
    return jarjestetty_tuotantokausien_mukaan

if __name__ == "__main__":
    sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 },  { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }  ]

    for sarja in jarjesta_tuotantokausien_mukaan(sarjat):
        print(f"{sarja['nimi']}  {sarja['kausia']} tuotantokautta")

    # for sarja in jarjesta_tuotantokausien_mukaan(sarjat):
    #     print(sarja)
