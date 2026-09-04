lista = []

while(True):

    luku = input('Anna luku > ')

    if luku == '':
        break

    lista.append(int(luku)) 

lista.sort(reverse=True)

a = 0

for x in lista:
    print(x)
    a = a + 1
    if (a == 5):
       break