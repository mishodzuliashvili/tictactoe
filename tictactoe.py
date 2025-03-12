import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Tally the number of X's and O's on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # Since X always makes the first move, if the counts are equal, it's X's turn
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_moves.add((i, j))

    return available_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Verify the action is valid
    if action not in actions(board):
        raise Exception("Invalid action")

    # Create a deep copy to avoid modifying the original board
    new_board = copy.deepcopy(board)

    # Apply the move
    i, j = action
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Examine rows for a winner
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    # Check columns for a winner
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        if column.count(X) == 3:
            return X
        if column.count(O) == 3:
            return O

    # Evaluate diagonals for a winner
    diagonal1 = [board[i][i] for i in range(3)]
    if diagonal1.count(X) == 3:
        return X
    if diagonal1.count(O) == 3:
        return O

    diagonal2 = [board[i][2 - i] for i in range(3)]
    if diagonal2.count(X) == 3:
        return X
    if diagonal2.count(O) == 3:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game ends if there's a winner
    if winner(board) is not None:
        return True

    # Check if any empty cells remain
    for row in board:
        if EMPTY in row:
            return False

    # If all cells are filled and no winner exists, it's a draw
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the game is already over, no action is possible
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        # X aims to maximize utility
        best_score = float("-inf")
        optimal_move = None

        for action in actions(board):
            # Calculate the minimum opponent value for each possible move
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                optimal_move = action

        return optimal_move
    else:
        # O aims to minimize utility
        best_score = float("inf")
        optimal_move = None

        for action in actions(board):
            # Calculate the maximum opponent value for each possible move
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                optimal_move = action

        return optimal_move


def max_value(board):
    """
    Returns the maximum utility achievable from a board state.
    """
    if terminal(board):
        return utility(board)

    value = float("-inf")

    for action in actions(board):
        value = max(value, min_value(result(board, action)))

    return value


def min_value(board):
    """
    Returns the minimum utility achievable from a board state.
    """
    if terminal(board):
        return utility(board)

    value = float("inf")

    for action in actions(board):
        value = min(value, max_value(result(board, action)))

    return value
