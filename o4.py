data = {
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Tyskland": ["Berlin", 3.769],
}

land = input("Skriv inn et land: ")
if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hoovedstad} er hovedstaden i {land} og har {innbyggere} millioner innbyggere i {hovedstad}.")
else:
    print(f"Fant ikke landet {land}.")