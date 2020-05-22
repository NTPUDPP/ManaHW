import numpy as np
from math import inf as infinity

game_state = [['','',''],['','',''],['','','',]]; #2D-Array 
players = ['X','O']; #Player's types
player_repeat = 'Y'

def move_on(player_ind,state,block_num):
    if state[(block_num - 1) / 3][(block_num - 1) % 3] is '':
        state[(block_num-1)/3][(block_num-1)%3] = player_ind
    else:
        block_num = input('Position is not empty!! Please enter another position for placing X or O : ')
        move_on(player_ind,state,block_num)

def checking_current_state(game_state):
    #Checking a drawing condition 
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] == '':
                draw_flag = 1
    if draw_flag == 0:
        return None, "Draw"

    #Checling a winning condition (Vertical)
    if game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not '': #left-vertical
        return game_state[0][0], "Done"
    if game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not '': #middle-vertical
        return game_state[0][1], "Done"
    if game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not '': #right-vertical
        return game_state[0][2], "Done"

    #Checking a winning condition (Horizontal)
    if game_state[0][0] == game_state[0][1]and game_state[0][1] == game_state[0][2] and game_state[0][0] is not '': #top-horizontal
        return game_state[0][0], "Done"
    if game_state[1][0] == game_state[1][1]and game_state[1][1] == game_state[1][2] and game_state[1][0] is not '': #middle-horizontal
        return game_state[1][0], "Done"
    if game_state[2][0] == game_state[2][1]and game_state[2][1] == game_state[2][2] and game_state[2][0] is not '': #bottom-horizontal
        return game_state[2][0], "Done"
    
    #Checking a winning condition (Diagonal)
    if game_state[0][0] == game_state[1][1]and game_state[1][1] == game_state[2][2] and game_state[0][0] is not '': #left-horizontal
        return game_state[0][0], "Done"
    if game_state[0][2] == game_state[1][1]and game_state[1][1] == game_state[2][0] and game_state[0][2] is not '': #right-horizontal
        return game_state[0][2], "Done"

    return None, "Not yet"

def create_board(game_state):
    print('____________________')
    print('|' + str(game_state[0][0] + '|' + str(game_state[0][1]) + '|' + str(game_state[0][2]) + '|'),
    print('|' + str(game_state[1][0] + '|' + str(game_state[1][1]) + '|' + str(game_state[1][2]) + '|'),
    print('|' + str(game_state[2][0] + '|' + str(game_state[2][1]) + '|' + str(game_state[2][2]) + '|'),
    print('____________________')

#Playing
while player_repeat == 'Y' or player_repeat == 'y':
    print('Start New Game')
    current_state = "Not yet"
    game_state = [['','',''],['','',''],['','','',]]; #2D-Array
    winner = None
    player_order = input('Who is gonna play it first (X is P1 or O is P2) : ')
    if player_order == 'X' or player_order == 'x':
        player_id = 0 #P1
    else:
        player_id = 1 #P2

    while current_state == 'Not yet':
        if player_id == 0: #Human
            player_pos = input('Enter your position to place X or O (from 1-9) : ')
            move_on(players[player_id],game_state,player_pos)
        else: #Bot
            player_pos = input('Enter your position to place X or O (from 1-9) : ')
            move_on(players[player_id],game_state,player_pos)
        create_board(game_state)

        winner, current_state = checking_current_state(game_state)

        if winner is not None:
            print(str(winner) + 'is the winner!!')
        else:
            player_id = (player_id-1)%2

        if current_state == "Draw":
            print('DRAW!!')

    player_repeat = input('Do you want to play it again (Y/N) : ')
    if player_repeat == 'N' or player_repeat == 'n':
        print("END")