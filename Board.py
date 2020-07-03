import numpy as np

class Board():

    player1 = 1
    player2 = -1
    # player 1 plays top down (x == 0 to x == self.size - 1) and player -1 plays left right (y == 0 to y == self.size -1 )

    def __init__(self, size):
        self.board = np.zeros((2, size, size))
        self.size = size

    hex_directions = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]]

    def neighborhood(self, x, y):
        for i in self.hex_directions:
            if 0 <= i[0]+x < self.size and 0 <= i[1] + y < self.size:
                yield [i[0] + x, i[1] + y]

    def paint_neighbor(self, x, y):
        player = self.board[0, x, y]
        for i in self.neighborhood(x, y):
            if self.board[0, i[0], i[1]] == player and self.board[1, i[0], i[1]] == 0:
                self.board[1, i[0], i[1]] = player
                self.paint_neighbor(i[0], i[1])

    def check_conn_start(self, x, y, player):
        if (x == 0 and player == self.player1) or (y == 0 and player == self.player2):
            self.board[1, x, y] = player
            self.paint_neighbor(x, y)
        else:
            for i in self.neighborhood(x, y):
                if self.board[0, i[0], i[1]] == player and self.board[1, i[0], i[1]] != 0:
                    self.board[1, x, y] = self.board[1, i[0], i[1]]
                    self.paint_neighbor(x, y)

    def check_victory(self,player):
        if player == self.player1:
            return sum(self.board[1, self.size - 1, :]) > 0
        else:
            return sum(self.board[1, :,self.size - 1]) < 0

    def print_board(self):
        for i in range(self.size):
            line = ' '*2*i
            for j in range(self.size):
                line += '{:4.0f}'.format(self.board[0,i,j])
            print(line)
