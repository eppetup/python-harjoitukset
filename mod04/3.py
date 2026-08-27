sukupuoli = input("Anna biologinen sukupuoli (mies/nainen) > ")
hemoglobiinit = int(input("Anna hemoglobiiniarvo g/l > "))

if sukupuoli == "nainen":
  alaraja = 117
  ylaraja = 175
elif sukupuoli == "mies":
  alaraja = 134
  ylaraja = 195
else:
  print("Virheellinen sukupuoli")
  quit()

if hemoglobiinit < alaraja:
  print("Hemoglobiiniarvo on alhainen")
elif hemoglobiinit > ylaraja:
  print("Hemoglobiiniarvo on korkea")
else:
  print("Hemoglobiiniarvo on normaali")

  