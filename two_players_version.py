import Board
import numpy as np

print('The player 1 plays top down and the player -1 plays left to right!\nHave fun!!!')
board = Board.Board(int(input('Choose the size of the board\n')))
board.print_board()

def turn(board,player):
    while True:
        position_str = input(f'Player {player}:\nChoose a position to play as two integers (matrix entry between 0 and {board.size - 1}) separated by a comma\n')
        x , y = int(position_str.split(',')[0]),int(position_str.split(',')[1])
        if board.board[0, x, y] == 0:
            board.board[0, x, y] = player
            board.check_conn_start(x, y, player)
            break

player_on = (-1)**np.random.randint(0,2)
while True:
    player_on *= -1
    turn(board,player_on)
    if board.check_victory(player_on):
        board.print_board()
        print(f'Player {player_on} won!')
        break
    else:
        board.print_board()
