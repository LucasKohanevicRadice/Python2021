# Tee ratkaisu tänne

def anagrammi(m1 :str, m2 :str):

   if sorted(m1) == sorted(m2):
       return True
   elif sorted(m1) != sorted(m2):
       return False
