import random

def noppa(tahkot):
    heitto = random.randint(1,tahkot)
    return heitto


tahkot = int(input("Syötä tahkojen määrä > "))

while True:
    tulos = noppa(tahkot)
    print(f'{tulos}')
    if tulos == tahkot:
        break