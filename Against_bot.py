from Board import Board
import AI
import numpy as np

class Game_Against_Bot(Board):

    def __init__(self, size, player, bot):
        super().__init__(size)

        self.player = player
        self.bot = bot

    def turn(self,who_is_playing):

        if who_is_playing == self.player:
            while True:
                position_str = input(f'Player {self.player}:\nChoose a position to play as two integers (matrix entry between 0 and {self.size - 1}) separated by a comma\n')
                x, y = int(position_str.split(',')[0]), int(position_str.split(',')[1])
                if self.board[0, x, y] == 0:
                    self.board[0, x, y] = self.player
                    self.check_conn_start(x, y, self.player)
                    break
        else:
            x, y = AI.random_bot(self.board)
            self.board[0, x, y] = self.bot
            self.check_conn_start(x, y, self.bot)

    def game(self):

        player_on = 1 if np.random.randint(0, 2) else -1
        while True:
            player_on *= -1
            self.turn(player_on)
            if self.check_victory(player_on):
                self.print_board()
                print(f'Player {player_on} won!')
                break
            else:
                self.print_board()

