from Board import Board
import numpy as np

#
#board = Board.Board(int(input('Choose the size of the board\n')))
#board.print_board()

class Two_players_game(Board):

    def __init__(self,size):
        super().__init__(size)

    def turn(self, player):
        while True:
            position_str = input(f'Player {player}:\nChoose a position to play as two integers (matrix entry between 0 and {self.size - 1}) separated by a comma\n')
            x , y = int(position_str.split(',')[0]),int(position_str.split(',')[1])
            if self.board[0, x, y] == 0:
                self.board[0, x, y] = player
                self.check_conn_start(x, y, player)
                break

    def game(self):

        print('The player 1 plays top down and the player -1 plays left to right!\nHave fun!!!')

        player_on = (-1)**np.random.randint(0,2)
        while True:
            player_on *= -1
            self.turn(player_on)
            if self.check_victory(player_on):
                self.print_board()
                print(f'Player {player_on} won!')
                break
            else:
                self.print_board()
