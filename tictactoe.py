"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    count_X, count_O = 0, 0
    for row in board:
        count_X += row.count(X)
        count_O += row.count(O)
    print(count_X, count_O)
    if count_X <= count_O:
        return X
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    moves = set()
    for x in range(0,3):
        for y in range(0,3):
            if board[x][y] == EMPTY:
                moves.add((x,y))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x,y = action
    turn = player(board)
    updated_baord = copy.deepcopy(board)
    try:
        if board[x][y] == EMPTY and x in range(0,3) and y in range(0,3):
            updated_baord[x][y] = turn
            print(updated_baord)
            return updated_baord
        else:
            raise ValueError("Invalid Move")
    except:
        raise ValueError("Invalid Move")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # rows
    for x in range(0,3):
        if board[x][0] != EMPTY and board[x][0] == board[x][1] and board[x][1] == board[x][2]:
            return board[x][0]
    # columns 
    for y in range(0,3):
        if board[0][y] != EMPTY and board[0][y] == board[1][y] and board[1][y] == board[2][y]:
            return board[0][y]
    # diagonals
    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return None   

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)
    if winner(board) is not None or empty_count == 0:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    turn = player(board)
    if turn == X:
        _,action = max_value(board)
    elif turn == O:
        _,action = min_value(board)
    return action

    
def max_value(board):
    if terminal(board):
        return utility(board)
    value = float('-inf')
    optimal_action = None
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
        optimal_action = action
    return value


def min_value(board):
    if terminal(board):
        return utility(board)
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action)))  
    return value

matrix = [[X, O, X],[X, O, X],[O, X, O]]
print(winner(matrix))
