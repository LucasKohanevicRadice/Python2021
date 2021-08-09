# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti



def joulukuusi(koko):

    print("joulukuusi!")
    i = 1
    kerroin = 0
    neulasia = "**"

    while i <= koko:
        print(" "*(koko-i) + "*" + neulasia*kerroin)
        i += 1
        kerroin += 1

    print(" " * (koko-1) + "*")

if __name__ == "__main__":
    joulukuusi(5)