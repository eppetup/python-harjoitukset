def gallatLitroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

while True:
  gallonat = int(input('Syötä gallonoiden määrä  > '))
  if gallonat < 0:
     break
  tulos = gallatLitroiksi(gallonat)
  print(f"{gallonat} gallonaa == {tulos} litraa")
