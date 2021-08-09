# tee ratkaisu tänne

import math

# a^2 + b^2 = c^2, eli sqrt(a^2) + sqrt(b^2) = c. Simple enough.

def hypotenuusa(kateetti1: float, kateetti2: float):

    hypotenuusa = math.sqrt(kateetti1**2 + kateetti2**2)
    
    return hypotenuusa
