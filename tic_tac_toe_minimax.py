"""
Tkinter Tic-Tac-Toe: Human (X) vs AI (O)
AI uses Minimax with alpha-beta pruning and plays optimally.
"""

import tkinter as tk

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


def minimax(board, depth, is_ai_turn, alpha, beta):
    """Return score for current board using Minimax with alpha-beta pruning."""
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
    """Return best move index for AI."""
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


class TicTacToeGUI:
    """GUI application for playing Tic-Tac-Toe against Minimax AI."""

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe: You (X) vs AI (O)")

        self.board = create_board()
        self.game_over = False

        self.status_label = tk.Label(root, text="Your turn (X)", font=("Arial", 14), pady=10)
        self.status_label.pack()

        self.board_frame = tk.Frame(root)
        self.board_frame.pack(padx=10, pady=5)

        self.buttons = []
        self._build_board_buttons()

        self.restart_button = tk.Button(
            root,
            text="Restart Game",
            font=("Arial", 12),
            command=self.restart_game,
            pady=5,
        )
        self.restart_button.pack(pady=8)

    def _build_board_buttons(self):
        """Create all board buttons once."""
        for index in range(9):
            button = tk.Button(
                self.board_frame,
                text=" ",
                width=6,
                height=3,
                font=("Arial", 20),
                command=lambda i=index: self.handle_human_move(i),
            )
            button.grid(row=index // 3, column=index % 3, padx=4, pady=4)
            self.buttons.append(button)

    def set_status(self, message):
        """Update top status message."""
        self.status_label.config(text=message)

    def refresh_board(self):
        """Update button texts and enabled state from current board."""
        for index, button in enumerate(self.buttons):
            value = self.board[index]
            button.config(text=value)

            if self.game_over or value != EMPTY:
                button.config(state=tk.DISABLED)
            else:
                button.config(state=tk.NORMAL)

    def finish_if_game_over(self):
        """Update status and stop the game if terminal state is reached."""
        state = evaluate_game_state(self.board)
        if state is None:
            return False

        self.game_over = True
        if state == HUMAN:
            self.set_status("You win!")
        elif state == AI:
            self.set_status("AI wins!")
        else:
            self.set_status("It's a draw!")

        self.refresh_board()
        return True

    def handle_human_move(self, index):
        """Apply human move and schedule AI move when needed."""
        if self.game_over or self.board[index] != EMPTY:
            return

        self.board[index] = HUMAN
        self.refresh_board()

        if self.finish_if_game_over():
            return

        self.set_status("AI is thinking...")
        for button in self.buttons:
            button.config(state=tk.DISABLED)

        self.root.after(350, self.handle_ai_move)

    def handle_ai_move(self):
        """Compute and apply one AI move."""
        if self.game_over:
            return

        ai_move = get_best_ai_move(self.board)
        if ai_move is not None:
            self.board[ai_move] = AI

        self.refresh_board()

        if self.finish_if_game_over():
            return

        self.set_status("Your turn (X)")

    def restart_game(self):
        """Reset board and UI for a new round."""
        self.board = create_board()
        self.game_over = False
        self.set_status("Your turn (X)")
        self.refresh_board()


def main():
    """Start GUI application."""
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
