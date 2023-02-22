import random


def elegir_opcion():
  option = ("piedra", "papel", "tijera")
  user_option = input("piedra, papel o tijera => ").lower()
  
  if not user_option in option:
    print("La opcion escrita no es correcta")
    return None, None

  computer_option = random.choice(option)
  print('El CPU, escogio =>', computer_option)
  return user_option, computer_option

def reglas_juego(user_option, computer_option, count_user, count_computer):
  if user_option == computer_option:
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("El usuario gano!!!")
      count_user += 1
    else:
      print("papel gana a piedra")
      print("La computadora gano!!!")
      count_computer += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("EL usuario gano!!!")
      count_user += 1
    else:
      print("tijera gana a papel")
      print("La computadora gano")
      count_computer += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel")
      print("El usuario gano!!!")
      count_user += 1
    else:
      print("piedra gana a tijera")
      print("La computadora gano!!!")
      count_computer += 1
  return count_user, count_computer


def juego ():
  count_raund = 0
  count_user = 0
  count_computer = 0
  while True:
    print('*' * 32)
    print(' ' * 12, 'ROUND ', count_raund, ' ' * 12)
    print('*' * 32)
    print('*', ' ' * 28, '*')
    print('*', 'Rondas ganadas User: ', count_user, ' ' * 4, '*')
    print('*', 'Rondas ganadas CPU: ', count_computer, ' ' * 5, '*')
    print('*', ' ' * 28, '*')
    print('*' * 32)

    user_option, computer_option = elegir_opcion()
    count_user, count_computer = reglas_juego(user_option, computer_option, count_user, count_computer)
    
    
    if count_computer == 2:
      print('La cumputadora gano con ', count_computer, ' ganadas.')
      break
    if count_user == 2:
      print('El usuario gano con ', count_user, ' ganadas')
      break
    count_raund += 1



juego()