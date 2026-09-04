syote = 0
suurin = 0
pienin = 0
a = 0

while(syote != ''):

    syote = input('Anna luku > ')

    if a == 0 and syote.isnumeric():
       suurin = int(syote)
       pienin = int(syote)
       a = 1
 
    if syote.isnumeric():
      if int(syote) > suurin:
        suurin = int(syote)
      if int(syote) < pienin:
        suurin = int(syote)

print(f'Suurin luku {suurin}')
print(f'Pienin luku {pienin}')
quit()