import math

def areal_og_omkrets(a, b):
    r = a / 2
    areal_trekant = (a * b) / 2
    areal_halvsirkel = (math.pi * r**2) / 2
    total_areal = areal_trekant + areal_halvsirkel

    omkrets = b + a + (math.pi * r)

    return total_areal, omkrets

a = float(input("Skriv inn lengden av basen a: "))
b = float(input("Skriv inn høyden b: "))

areal, omkrets = areal_og_omkrets(a, b)
print(f"Total areal: {areal:.2f}")