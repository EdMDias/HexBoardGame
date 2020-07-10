import numpy as np
from keras.models import Sequential
from keras.layers import Dense

def random_bot(board):
    empty_positions = []
    for x in range(len(board[0, :, :])):
        for y in range(len(board[0, :, :])):
            if board[0, x, y] == 0:
                empty_positions.append([x, y])

    return np.random.permutation(empty_positions)[0]


def nn_bot(board):
    size = len(board[0, :, :])
    nn = Sequential()
    nn.add(Dense(2, activation='relu'))
    nn.add(Dense(size**2, activation='sigmoid'))
    nn.compile(loss = 'binary_crossentropy', optimizer = 'adam') #only needed to compile
    #return nn.get_layer('last')
    return nn.predict(board)

def model(size_of_board):
    nn = Sequential()
    nn.add(Dense(2, activation='relu'))
    nn.add(Dense(size_of_board ** 2, activation='softmax'))
    nn.compile(loss='binary_crossentropy', optimizer='adam')  # only needed to compile
    return nn


class NN_bot():

    def __init__(self,size_of_board,model):
        self.size_of_board = size_of_board
        self.model = model

#    def empty_positions(self, board):
#        tmp_board = board[0, :, :].copy()
#        for x in range(len(tmp_board)):
#            for y in range(len(tmp_board)):
#                if tmp_board[x, y] == 0:
#                    tmp_board[x, y] = 1
#                else:
#                    tmp_board[x, y] = 0
#        return tmp_board

    def empty_positions(self, board):
        return [board==0].copy()


    def predict_play(self, full_board):
        predictions = self.model.predict(full_board[0, :, :])
        predictions = predictions*self.empty_positions(full_board)
        return np.unravel_index(np.argmax(predictions),predictions.shape)
