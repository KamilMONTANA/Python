# 📈 Day 14: Higher Lower (Instagram Edition)

An interactive console game inspired by the popular web game "Higher Lower". Bidders compare two randomly selected accounts from social media and try to guess which has more followers on Instagram.

## 🎯 Project Goal
To practice handling structured data (arrays of dictionary objects), preventing duplicate randomized choices in a single round, tracking score milestones, and decoupling scripts into distinct files.

## ✨ Features
- **Streak-based Play:** The game session continues as long as the player chooses the correct answer.
- **Dynamic Database Entries:** Competitors are dynamically loaded from a curated dataset list in `data.py`.
- **Score Tracker:** Displays the user's current score after every successful round.
- **Graphic Assets:** Leverages detailed ASCII logo displays and a custom "VS" banner loaded from `art.py`.

## 📂 Project Structure
- `main.py` – coordinates the comparison logic, reads user selections, and handles round progression.
- `data.py` – contains the database of popular accounts, including their descriptions, origins, and exact follower counts.
- `art.py` – stores the graphic ASCII assets for the game layout.

## 🎓 Key Learnings
- Building loop states that terminate as soon as an incorrect input or guess is processed.
- Traversing complex dictionary fields nested inside standard lists.
- Cleaning up user entries using string casing standardizers (`guess.upper()`).
- Modularizing code by moving static data and ASCII files to helper modules.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python main.py
```
