# Reference:  https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/
# Description: An implementatio of the game using alpha-beta pruning to increase the solving speed
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
    count = 0
    for row in board:
        for i in range(3):
            if row[i] == X or row[i] == O:
                count += 1
    if count % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action = (i, j)
                actions.add(action)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    if board[row][col] != EMPTY:
        raise Exception("Invalid Move")
    if row > 3 or col > 3 or row < 0 or col < 0:
        raise Exception("Invalid Move")
    # Find out the player 
    p = player(board)
    tmp = copy.deepcopy(board)
    tmp[row][col] = p
    return tmp


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
    # Check the vertical
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
    # Check the left diagonal
    if (board[0][0] == board[1][1] == board[2][2]) and board[1][1] != EMPTY:
        return board[1][1]
     # Check the right diagonal
    if (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != EMPTY:
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    p = winner(board)
    if p != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    p = winner(board)
    if p == X:
        return 1
    elif p == O:
        return -1
    return 0

"""
def minimax(board):
    if terminal(board):
        return None
    p = player(board)
    # If it is X, return the action that maximizes the utility
    # If it is O, return the action that minimizes the utility
    if p == X:
        n = max_value(board)
    else:
        n = min_value(board)
    for action in actions(board):
        if p == X:
            if min_value(result(board, action)) == n:
                return action
        if p == O:
            if max_value(result(board, action)) == n:
                return action
    return None

# Implement Max function

def max_value(board):
    x = -100
    if terminal(board):
        return utility(board)
    for action in actions(board):
        x = max(x, min_value(result(board, action)))
    return x


def min_value(board):
    y = 100
    if terminal(board):
        return utility(board)
    for action in actions(board):
        y = min(y, max_value(result(board, action)))
    return y
"""
def minimax(board):
    if terminal(board):
        return None
    p = player(board)
    if p == X:
        action = solve(board)[1]
    elif p == O:
        action = solve(board)[1]
    return action
    


# Add just the two functions so that they return both action and the max value
def solve(board, alpha=-float('inf'), beta=float('inf')):
    if terminal(board):
        return utility(board), None
    if player(board) == "X":
        best_value = -float('inf')
        set_action = actions(board)
        best_action = list(set_action)[0]
        for action in set_action:
            # the utility of taking the action
            new_board = result(board, action)
            value = solve(new_board, alpha, beta)
            value = value[0]
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value, best_action
    elif player(board) == "O":
        best_value = float('inf')
        set_action = actions(board)
        best_action = list(set_action)[0]
        for action in set_action:
            # the utility of taking the action
            new_board = result(board, action)
            value = solve(new_board, alpha, beta)[0]
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value, best_action

