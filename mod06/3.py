luku = int(input('Anna luku > '))

a = 2

for x in range(luku):
  if luku % a == 0 and a != luku:
    print('Luku ei ole alkuluku')
    quit()

print('Luku on alkuluku')