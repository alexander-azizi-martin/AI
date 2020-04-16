"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None
INFINITY = 32


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
    x_turns = 0
    o_turns = 0

    # Iterates over board and counts num of Xs and Os
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                x_turns += 1
            elif board[row][col] == "O":
                o_turns += 1

    # Checks whose turn it is based o num of Xs and Os on board
    if x_turns + o_turns == 9:
        return EMPTY
    elif x_turns - o_turns == 0:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    # Iterates over board and finds empty spots
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                actions.append((row, col))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = deepcopy(board)
    current_player = player(board_copy)
    row, col = action

    # Checks if action is valid
    if board_copy[row][col] == EMPTY:
        board_copy[row][col] = current_player
    else:
        raise ValueError

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks board horizontally and vertically for three in a row
    for row in range(3):
        player_h, player_v = board[row][0], board[0][row]
        num_in_row_h, num_in_row_v = 0, 0

        for col in range(3):
            if board[row][col] == player_h:
                num_in_row_h += 1
            if board[col][row] == player_v:
                num_in_row_v += 1

        if num_in_row_h == 3 and player_h != None:
            # Three in a row was found on horizontally
            return player_h
        elif num_in_row_v == 3 and player_v != None:
            # Three in a row was found on vertically
            return player_v

    # Checks board diagonally for three in a row
    player_l, player_r = board[0][0], board[0][2]
    num_in_row_l, num_in_row_r = 0, 0

    for row, col in zip(range(3), range(3)):
        if board[row][col] == player_l:
            num_in_row_l += 1
        if board[row][2 - col] == player_r:
            num_in_row_r += 1

    if num_in_row_l == 3 and player_l != None:
        # Three in a row was found on the left diagonal
        return player_l
    elif num_in_row_r == 3 and player_r != None:
        # Three in a row was found on the right diagonal
        return player_r

    # No three in a row was found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks if there is a winner or if the board is full
    return winner(board) != None or len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)

    if player == "X":
        return 1
    elif player == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    optimal_action = ()

    if terminal(board):
        return ()

    min_value = INFINITY
    max_value = -INFINITY

    # Tries to maximize score with X
    if current_player == "X":
        for action in actions(board):
            optimal = MinValue(result(board, action), -INFINITY, INFINITY, 0)
            if optimal > max_value:
                optimal_action = action
                max_value = optimal

    # Tries to maximize score with O
    if current_player == "O":
        for action in actions(board):
            optimal = MaxValue(result(board, action), -INFINITY, INFINITY, 0)
            if optimal < min_value:
                optimal_action = action
                min_value = optimal

    return optimal_action


def MaxValue(board, alpha, beta, depth):
    """
    Returns the utility of an action for the X player.
    """
    if terminal(board):
        return utility(board)

    v = -INFINITY
    for action in actions(board):
        v = max(v, MinValue(result(board, action), alpha, beta, depth + 1))
        alpha = max(alpha, v)
        if alpha >= beta:
            return alpha

    return v


def MinValue(board, alpha, beta, depth):
    """
    Returns the utility of an action for the O player.
    """
    if terminal(board):
        return utility(board)

    v = INFINITY
    for action in actions(board):
        v = min(v, MaxValue(result(board, action), alpha, beta, depth + 1))
        beta = min(beta, v)
        if alpha >= beta:
            return beta

    return v
