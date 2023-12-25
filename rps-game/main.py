# Para limpiar la shell cuando se ejecute
import os 
os.system('clear')

# Juego de piedra, papel o tijera
import random

# funcion para escoger opción del jugador
def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = (input('piedra, papel o tijera => ')).lower()

  if not user_option in options:
    print('esa opcion no es valida')
    return None, None

  computer_option = random.choice(options)
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

  
# funcion que calcula al ganador de la ronda
def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_wins, computer_wins

  
# funcion que muestras las victorias y el ganador final
def check_winner(user_wins, computer_wins):
  print('computer_wins', computer_wins)
  print('user_wins', user_wins)
  if computer_wins == 2:
    print('El ganador es la computadora')
    exit()

  if user_wins == 2:
    print('El ganador es el usuario')
    exit()

    
# funcion principal del juego
def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  # ciclo donde se invocan las funciones del juego
  while True:
    print('*' * 25)
    print('ROUND', rounds)
    print('*' * 25)
    rounds += 1
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, 
    user_wins, computer_wins)
    check_winner(user_wins, computer_wins)

    
# primera linea que se ejecuta  
run_game()