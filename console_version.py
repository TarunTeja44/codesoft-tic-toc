"""
Console Tic-Tac-Toe: Human (X) vs AI (O)
AI uses Minimax with alpha-beta pruning and plays optimally.
"""

HUMAN = "X"
AI = "O"
EMPTY = " "
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def create_board():
    """Return a fresh empty board."""
    return [EMPTY] * 9


def available_moves(board):
    """Return indexes for all empty cells."""
    return [index for index, value in enumerate(board) if value == EMPTY]


def get_winner(board):
    """Return 'X' or 'O' if there is a winner, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    """Return True when board is full and no one has won."""
    return get_winner(board) is None and EMPTY not in board


def evaluate_game_state(board):
    """Return one of: 'X', 'O', 'draw', or None (game not finished)."""
    winner = get_winner(board)
    if winner is not None:
        return winner
    if is_draw(board):
        return "draw"
    return None


def print_board(board):
    """Print the board using a clean grid with position hints for empty cells."""
    print("\nCurrent Board:")
    for row in range(3):
        start = row * 3
        row_cells = []
        for col in range(3):
            index = start + col
            cell_value = board[index]
            row_cells.append(str(index + 1) if cell_value == EMPTY else cell_value)
        print(f" {row_cells[0]} | {row_cells[1]} | {row_cells[2]}")
        if row < 2:
            print("-----------")
    print()


def minimax(board, depth, is_ai_turn, alpha, beta):
    """
    Return score for the current board using Minimax.

    AI tries to maximize score, human tries to minimize score.
    Depth is used so the AI prefers quick wins and slower losses.
    """
    winner = get_winner(board)
    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if is_draw(board):
        return 0

    if is_ai_turn:
        best_score = -float("inf")
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score

    best_score = float("inf")
    for move in available_moves(board):
        board[move] = HUMAN
        score = minimax(board, depth + 1, True, alpha, beta)
        board[move] = EMPTY
        best_score = min(best_score, score)
        beta = min(beta, best_score)
        if beta <= alpha:
            break
    return best_score


def get_best_ai_move(board):
    """Return the best move index for AI."""
    best_score = -float("inf")
    best_move = None

    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, depth=0, is_ai_turn=False, alpha=-float("inf"), beta=float("inf"))
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def get_valid_human_move(board):
    """Prompt until user enters a legal move."""
    while True:
        raw_value = input("Your turn (X). Enter position (1-9): ").strip()

        if not raw_value.isdigit():
            print("Invalid input. Enter a number from 1 to 9.")
            continue

        position = int(raw_value)
        if position < 1 or position > 9:
            print("Invalid move. Position must be between 1 and 9.")
            continue

        move = position - 1
        if board[move] != EMPTY:
            print("Invalid move. That cell is already occupied.")
            continue

        return move


def announce_result(state):
    """Print final result message."""
    if state == HUMAN:
        print("You win. Nice game!")
    elif state == AI:
        print("AI wins. Better luck next time.")
    else:
        print("It's a draw.")


def play_one_game():
    """Play one full game session."""
    board = create_board()
    current_player = HUMAN

    print("\nTic-Tac-Toe: You are X, AI is O")

    while True:
        print_board(board)

        if current_player == HUMAN:
            move = get_valid_human_move(board)
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            move = get_best_ai_move(board)
            board[move] = AI
            print(f"AI chose position {move + 1}")

        state = evaluate_game_state(board)
        if state is not None:
            print_board(board)
            announce_result(state)
            return

        current_player = AI if current_player == HUMAN else HUMAN


def ask_play_again():
    """Return True if user wants another game."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def main():
    """Entry point for console game."""
    print("Welcome to Tic-Tac-Toe with Minimax AI")

    while True:
        play_one_game()
        if not ask_play_again():
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    main()
