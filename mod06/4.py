kaupungit = []

for x in range(5):
    nimi = input(f'Anna kaupungin nimi ({x+1}/5) > ')
    kaupungit.append(nimi)

for x in kaupungit:
    print(x)