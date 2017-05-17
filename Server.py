from InputValidator import InputValidator
from Game import Game
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2137)
print("Server at {} ".format(server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    print("Waiting for connection...")
    connection, client_address = sock.accept()
    if connection or client_address:
        print("Client connected.")
        break

try:
    print("Connection from: " + str(client_address))
    while True:
        connection.send(str.encode("1. Start\n2. Koniec"))
        data = connection.recv(1024)
        choice = int(data.decode())
        if InputValidator.is_choice_valid(choice):
            if choice == 1:
                connection.send(str.encode("Podaj rozmiar planszy"))
                data = connection.recv(1024)
                size = int(data.decode())
                if InputValidator.is_size_valid(size):
                    game = Game(size)
                    connection.send(str.encode("1. Kółko\n2. Krzyżyk"))
                    data = connection.recv(1024)
                    sign = int(data.decode())
                    if InputValidator.is_choice_valid(sign):
                        game.start_game(sign)
                        while True:
                            connection.send(str.encode(game.draw_board() + "\nPodaj numer wiersza: "))
                            data = connection.recv(1024)
                            row = int(data.decode())
                            connection.send(str.encode("Podaj numer kolumny: "))
                            data = connection.recv(1024)
                            col = int(data.decode())
                            if InputValidator.is_position_valid(size, row, col) and game.is_position_valid(row, col):
                                game.player_move(row, col)
                                if game.check_winner() == 1:
                                    connection.send(str.encode(game.draw_board() + "\nwygrało kolko " + "END"))
                                    break
                                elif game.check_winner() == 2:
                                    connection.send(str.encode(game.draw_board() + "\nwygrał krzyżyk " + "END"))
                                    break
                                elif game.check_winner() == 3:
                                    connection.send(str.encode(game.draw_board() + "\nremis " + "END"))
                                    break
                            else:
                                connection.send(str.encode("Podana pozycja jest zajeta, lub niepoprawna"))
                    else:
                        connection.send(str.encode("Niewłaściwy typ gracza"))
                else:
                    connection.send(str.encode("Niewłaściwy rozmiar planszy"))
            elif choice == 2:
                connection.send(str.encode("Koniec gry " + "END"))
                break
        else:
            connection.send(str.encode("Niewłaściwy typ wyboru menu"))

finally:
    connection.send(str.encode("Connection closed."))
    connection.close()
    print("Connection closed.")
