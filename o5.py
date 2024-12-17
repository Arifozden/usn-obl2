import math

def areal_og_omkrets(a, b):
    r = a / 2
    areal_trekant = (a * b) / 2
    areal_halvsirkel = (math.pi * r**2) / 2
    total_areal = areal_trekant + areal_halvsirkel

    omkrets = b + a + (math.pi * r)