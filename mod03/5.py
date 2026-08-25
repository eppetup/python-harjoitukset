leiviskat = float(input('Anna leiviskät.\n'))
naulat = float(input('\nAnna naulat.\n'))
luodit = float(input('\nAnna luodit.\n'))

naulat += leiviskat * 20
luodit += naulat * 32
grammat = luodit * 13.3

print(grammat)
kilogrammat = int(grammat // 1000)
grammat = grammat % 1000

print('\nMassa nykymittojen mukaan:')
print(f'{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.')
