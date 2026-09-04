vaarat = 0

while(vaarat < 5):
  tunnus = input('Syotä käyttäjätunnus > ')
  salasana = input('Syötä salasana > ')

  if tunnus == 'python' and salasana == 'rules':
    print('Tervetuloa')
    quit()
  else:
    vaarat = vaarat + 1
    print(f'Pääsy evätty {vaarat}/5')