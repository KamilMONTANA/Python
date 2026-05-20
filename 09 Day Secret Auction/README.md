# 🔨 Day 9: Secret Auction

A console-based secret auction (blind bidding) program built in Python. Bidders submit their names and bids privately, and the program automatically resolves the highest bidder once all offers are collected.

## 🎯 Project Goal
To practice utilizing Python dictionaries (`dict`), iterating over key-value pairs, dynamically appending records, and simulating screen-clear routines.

## ✨ Features
- **Unlimited Bidders:** The loop accepts any number of auction participants.
- **Bidding Privacy:** Prints 50 empty lines `\n` after each entry, pushing prior bids out of view so the next bidder cannot see previous amounts.
- **Automatic Winner Calculation:** A dedicated finder function iterates over the bids database to identify the highest bidder.
- **ASCII Art Welcome:** Renders a custom auction logo upon launching.

## 📂 Project Structure
- `main.py` – the main script controlling the bidding loops and winner calculation.
- `art.py` – contains the ASCII art logo imported at launch.

## 🎓 Key Learnings
- Constructing, writing, and reading keys and values inside dictionaries (`bids = {}`).
- Finding maximum values in a dataset by iterating over a dictionary keyset (`for bidder in bids`).
- Importing assets across files (`from art import logo`).
- Controlling loop structures with custom boolean flags (`bidding_finisher`).

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python main.py
```
