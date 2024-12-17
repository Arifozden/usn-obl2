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

nytt_land = input("Skriv inn et nytt land: ")
hovedstad = input("Skriv inn hovedstaden i dette landet: ")
innbyggere = float(input("Skriv inn antall millioner innbyggere i hovedstaden: "))