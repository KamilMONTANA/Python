# 🪓 Day 7: Hangman

A classic console-based "Hangman" word-guessing game written in Python. The player tries to reveal a randomly selected secret word letter by letter, working against a limited number of remaining attempts.

## 🎯 Project Goal
To practice dynamic loop states (`while`), check list items, update game strings on the fly, and implement index replacement logics.

## ✨ Features
- **Randomized Word Lists:** The game chooses a secret word from a collection of fruits inside the code.
- **Dynamic State Display:** Renders progress at each turn (e.g. `_ _ _ _`).
- **Lives/Attempts Tracker:** The player starts with 7 lives. Each incorrect letter guess subtracts 1 life and displays the updated count.
- **Input Cleaning:** Normalizes the typed character to lowercase automatically.

## 📂 Project Structure
- `hangman.py` – the complete game file containing the word lists, user loop, and letter match validation.

## 🎓 Key Learnings
- Building loops with complex compound termination conditions (wins when no `_` is left, losses when lives drop to 0).
- Using inline list comprehensions to compare, map, and merge correct guesses with existing hidden strings.
- Using `"".join()` to bundle a sequence of character flags into a readable output.
- Intercepting and validating custom user entries.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python hangman.py
```
