# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:08:26 2021

@author: jhyoon
"""
# 1차원 리스트 보드
game_board = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']


# 비어 있는 칸을 찾아서 리스트로 반환
def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
        if cell == ' ':
            cells.append(x)
    return cells
        
# 비어 있는 칸에 놓을 수 있음
def valid_move(x):
    return x in empty_cells(game_board)

# 위치 x에 놓음
def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

# 현재 게임 보드를 그림
def draw(board):
    for i, cell in enumerate(board):
        if i%3 == 0:
            print('\n---------------')
        print('|', cell, '|', end='')
    print('\n---------------')
            
# 보드의 상태를 평가
def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score


# 1차원 리스트에서 동일한 문자가 수직, 수평, 대각선 줄이 나타나면 승리
def check_win(board, player):
    win_conf = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conf

def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')

# minimax 알고리즘
def minimax(board, depth, maxPlayer):
    pos = -1
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)
    
    if maxPlayer:
        value = -10000 # 음의 무한대
        for p in empty_cells(board):
            board[p] = 'X'
            
            x, score = minimax(board, depth-1, False)
            board[p] = ' '
            
            if score > value:
                value = score
                pos = p
    else:
        value = +10000 # 양의 무한대
        for p in empty_cells(board):
            board[p] = 'O'
            
            # 경기자 교체
            x, score = minimax(board, depth-1, True)
            board[p] = ' ' # 보드 원상태로
            if score < value:
                value = score
                pos = p
    return pos, value

player = 'X'

# main program
while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break
    i, v = minimax(game_board, 9, player == 'X')
    move(i, player)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    
if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')
            
    
            