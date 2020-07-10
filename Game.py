import Against_bot
import Bot_vs_bot
import AI
import two_players_version as tpv

def game():

    print('Choose the type of game you want to try?')
    m = int(input('1 - 2 Players Game\n2 - Player vs Bot Game\n3 - Bot vs Bot Game\n1, 2 or 3?\n'))
    n = int(input('\nAnd what is the size of the board you feel like?\n'))


    if m == 1:
        game = tpv.Two_players_game(n)
        game.game()
    elif m == 2:
        game = Against_bot.Game_Against_Bot(n, AI.random_bot)
        game.game()
    else:
        model = AI.model(n)
        battle_of_random = Bot_vs_bot.Bot_vs_bot(n,AI.random_bot,AI.random_bot)
        battle_of_random.game()