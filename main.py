import numpy as np

class board():
    def __init__(self,size):
        self.board = np.zeros((3,size,size))
        self.size = size

    def place_piece(self,x,y,player):
        if self.board[0,x,y]==0:
            self.board[0,x,y] = player

    hex_directions = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]]

    def neighborhood(self, x, y):
        for i in hex_directions:
            if i[0]+x >= 0 and i[0]+x < self.size and i[1]+y >= 0 and i[1]+y < self.size:
                yield i

    def paint_neighbor(self, x, y, level):
        player = self.board[0, x, y]
        for i in self.neighborhood(x,y):
            if self.board[0,i[0],i[1]] == player and  self.board[level,i[0],i[1]] == 0:
                self.board[level, i[0], i[1]] = 1
                self.paint_neighbor(i[0], i[1], level)


    def check_conn_start(self, x, y, player):
        if (x==0 and player == player1) or (y==0 and player==player2):
            board[1,x,y]=1
            # set board[1,a,b]=1 for neighbors of [a,b] that have the same piece
        #elif one neighbor of [x,y] has [1,a,b]=1
            # board[1,x,y]=1
            # set board[1,a,b]=1 for neighbors of [a,b] that have the same piece

    def check_conn_end(self,x,y):
        if (x == self.size and player == player1) or (y == self.size and player == player2):
            board[2, x, y] = 1



