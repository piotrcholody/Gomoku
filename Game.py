import random
from abc import ABC, abstractmethod


class AbstractGame(ABC):

    @abstractmethod
    def start_game(self, player_sign):
        pass

    @abstractmethod
    def is_position_valid(self, x, y):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def player_move(self, x, y):
        pass

    @abstractmethod
    def computer_move(self, x, y):
        pass

    @abstractmethod
    def check_winner(self):
        pass


class Game(AbstractGame):
    def __init__(self, board_size):
        self.board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.player = 0
        self.computer = 0

    def start_game(self, player_sign):
        if player_sign == 1:
            self.player = 1
            self.computer = 2
        else:
            self.player = 2
            self.computer = 1
        if self.computer == 1:
            self.row = random.randint(0, len(self.board) - 1)
            self.col = random.randint(0, len(self.board) - 1)
            self.computer_move(self.row, self.col)

    def check_winner(self):
        for i in self.board:
            if i.count(1) == len(self.board):
                return 1
            elif i.count(2) == len(self.board):
                return 2
        self.tmp = [[0 for _ in range(len(self.board))] for _ in range(len(self.board))]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.tmp[i][j] = self.board[j][i]
        for i in self.tmp:
            if i.count(1) == len(self.board):
                return 1
            elif i.count(2) == len(self.board):
                return 2
        self.tmp = [[0 for _ in range(len(self.board))] for _ in range(len(self.board))]
        k = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if i == j:
                    self.tmp[k] = self.board[i][j]
                    k += 1
        if self.tmp.count(1) == len(self.board):
            return 1
        elif self.tmp.count(2) == len(self.board):
            return 2
        self.tmp = [[0 for _ in range(len(self.board))] for _ in range(len(self.board))]
        k = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if len(self.board) - i - 1 == j:
                    self.tmp[k] = self.board[i][j]
                    k += 1
        if self.tmp.count(1) == len(self.board):
            return 1
        elif self.tmp.count(1) == len(self.board):
            return 2
        self.counter = 0
        for i in self.board:
            self.counter += i.count(0)
        if self.counter == 0:
            return 3
        return 0

    def player_move(self, x, y):
        if self.is_position_valid(x, y):
            self.board[x][y] = self.player
        while True:
            self.row = random.randint(0, len(self.board) - 1)
            self.col = random.randint(0, len(self.board) - 1)
            if self.is_position_valid(self.row, self.col):
                self.computer_move(self.row, self.col)
                break

    def computer_move(self, x, y):
        if self.check_winner() == 0:
            self.board[x][y] = self.computer
        self.draw_board()

    def is_position_valid(self, x, y):
        if self.board[x][y] == 0:
            return True
        else:
            return False

    def draw_board(self):
        self.temp = ''
        for i in range(len(self.board)):
            self.temp += '|'
            for j in range(len(self.board)):
                self.sign = ' '
                if self.board[i][j] == 1:
                    self.sign = 'O'
                elif self.board[i][j] == 2:
                    self.sign = 'X'
                self.temp += self.sign + " |"
            self.temp += '\n'
        return self.temp
