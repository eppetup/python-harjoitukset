pituus = float(input("Anna kuhan pituus senttimetreinä > "))
if pituus < 37:
  print("Laske kuha takaisin järveen!")
  print(f"Alimmasta sallitusta pyyntimitasta puuttuu {37 - pituus} senttiä")
