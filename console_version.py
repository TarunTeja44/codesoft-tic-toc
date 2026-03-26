"""
Tic-Tac-Toe: Human vs AI (Unbeatable Minimax) — Console Version

Features:
- Unbeatable AI using Minimax algorithm
- Clear board display with numbered positions
- "AI is thinking..." message
- "AI chose position X" transparency
- Input validation with error messages
- Beautiful winner announcement
- Play multiple games without restart

How to run:
    python console_version.py
"""


def create_board():
    """Create and return an empty 3x3 board."""
    return [" " for _ in range(9)]


def display_board(board):
    """Display the board in a professional 3x3 format."""
    print("\nCurrent Board:")
    for row in range(3):
        start = row * 3
        cells = board[start:start + 3]
        display_cells = []
        
        for idx, cell in enumerate(cells):
            pos = start + idx + 1
            # Show position number if cell is empty, else show X or O
            display_cells.append(cell if cell != " " else str(pos))
        
        print(f" {display_cells[0]} | {display_cells[1]} | {display_cells[2]} ")
        if row < 2:
            print("-----------")
    print()


def check_winner(board, player):
    """Return True if the given player has won."""
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] == player:
            return True, (a, b, c)
    return False, None


def is_draw(board):
    """Return True if it's a draw."""
    return " " not in board and not check_winner(board, "X")[0] and not check_winner(board, "O")[0]


def get_available_moves(board):
    """Return list of empty cell indices."""
    return [i for i, cell in enumerate(board) if cell == " "]


def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm: evaluates all possible future states.
    AI maximizes score; human minimizes it.
    Scores: AI win=+1, Human win=-1, Draw=0
    """
    winner, _ = check_winner(board, "O")
    if winner:
        return 1
    
    winner, _ = check_winner(board, "X")
    if winner:
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
    """Find the optimal move for AI using Minimax."""
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


def get_human_move(board):
    """Get and validate human input."""
    while True:
        try:
            move_text = input("Your turn (X). Enter position (1-9): ").strip()
            
            if not move_text.isdigit():
                print("❌ Invalid input! Please enter a NUMBER from 1 to 9.")
                continue
            
            position = int(move_text)
            
            if position < 1 or position > 9:
                print(f"❌ Invalid position! Choose a number from 1 to 9, not {position}.")
                continue
            
            index = position - 1
            
            if board[index] != " ":
                print(f"❌ Cell {position} is already occupied! Try another position.")
                continue
            
            return index
        
        except ValueError:
            print("❌ Invalid input! Please enter a number from 1 to 9.")


def play_one_game():
    """Play one complete game."""
    board = create_board()
    
    print("\n" + "="*50)
    print("  TIC-TAC-TOE: YOU (X) vs AI (O)")
    print("="*50)
    print("\n🤖 AI Power: Unbeatable Minimax Algorithm")
    print("📍 Positions: 1-9 (numbered on board)")
    
    current_player = "X"  # Human starts

    while True:
        display_board(board)
        
        if current_player == "X":
            # Human's turn
            move = get_human_move(board)
            board[move] = "X"
            
            winner, winning_line = check_winner(board, "X")
            if winner:
                display_board(board)
                print("🎉 YOU WIN! Great job!")
                return
            
            if is_draw(board):
                display_board(board)
                print("🤝 DRAW! Nobody wins this round.")
                return
            
            current_player = "O"
        
        else:
            # AI's turn
            print("🤖 AI is thinking...")
            move = get_best_ai_move(board)
            board[move] = "O"
            
            print(f"✅ AI chose position {move + 1}")
            
            winner, winning_line = check_winner(board, "O")
            if winner:
                display_board(board)
                print("🎯 AI WINS! Three in a row!")
                print("💡 Better luck next time. The Minimax algorithm is unbeatable!")
                return
            
            if is_draw(board):
                display_board(board)
                print("🤝 DRAW! Nobody wins this round.")
                return
            
            current_player = "X"


def ask_restart():
    """Ask if user wants to play again."""
    while True:
        answer = input("\n▶ Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("❌ Please enter 'y' or 'n'.")


def main():
    """Main game loop."""
    print("\n" + "╔" + "="*48 + "╗")
    print("║  Welcome to Tic-Tac-Toe with Unbeatable AI  ║")
    print("║  Powered by Minimax Algorithm              ║")
    print("╚" + "="*48 + "╝\n")
    
    while True:
        play_one_game()
        if not ask_restart():
            print("\n✨ Thanks for playing! Better luck next time. ✨\n")
            break


if __name__ == "__main__":
    main()
