
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game to practice string manipulation, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a command-line Hangman game in Python. You may start from the provided starter file `assignments/games-in-python/starter-code.py` and implement the game logic so a player can guess letters to reveal a secret word.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list
- Accept single-letter guesses (case-insensitive) and validate input
- Show current progress with placeholders (e.g. `_ a _ _ a _`)
- Track and display remaining incorrect attempts (e.g. 6 attempts left)
- Record and display letters already guessed (both correct and incorrect)
- Do not penalize repeated guesses of the same letter
- End the game when the word is fully guessed or attempts are exhausted
- Display a clear win or lose message; reveal the secret word on loss

#### Starter Files

- `starter-code.py` — minimal scaffold for the game (in `assignments/games-in-python/`)

## Example Interaction

```
Welcome to Hangman!
_ _ _ _ _
Guesses left: 6
Guessed letters: 
Enter a letter: a
Good guess: _ a _ _ a _
Guesses left: 6
Guessed letters: a
```

## Getting Started

1. Open `assignments/games-in-python/starter-code.py` and implement the game logic.
2. Run the program with:

```bash
python assignments/games-in-python/starter-code.py
```

## Hints

- Keep the word list small while developing (5–15 words).
- Use a `set` to track guessed letters and avoid duplicate penalties.
- Make input handling robust: strip whitespace and convert to lowercase.

---

Follow the repository's assignment template and aim for clear, student-friendly instructions.
