import Board

board = Board.Board(int(input('Choose the size of the board\n')))

def turn(board,player):
    position_str = input('Choose a position to play - tow integers separated by a comma\n')
    x , y = int(position_str.split(',')[0]),int(position_str.split(',')[1])
    board.place_piece(x, y, player)
    board.check_conn_start(x, y, player)

player_on = -1
while True:
    player_on *= -1
    turn(board,player_on)
    if board.check_victory():
        board.print_board()
        print(f'Player {player_on} won!')
        break
    else:
        board.print_board()