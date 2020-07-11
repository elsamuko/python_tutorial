instances = []

# Menue Legende
print(" ")
print("   1  Eingabe                    (Erweitert die Liste um einen Eintrag)")
print("   2  Ausgabe                    (Zeigt alle Listeneintraege an")
print(" ")

class Auto():
    def __init__(self, brand):
        self.brand = brand

def eingabe(brand, instances):
    # y = "auto" + str(index)
    y = Auto(brand)
    instances.append(y)
    menue(instances)

def ausgabe(instances):
    for i in instances:
        print(i.brand)

def menue(instances):
    print(" ")
    x = input("Input:")
    if x == "1": eingabe(input("Bitte Marke eingeben: "), instances)
    if x == "2": ausgabe(instances)

menue(instances)     # Mit dieser Funktion wird das Programm sozusagen gestartet

