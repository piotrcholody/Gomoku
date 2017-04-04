from InputValidator import InputValidator
from Game import Game


print ('Podaj rozmiar planszy:')
size = int(input())
if InputValidator.is_size_valid(size):
    game1 = Game(size)
    print('kolko czy krzyzyk?')
    print('1. kolko')
    print('2. krzyzyk')
    sign = int(input())
    game1.start_game(sign)
    while True:
         print('Podaj numer wiersza:')
         row = int(input())
         print('Podaj numer kolumny:')
         col = int(input())
         if InputValidator.is_position_valid(size, row, col) and game1.is_position_valid(int(row), int(col)):
             game1.player_move(int(row), int(col))
             if game1.check_winner() == 1:
                  print('wygralo kolko')
                  break
             elif game1.check_winner() == 2:
                print('wygral krzyzyk')
                break
             elif game1.check_winner() == 3:
                  print('remis')
                  break
         else:
            print ('podana pozycja jest nieprawidlowa')
else:
    print('rozmiar planszy musi byc pomiedzy 3, a 20')
