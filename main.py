import numpy as np

class Board():

    player1 = 1
    player2 = -1
    # player1 plays left to right and player2 plays top to bottom

    def __init__(self,size):
        self.board = np.zeros((3,size,size))
        self.size = size

    def place_piece(self,x,y,player):
        if self.board[0,x,y]==0:
            self.board[0,x,y] = player

    hex_directions = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]]

    def neighborhood(self, x, y):
        for i in hex_directions:
            if 0 <= i[0]+x < self.size and 0 <= i[1] + y < self.size:
                yield [i[0] + x, i[1] + y]

    def paint_neighbor(self, x, y, level):
        player = self.board[0, x, y]
        for i in self.neighborhood(x, y):
            if self.board[0, i[0], i[1]] == player and self.board[level, i[0], i[1]] == 0:
                self.board[level, i[0], i[1]] = 1
                self.paint_neighbor(i[0], i[1], level)

    def check_conn_start(self, x, y, player):
        if (x == 0 and player == self.player1) or (y == 0 and player == self.player2):
            self.board[1, x, y] = 1
            self.paint_neighbor(x, y, 1)
        else:
            for i in self.neighborhood(x, y):
                if self.board[0, i[0], i[1]] == player and self.board[1, i[0], i[1]] == 1:
                    self.board[0, x, y] = 1
                    self.paint_neighbor(x, y, 1)

    def check_conn_end(self,x,y):
        if (x == self.size and player == player1) or (y == self.size and player == player2):
            self.board[2, x, y] = 1
            self.paint_neighbor(x, y, 2)
        else:
            for i in self.neighborhood(x, y):
                if self.board[0, i[0], i[1]] == player and self.board[1, i[0], i[1]] == 2:
                    self.board[0, x, y] = 1
                    self.paint_neighbor(x, y, 2)

    def check_victory(self, x, y):
        return self.board[1, x, y] == self.board[2, x, y] == 1