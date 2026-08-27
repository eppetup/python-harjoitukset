vuosi = int(input("Anna vuosiluku > "))

karkausvuosi = False

if vuosi % 100 == 0:
  if vuosi % 400 == 0:
    karkausvuosi = True
elif vuosi % 4 == 0:
  karkausvuosi = True

if karkausvuosi:
  print(f"Vuosi {vuosi} on karkausvuosi")
else:
  print(f"Vuosi {vuosi} ei ole karkausvuosi")