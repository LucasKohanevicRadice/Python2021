# tee ratkaisu tänne

def lue(viesti: str, alkuraja: int, loppuraja: int ):

    while True:

        try:

            syote = int(input(f"{viesti }"))

            if syote in range(alkuraja,loppuraja+1):

                return syote
                  
            else:
                print(f"Syötteen on oltava kokonaisluku väliltä {alkuraja}...{loppuraja}")
                continue

        except ValueError:
            print(f"Syötteen on oltava kokonaisluku väliltä {alkuraja}...{loppuraja}")
            pass


    

if __name__ == "__main__":
    luku = lue("syötä luku: ", 95, 10)
    print("syötit luvun:", luku)    

    

