import random

# koodi 1
koodi1 = ""
x = 0

while x < 3:
  koodi1 += str((random.randint(0, 9)))
  x += 1

print(f'Kolmenumeroinen koodi: {koodi1}')

# koodi2
koodi2 = ""
x = 0

while x < 4:
  koodi2 += str((random.randint(1, 6)))
  x += 1

print(f'Nelinumeroinen koodi: {koodi2}')