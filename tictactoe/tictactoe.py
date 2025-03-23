"""
Tic Tac Toe Player
"""

import math, copy

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
    moves = 0

    if initial_state() == True:
        return X
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] is not None:
                    moves += 1
        if moves % 2 == 0:
            return X
        else:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid Move")

    i, j = action
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)
    return board_copy

# The 4 next functions are for checking if player or AI wins if a line, column or both diagonals
def check_row(board, player):
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False
    
def check_col(board, player):
    for j in range(len(board)):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    return False

def check_diag1(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if i == j and board[i][j] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False
    
def check_diag2(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (len(board) - i - 1) == j and board[i][j] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_row(board, X) or check_col(board, X) or check_diag1(board, X) or check_diag2(board, X):
        return X
    elif check_row(board, O) or check_col(board, O) or check_diag1(board, O) or check_diag2(board, O):
        return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there's a winner
    if winner(board):
        return True

    # Check if there's no empty tiles.
    cells = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is not EMPTY:
                cells += 1
    if cells == 9:
        return True
    
    else:
        return False


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


def minimax_value(board):
    """
    recursive function to get the min and max possible value of each play
    """
    if terminal(board):
        return utility(board)
    elif player(board) == X:
        func = max
        v = -math.inf
    else:
        func = min
        v = math.inf
    for action in actions(board):
        v = func(v, minimax_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    for action in actions(board):
        if minimax_value(board) == minimax_value(result(board, action)):
            return action
    
