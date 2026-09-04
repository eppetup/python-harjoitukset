import random

pisteet = int(input('Pisteiden määrä > '))
a = 0
ympyrassa = 0

while a < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        ympyrassa = ympyrassa + 1

    a = a + 1

pii = 4 * ympyrassa / pisteet
print(f'{pii}')