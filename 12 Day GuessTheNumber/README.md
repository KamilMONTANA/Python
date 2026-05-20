# 🎯 Day 12: Guess The Number

An interactive console game where the player attempts to guess a randomly chosen integer between 1 and 100. The player selects a difficulty setting which determines their maximum attempts.

## 🎯 Project Goal
To learn and apply variable scope in Python (Local vs. Global Scope), define global constants, and utilize control loops with conditional limit counters.

## ✨ Features
- **Difficulty Selection:**
  - **Easy:** 10 attempts to guess the number.
  - **Medium:** 5 attempts to guess the number.
  - **Hard:** 3 attempts to guess the number.
- **Dynamic Hints:** Informs the player if their guess was too high or too low.
- **ASCII Art Banner:** Displays a game logo loaded from `logo.py`.

## 📂 Project Structure
- `main.py` – coordinates the attempt decrement loops, random number evaluations, and winning matches.
- `logo.py` – contains the ASCII art string representing the game's logo.

## 🎓 Key Learnings
- Understanding the difference between Local and Global scope namespaces in Python.
- Applying proper styling guides to global constants (declaring them in *UPPERCASE*).
- Implementing conditional loop cycles and using the Python `while ... else` construct to catch failure states once attempts run out.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python main.py
```
