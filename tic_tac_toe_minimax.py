"""
Tic-Tac-Toe: Human vs AI (Unbeatable using Minimax) with a basic GUI.

How to run:
    python tic_tac_toe_minimax.py

The human is X and the AI is O.
"""

import tkinter as tk


def create_board():
    """Create and return an empty 3x3 board represented by a list of 9 cells."""
    return [" " for _ in range(9)]


def check_winner(board, player):
    """Return True if the given player has any winning combination."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in winning_lines)


def is_draw(board):
    """Return True if the board is full and no player has won."""
    return " " not in board and not check_winner(board, "X") and not check_winner(board, "O")


def get_available_moves(board):
    """Return a list of indexes that are still empty."""
    return [index for index, cell in enumerate(board) if cell == " "]


def minimax(board, depth, is_maximizing):
    """
    Minimax explores every possible game path and returns a score.

    Scores from AI perspective:
    +1 = AI wins
    -1 = Human wins
     0 = Draw
    """
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for move in get_available_moves(board):
        board[move] = "X"
        score = minimax(board, depth + 1, True)
        board[move] = " "
        best_score = min(best_score, score)
    return best_score


def get_best_ai_move(board):
    """Find and return the optimal move index for AI using Minimax."""
    best_score = -float("inf")
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, depth=0, is_maximizing=False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


class TicTacToeGUI:
    """Simple Tkinter interface for human vs unbeatable AI Tic-Tac-Toe."""

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe: You (X) vs AI (O)")

        self.board = create_board()
        self.game_over = False

        self.status_label = tk.Label(
            root,
            text="Your turn (X)",
            font=("Arial", 14),
            pady=10,
        )
        self.status_label.pack()

        board_frame = tk.Frame(root)
        board_frame.pack(padx=10, pady=5)

        self.buttons = []
        for index in range(9):
            button = tk.Button(
                board_frame,
                text=" ",
                width=6,
                height=3,
                font=("Arial", 20),
                command=lambda i=index: self.human_move(i),
            )
            button.grid(row=index // 3, column=index % 3, padx=4, pady=4)
            self.buttons.append(button)

        self.restart_button = tk.Button(
            root,
            text="Restart Game",
            font=("Arial", 12),
            command=self.restart_game,
            pady=5,
        )
        self.restart_button.pack(pady=8)

    def update_board_ui(self):
        """Refresh all button texts from board state."""
        for index, value in enumerate(self.board):
            self.buttons[index].config(text=value)

    def set_board_enabled(self, enabled):
        """Enable or disable all board buttons."""
        state = tk.NORMAL if enabled else tk.DISABLED
        for index, button in enumerate(self.buttons):
            if enabled and self.board[index] == " ":
                button.config(state=tk.NORMAL)
            elif enabled and self.board[index] != " ":
                button.config(state=tk.DISABLED)
            else:
                button.config(state=state)

    def human_move(self, index):
        """Handle the human click move, then trigger AI move if game continues."""
        if self.game_over or self.board[index] != " ":
            return

        self.board[index] = "X"
        self.update_board_ui()

        if check_winner(self.board, "X"):
            self.status_label.config(text="You win!")
            self.game_over = True
            self.set_board_enabled(False)
            return

        if is_draw(self.board):
            self.status_label.config(text="It's a draw!")
            self.game_over = True
            self.set_board_enabled(False)
            return

        self.status_label.config(text="AI is thinking...")
        self.set_board_enabled(False)

        self.root.after(350, self.ai_move)

    def ai_move(self):
        """Compute and apply AI move using Minimax."""
        if self.game_over:
            return

        move = get_best_ai_move(self.board)
        if move is not None:
            self.board[move] = "O"

        self.update_board_ui()

        if check_winner(self.board, "O"):
            self.status_label.config(text="AI wins!")
            self.game_over = True
            self.set_board_enabled(False)
            return

        if is_draw(self.board):
            self.status_label.config(text="It's a draw!")
            self.game_over = True
            self.set_board_enabled(False)
            return

        self.status_label.config(text="Your turn (X)")
        self.set_board_enabled(True)

    def restart_game(self):
        """Reset game state and UI for a fresh round."""
        self.board = create_board()
        self.game_over = False
        self.update_board_ui()
        self.status_label.config(text="Your turn (X)")
        self.set_board_enabled(True)


def main():
    """Start the Tkinter GUI app."""
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
