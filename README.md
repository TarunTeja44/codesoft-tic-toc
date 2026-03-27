# Tic-Tac-Toe AI with Minimax

A beginner-to-intermediate Python project where a human plays Tic-Tac-Toe against an AI that uses the Minimax algorithm.

The repository includes:
- Console version for clear step-by-step interaction
- Tkinter GUI version for a visual desktop experience

## Features

- Unbeatable AI using Minimax (with alpha-beta pruning)
- Clear win, loss, and draw detection
- Input validation for console mode
- User-friendly messages such as AI is thinking...
- Restart support in both console and GUI versions
- Clean, modular, beginner-friendly code structure

## Minimax in Simple Terms

Minimax is a decision-making algorithm used in turn-based games.

- The AI assumes both players make the best possible moves.
- On AI turns, it chooses moves that maximize its score.
- On human turns, it assumes the human chooses moves that minimize the AI's score.

In this project, game outcomes are scored as:
- AI win: positive score
- Human win: negative score
- Draw: zero

Because Tic-Tac-Toe is small enough to search fully, Minimax can evaluate all possible outcomes and choose an optimal move every time.

## Project Structure

- `console_version.py`: Console-based game
- `tic_tac_toe_minimax.py`: Tkinter GUI game
- `index.html`: Browser version (optional)
- `.gitignore`: Python-focused ignore rules

## How to Run

### 1. Console version

```bash
python console_version.py
```

You will enter moves by typing numbers 1 to 9.

### 2. GUI version (Tkinter)

```bash
python tic_tac_toe_minimax.py
```

Click a cell to place X. The AI responds as O.

## Console Gameplay Example

```text
Welcome to Tic-Tac-Toe with Minimax AI

Tic-Tac-Toe: You are X, AI is O

Current Board:
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Your turn (X). Enter position (1-9): 5
AI is thinking...
AI chose position 1
```

## What Was Improved

- Removed duplicated logic by using reusable helper functions
- Unified winner/draw state checks into shared game-state functions
- Refactored Minimax for readability and efficiency
- Improved naming for better code clarity
- Simplified GUI flow with reusable update and finish handlers
- Added clean `.gitignore` and removed unnecessary tracked files

## Future Improvements

- Add difficulty modes (easy, medium, unbeatable)
- Add scoreboard (wins/losses/draws)
- Highlight the winning line in GUI
- Add unit tests for game logic functions
- Package as a small desktop app executable

## License

This project is for learning and internship practice. You may reuse and modify it for educational purposes.
