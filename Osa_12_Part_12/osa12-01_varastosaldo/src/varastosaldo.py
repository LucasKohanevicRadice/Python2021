def jarjesta_varastosaldon_mukaan(alkiot: list):
    
    jarjestetty_varastosaldon_mukaan = []

    def varastosaldot(alkio: tuple):
        return alkio[2]
    
    # alkiot.sort(key = varastosaldot)

    for rivi in alkiot:
        jarjestetty_varastosaldon_mukaan.append(rivi) 
    
    jarjestetty_varastosaldon_mukaan.sort(key = varastosaldot)

    # jarjestetty_varastosaldon_mukaan.append(alkiot)


    return jarjestetty_varastosaldon_mukaan

    
if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22)]

    for tuote in jarjesta_varastosaldon_mukaan(tuotteet):
        print(f"{tuote[0]} {tuote[2]} kpl")
