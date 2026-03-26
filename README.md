# Tic-Tac-Toe: Human vs Unbeatable AI

A beginner-friendly Python implementation of Tic-Tac-Toe with an **unbeatable AI** powered by the **Minimax algorithm**.

## Features

✨ **Unbeatable AI** – Uses the Minimax algorithm to make optimal moves every time  
🎮 **Two Versions Available**:
  - **GUI Version** (`tic_tac_toe_minimax.py`) – Click-based with Tkinter
  - **Console Version** (`console_version.py`) – Terminal-based with detailed messages  
🤖 **Smart AI Messaging** – Shows "AI is thinking..." and "AI chose position X"  
♻️ **Restart Anytime** – Play multiple games in one session  
✅ **Bulletproof Input Validation** – No invalid moves accepted + error messages  
🏆 **Clear Win/Loss/Draw Detection** – Game state always transparent  
📊 **Professional Board Display** – Numbered positions + formatted output  

## How It Works

### 🎯 Minimax Algorithm — The Brain of Unbeatable AI

**What is Minimax?**

Minimax is a decision-making algorithm where the AI tries to **maximize** its chances of winning while **minimizing** the opponent's chances. It's like a chess master thinking many moves ahead!

**Key Concept:**

Instead of making random moves, the AI:
1. Imagines every possible future game state (like a game tree)
2. Scores each outcome:
   - AI wins = +1
   - Human wins = -1
   - Draw = 0
3. Works backward from end states to current move
4. Chooses the move that guarantees the best result

**How It Makes Winning Moves:**

```
AI's Turn (Maximizing):
  ├─ Move A → Best outcome = +1 (AI wins)  ← Choose this!
  ├─ Move B → Best outcome = 0 (Draw)
  └─ Move C → Best outcome = -1 (AI loses)

Human's Turn (Minimizing):
  ├─ Move A → Best outcome = -1 (AI loses)  ← They choose this
  ├─ Move B → Best outcome = 0 (Draw)
  └─ Move C → Best outcome = +1 (AI wins)
```

**Why This Makes AI Unbeatable:**

- ✅ Evaluates **all** possible moves
- ✅ Plays defensively (blocks your wins)
- ✅ Plays offensively (creates winning threats)
- ✅ Never makes a mistake
- ✅ Guaranteed to win or force a draw

**Interview Question Ready:**
> "Minimax ensures optimal gameplay through recursive game-tree evaluation, eliminating suboptimal moves by backward induction from terminal states to the current position."

## Requirements

- Python 3.7+
- Tkinter (included with standard Python)
- No external libraries needed

## How to Run

### Version 1: GUI (Tkinter) — Click-Based
```bash
python tic_tac_toe_minimax.py
```
- Click empty cells to make your move
- AI responds instantly with optimal moves
- Click "Restart Game" to play again

### Version 2: Console — Terminal-Based (RECOMMENDED FOR INTERVIEW)
```bash
python console_version.py
```
- Enter move positions as numbers 1-9
- See "AI is thinking..." and "AI chose position X" messages
- Better for demonstrating algorithm understanding
- Shows input validation feedback
- Professional formatted board output

## Project Files

```
codesoft-tic-toc/
├── tic_tac_toe_minimax.py    → GUI version (Tkinter)
├── console_version.py         → Console version (Terminal)
├── README.md                  → This file
└── __pycache__/              → Compiled Python cache (ignore)
```

## Core Algorithm Structure

Both versions share the same **Minimax AI logic**:

```
create_board()              # Initialize empty board
check_winner()              # Detect winning combinations
get_available_moves()       # List empty cells
minimax()                   # Core algorithm (recursive game tree evaluation)
get_best_ai_move()          # Find optimal AI move using Minimax
get_human_move()            # Handle user input with validation
play_one_game()             # Main game loop
```

## Example Gameplay

### GUI Version (Tkinter):
Click cells to play. AI responds instantly with optimal moves.

### Console Version (Terminal):

```
╔════════════════════════════════════════╗
║  TIC-TAC-TOE: YOU (X) vs AI (O)       ║
╚════════════════════════════════════════╝

Current Board:
 ① | ② | ③
-----------
 ④ | ⑤ | ⑥
-----------
 ⑦ | ⑧ | ⑨

Your turn (X). Enter position (1-9): 5

Current Board:
 ① | ② | ③
-----------
 ④ | X | ⑥
-----------
 ⑦ | ⑧ | ⑨

AI is thinking...
AI chose position 1

Current Board:
 O | ② | ③
-----------
 ④ | X | ⑥
-----------
 ⑦ | ⑧ | ⑨

Your turn (X). Enter position (1-9): 9

Current Board:
 O | ② | ③
-----------
 ④ | X | ⑥
-----------
 ⑦ | ⑧ | X

AI is thinking...
AI chose position 7

Current Board:
 O | ② | ③
-----------
 ④ | X | ⑥
-----------
 O | ⑧ | X

AI is thinking...
AI chose position 4

Current Board:
 O | ② | ③
-----------
 O | X | ⑥
-----------
 O | ⑧ | X

🎯 AI WINS! Three in a row: (1, 4, 7)
Better luck next time!

Play again? (y/n): n
Thanks for playing!
```

**Key Features Shown:**
- ✅ Clear numbered board positions
- ✅ "AI is thinking..." during computation
- ✅ "AI chose position X" transparency
- ✅ Input validation (no invalid moves accepted)
- ✅ Beautiful winner announcement
- ✅ Restart option

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
