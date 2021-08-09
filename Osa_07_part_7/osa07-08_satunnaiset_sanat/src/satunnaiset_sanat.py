# tee ratkaisu tänne


import random

def sanat(n: int, alku: str):

    kaikkine = []

    with open("sanat.txt") as tiedosto:

        for rivit in tiedosto:
            rivit = rivit.strip()
            if alku in rivit[:len(alku)]:
                kaikkine.append(rivit)

    try:
        return random.sample(kaikkine, n)
    
    except:
        raise ValueError
    
    # if len(kaikkine) < n:
    #     raise ValueError
    # else:
    #     return random.sample(kaikkine, n)

    #   Both work it seems. Very fascinating


    



#   Äijä vittu oot ollu haka. BIG PAT ON THE FOCKEN BACK M8 U FOCKEN ROCKIN IT. Tyylii 9/10 tehtävästä nyt menny tyyliin 3 viimesessä aliosassa läpi. Huhheijaa !1!11!!!!
if __name__ == "__main__":
    print(random.randint(1,3))