import utils
import random

print('\nStarting the Rock Paper Scissors game!\n')
player_name = input('Please enter your name: ')

print('\nPick a hand: (0: Rock, 1: Paper, 2: Scissors)\n')
player_hand = int(input('Please enter a number (0-2): '))

if utils.validate(player_hand):
    computer_hand = random.randint(0, 2)

    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, '\nComputer')

    result = utils.judge(player_hand, computer_hand)
    print('\nResult: ' + result)
else:
    print('\nPlease enter a valid number\n')
