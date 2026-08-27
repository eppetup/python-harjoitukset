sukupuoli = input("Anna biologinen sukupuoli (mies/nainen) > ")
hemoglobiinit = int(input("Anna hemoglobiiniarvo g/l > "))

if sukupuoli == "nainen":
  alaraja = 117
  ylaraja = 175
if sukupuoli == "mies":
  alaraja = 134
  ylaraja = 195
  
if hemoglobiinit < alaraja:
  print("Hemoglobiiniarvo on alhainen")
elif hemoglobiinit > ylaraja:
  print("Hemoglobiiniarvo on korkea")
else:
  print("Hemoglobiiniarvo on normaali")

  