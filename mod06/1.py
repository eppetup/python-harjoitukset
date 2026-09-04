import random

kuutiot = int(input('Anna arpakuutioiden lukumäärä > '))
summa = 0

for x in range(kuutiot):
  summa = summa + random.randint(1,6)

print(f'Silmälukujen summa: {summa}')