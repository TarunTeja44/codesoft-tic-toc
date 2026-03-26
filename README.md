# Tic-Tac-Toe: Human vs Unbeatable AI

A beginner-friendly Python implementation of Tic-Tac-Toe with an **unbeatable AI** powered by the **Minimax algorithm**.

## Features

✨ **Unbeatable AI** – Uses the Minimax algorithm to make optimal moves every time  
🎮 **Simple GUI** – Clean, easy-to-use interface built with Tkinter  
🤖 **Smart Status Messages** – Shows "AI is thinking..." during AI moves  
♻️ **Restart Anytime** – Play multiple games without restarting the program  
✅ **Input Validation** – Invalid moves are blocked automatically  
🏆 **Clear Win/Loss/Draw Detection** – Game state is always clear  

## How It Works

### Minimax Algorithm (Simple Explanation)

The Minimax algorithm evaluates every possible move by looking ahead at all future game states:

1. **Scoring**: Each game outcome gets a score:
   - AI wins = +1
   - Human wins = -1  
   - Draw = 0

2. **Strategy**:
   - On AI's turn → Choose the move that **maximizes** (increases) the score
   - On human's turn → Assume they choose moves that **minimize** (decrease) the score for AI

3. **Result**: The AI always picks the move that leads to the best outcome, making it impossible to beat.

## Requirements

- Python 3.7+
- Tkinter (included with standard Python)
- No external libraries needed

## How to Run

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/TarunTeja44/codesoft-tic-toc.git
   cd codesoft-tic-toc
   ```

2. **Run the game**:
   ```bash
   python tic_tac_toe_minimax.py
   ```

3. **Play**:
   - You are **X**, AI is **O**
   - Click empty cells to make your move
   - AI will respond automatically
   - Click "Restart Game" to play again

## Code Structure

```
tic_tac_toe_minimax.py
├── create_board()           # Initialize empty board
├── check_winner()           # Detect winning combinations
├── get_available_moves()    # List empty cells
├── minimax()                # Core algorithm (unbeatable AI)
├── get_best_ai_move()       # Find optimal AI move
└── TicTacToeGUI             # Tkinter GUI class
    ├── __init__()           # Build interface
    ├── human_move()         # Handle player clicks
    ├── ai_move()            # Execute AI logic
    └── restart_game()       # Reset board
```

## Example Gameplay

```
Welcome to Tic-Tac-Toe!
You are X, AI is O.

Current Board:
 X | O | X
-----------
 O |  X |  
-----------
   |   | O

AI wins! Better luck next time.

Play again? [Restart Game button]
```

## Why Minimax?

- **Optimal Moves**: The AI never makes a bad decision
- **Educational**: Great for learning game theory and recursion
- **Unbeatable**: Guaranteed to win or draw (never loses)
- **Simple Rules**: Tic-Tac-Toe is small enough to evaluate all possibilities

## Learning Resources

If you want to understand Minimax deeper, check out:
- How Minimax works in game theory
- Recursion and tree traversal
- Game AI fundamentals

## Contributing

This is a learning project. Feel free to fork and improve it!

## License

Open source – feel free to use and modify.

---

**Author**: Codsoft Tic-Toc  
**Contact**: puligillatarunteja@gmail.com
