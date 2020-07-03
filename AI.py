# This is the first opponent
import numpy as np

def random_bot(board):
    empty_positions = []
    for x in range(board.size):
        for y in range(board.size):
            if board[0, x, y] == 0:
                empty_positions.append([x, y])

    return np.random.shuffle(empty_positions)[0]
