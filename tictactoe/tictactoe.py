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

    xcounts, ocounts = 0, 0

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
    # make a deep copy of the board
    new_board = copy.deepcopy(board)

    # check if the action is legal
    if action not in actions(board):
        raise Exception
    else:
        new_board[action[0]][action[1]] = player(new_board)
    return new_board

    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check three horizontally
    for row in board:
        xcounts = row.count(X)
        ocounts = row.count(O)
        if xcounts == 3:
            return X 
        elif ocounts == 3:
            return O

    # check three vertically
    columns = []
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

    # check three diagnally
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
    # Check if board is full or if there is a winner
    empty_counts = 0
    for row in board:
        empty_counts += row.count(EMPTY)
    
    # if the board is not empty
    if empty_counts == 0:
        return True
    # if there is a winner
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
    
    cur_player = player(board)
    if cur_player == X:
        best_value = -math.inf
    else:
        best_value = math.inf

    for action in actions(board):
        new_value = minimax_value(result(board,action))
        if cur_player == X:
            if new_value > best_value:
                best_action = action
                best_value = new_value
        else:
            if new_value < best_value:
                best_action = action
                best_value = new_value
    
    return best_action

# Helper function
def minimax_value(board):
    if terminal(board):
        return utility(board)

    if player(board) == X: 
        # maximize value
        value = -math.inf
        for action in actions(board):
            value = max(value, minimax_value(result(board, action)))
    else:
        # minimize value
        value = math.inf
        for action in actions(board):
            value = min(value, minimax_value(result(board, action)))
    
    return value