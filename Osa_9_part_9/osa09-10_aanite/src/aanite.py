# TEE RATKAISUSI TÄHÄN:


class Aanite():

    def __init__(self, pituus: int) -> None:

        if pituus < 0:
            raise ValueError("Pituus ei voi olla negatiivinen, eihän?")

        self.pituus = pituus

        pass

    @property

    def lenght(self):
        return self.pituus
    
    @lenght.setter

    def lenght(self, pituus):

        if pituus >= 0:
            self.pituus = pituus
        
        else:
            raise ValueError("Pituus ei voi olla negatiivinen, eihän?")



dark_side_of_the_moon = Aanite(420)

print(dark_side_of_the_moon.lenght)

dark_side_of_the_moon.lenght = 520

print(dark_side_of_the_moon.lenght)






