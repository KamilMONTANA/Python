# 🏝️ Day 3: Treasure Island

An interactive, text-based adventure game written in Python. The player takes on the role of an adventurer exploring a mysterious, trap-laden island where every decision directly determines whether they survive to discover the treasure or meet a sudden end.

## 🎯 Project Goal
To practice complex conditional logic (`if`, `elif`, `else`), nested control flow, and user input validation with standard normalization.

## ✨ Features
- **Multi-stage Decision Making:** Every step requires careful choices (e.g., choosing paths, lighting torches, selecting cave tunnels, interacting with a dragon, and picking the right colored doors).
- **Atmospheric ASCII Art:** Displays custom graphic assets representing a dark forest, a cave, a guardian dragon, a skull, and a chest of gold.
- **Input Normalization:** Automatically handles trailing spaces and varying letter casings using `.strip().lower()`.

## 📂 Project Structure
- `main.py` – the main game file containing the story branching, ASCII graphics, and game-over routing.

## 🎓 Key Learnings
- Designing and nesting complex `if`/`elif`/`else` control paths.
- Normalizing user text entries to make the game flow robust against varying input styles.
- Working with multi-line raw strings (`r"""..."""`) for detailed console ASCII rendering.
- Using `sys.exit()` from the `sys` module to properly terminate the application.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python main.py
```
