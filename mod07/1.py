import random

def noppa():
    heitto = random.randint(1,6)
    return heitto

while True:
    tulos = noppa()
    print(f'{tulos}')
    if tulos == 6:
        break