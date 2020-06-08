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
    # when the game board is empty
    if board == initial_state():
        return X

    xcounts = 0
    ocounts = 0

    for row in board:
        xcounts += row.count(X)
        ocounts += row.count(O)

    if xcounts <= ocounts:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    # each action is represented as a tuple (i,j) where i corresponds to
    # the row of the cell and j corresponds to which cell in the row

    # possible moves are any cells that do not already have an X or O
    actions = set()

    for row in range(3):
        for cell in range(3):
            if board[row][cell] == EMPTY:
                actions.add((row,cell))
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    # check if the cell is empty
    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception
    else:
        # new board gets action
        new_board[action[0]][action[1]] = player(new_board)
    return new_board

    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    columns = []

    # for three horizontally
    for row in board:
        xcounts = row.count(X)
        ocounts = row.count(O)

        if xcounts == 3:
            return X
        elif ocounts == 3:
            return O
    
    # for three vertically
    for piece in range(3):
        column = [row[piece] for row in board]
        columns.append(column)
    
    for column in columns:
        xcounts = column.count(X)
        ocounts = column.count(O)
    
        if xcounts == 3:
            return X
        elif ocounts == 3:
            return O

    # for three diagnally
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    elif board[2][0] == board[1][1] == board[0][2] == X:
        return X
    elif board[2][0] == board[1][1] == board[0][2] == O:
        return O

    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks if board is full or if there is a winner
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False
    
    raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    # player X wants to maximize the score
    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            best_value = min_value(result(board,action))
            if best_value > value:
                value = best_value
                best_action = action
    
    # player O wants to minimize the score
    elif player(board) == O:
        value = math.inf
        for action in actions(board):
            best_value = max_value(result(board, action))
            if best_value < value:
                value = best_value
                best_action = action
    else:
        raise Exception

    return best_action

# Helper function max_value for the max_player
def max_value(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board,action)))
    return value

# Helper function min_value for the min_player
def min_value(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board,action)))
    return value







