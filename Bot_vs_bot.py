import numpy as np
from Board import Board

class Bot_vs_bot(Board):

    def __init__(self, size, bot1, bot2):
        super().__init__(size)
        self.bot1 = bot1
        self.bot2 = bot2

    def turn(self, bot):
        if bot == 1:
            x, y = self.bot1(self.board)
            self.board[0, x, y] = bot
            self.check_conn_start(x, y, bot)
        else:
            x, y = self.bot2(self.board)
            self.board[0, x, y] = bot
            self.check_conn_start(x, y, bot)

    def game(self):
        bot_on = 1 if np.random.randint(0, 2) else -1
        while True:
            bot_on *= -1
            self.turn(bot_on)
            if self.check_victory(bot_on):
                self.print_board()
                print(f'Bot {bot_on} won!')
                break
            else:
                self.print_board()

