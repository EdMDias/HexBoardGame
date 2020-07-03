from Board import Board
import numpy as np

class Game_Against_Bot(Board):

    def __init__(self, size, bot):
        super().__init__(size)

        self.bot = bot

    def turn(self,who_is_playing):

        if who_is_playing == 1:
            while True:
                position_str = input(f'Choose a position to play as two integers (matrix entry between 0 and {self.size - 1}) separated by a comma\n')
                x, y = int(position_str.split(',')[0]), int(position_str.split(',')[1])
                if self.board[0, x, y] == 0:
                    self.board[0, x, y] = 1
                    self.check_conn_start(x, y, 1)
                    break
        else:
            x, y = self.bot(self.board)
            self.board[0, x, y] = -1
            self.check_conn_start(x, y, -1)

    def game(self):

        print('Your pieces are marker with 1 and you play top bottom.\nGood luck!!!')
        self.print_board()

        player_on = 1 if np.random.randint(0, 2) else -1
        while True:
            player_on *= -1
            self.turn(player_on)
            if self.check_victory(player_on):
                self.print_board()
                if player_on == 1:
                    print('You won the Game!!!')
                else:
                    print('Shame on you!!!\nYou just lost against AI!!!')
                break
            else:
                self.print_board()

