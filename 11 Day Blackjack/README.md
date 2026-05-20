# 🃏 Day 11: Blackjack Capstone

A console-based Blackjack simulation game built in Python. The game incorporates standard casino rules, including dynamic Ace valuation (1 or 11 points), artificial dealer cards hitting (must hit under 17), and hand score tracking.

## 🎯 Project Goal
As the first major "Capstone Project" of the bootcamp, the objective was to synthesize all core concepts (loops, functions, lists, states, variables, nested conditions) into a polished and well-structured application.

## ✨ Features
- **Dynamic Aces:** The `calculate_score` function checks if the player's total is over 21 and evaluates Aces as 1 instead of 11 if necessary to prevent bust.
- **AI Dealer:** The dealer automatically hits until their hand score reaches a minimum of 17 points.
- **Interactive Player Actions:** Prompts the player to `Hit` (draw) or `Stand` (pass) while showing their hand and the dealer's first card.
- **Rematches:** Players can immediately start a new round without restarting the terminal.

## 📂 Project Structure
- `main.py` – contains the full card scoring system, game loops, hit/stand triggers, and winner resolution formulas.

## 🎓 Key Learnings
- Managing game states and deck lists in memory.
- Designing functions with complex internal control paths (such as the Ace checking loops in `calculate_score`).
- Documenting Python functions using professional `docstrings`.
- Splitting major logic flows into decoupled, reusable functions (`calculate_score`, `check_bust`, `dealer_hit`, `show_result`) to keep code readable and maintainable.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python main.py
```
