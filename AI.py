import numpy as np

def random_bot(board):
    empty_positions = []
    for x in range(len(board[0,:,:])):
        for y in range(len(board[0,:,:])):
            if board[0, x, y] == 0:
                empty_positions.append([x, y])

    return np.random.permutation(empty_positions)[0]
