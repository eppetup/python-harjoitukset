import math

def pizzanHinta(halkaisija, eurot):
    metrit = halkaisija / 100
    pinta_ala = math.pi * (metrit/2) ** 2
    hinta = eurot / pinta_ala
    return hinta


halkaisijat = []
hinnat = []
yksikkohinnat = []

for x in range(2):
    halkaisijat.append(int(input(f'Anna halkaisija senttimetreinä ({x+1}/2) > ')))
    hinnat.append(int(input(f'Anna hinta euroina ({x+1}/2) > ')))
    yksikkohinnat.append(pizzanHinta(halkaisijat[x], hinnat[x]))

if yksikkohinnat[0] < yksikkohinnat[1]:
    print("Ensimmäinen pizza on edullisempi")
else:
    print("Toinen pizza on edullisempi")
