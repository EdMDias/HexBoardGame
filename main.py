import numpy as np

def create_board(n):
    board = np.zeros((n,n))
    return board

hex_directions = [[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0]]
def neighborhood(board,entry=(1,1)):
    #entry needs to be a tuple (a,b)
    # n = len(board)
    neighbors = []
    for i in hex_directions:
        if board[entry[0]+i[0],entry[1]+i[1]] == board[entry]:
            neighbors.append(i)
    return neighbors

def check_victory(board,player):
    #the board will have entries '1' and '-1' which will be the player
    pass

