import random

numero = random.randint(1,10)

while(True):
    arvaus = int(input('Anna luku (1...10) > '))
    if (arvaus < numero):
      print('Liian pieni arvaus')
    if (arvaus > numero):
      print('Liian suuri arvaus')
    if (arvaus == numero):
      print('Oikein')
      quit()