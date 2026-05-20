# 🔑 Day 5: Password Generator

An advanced console-based password generator built in Python. The program allows users to customize the exact number of letters, numbers, and special symbols they want, and then generates a highly secure, completely randomized password.

## 🎯 Project Goal
To practice `for` loops, loop iterators using `range()`, dynamic array accumulation, and character scrambling using secure randomized APIs.

## ✨ Features
- **Total Customization:** Choose the exact count of characters, digits, and special symbols.
- **Enhanced Security:** Implements the modern Python `secrets` module (specifically `secrets.choice()`) to ensure cryptographically secure random selections.
- **Character Shuffling (Entropy Boost):** Applies an array scramble using `random.shuffle()` so the character sequence is entirely unpredictable.

## 📂 Project Structure
- `PasswordGenerator.py` – the main script containing all dictionary arrays, loop logic, and shuffling logic.

## 🎓 Key Learnings
- Constructing loops using `for ... in range(...)`.
- Using `.append()` to build arrays step-by-step and `"".join()` to collapse a character list into a single flat string.
- Using `random.shuffle()` to scramble list elements in place.
- Leveraging `secrets.choice()` for cryptographically strong value picking instead of `random.choice()`.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python PasswordGenerator.py
```
