# Tic-Tac-Toe Game with AI Implementation

I've developed a Tic-Tac-Toe application featuring an AI opponent that uses the Minimax algorithm.

In my `tictactoe.py` file, I've built the complete game functionality by implementing these essential functions:

- `player`: Determines the next turn by analyzing the board state
- `actions`: Identifies all valid moves available
- `result`: Generates a new board configuration after a move without altering the original
- `winner`: Evaluates if either player has achieved victory
- `terminal`: Checks if the game has concluded
- `utility`: Assigns values to final board states (X win = 1, O win = -1, tie = 0)
- `minimax`: Calculates optimal move selection through the minimax algorithm

The minimax strategy works by systematically evaluating potential future game positions. For each position, it selects the most advantageous move by assuming both players will make their best possible choices.

Tic-Tac-Toe is mathematically solved, so with perfect strategy, the AI cannot be defeated - a human player can at most achieve a draw.