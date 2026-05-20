# ☕ Day 15: Coffee Machine (Procedural)

A coffee machine simulator built in Python using a procedural programming paradigm. The application tracks water, milk, and coffee resources, accepts various coin nominations, provides change, and tracks cumulative profit from espresso, latte, and cappuccino orders.

## 🎯 Project Goal
To practice designing clean procedural code, dividing scripts into separate modules, mutating global variables, managing dictionary values, and conducting floating-point arithmetic.

## ✨ Features
- **Beverage Menu:** Serves espresso, latte, and cappuccino, each with distinct ingredient ratios and prices.
- **Resource Verification:** Verifies ingredient levels before prompting the user for money.
- **Coin Processing:** Accepts quarters ($0.25), dimes ($0.10), nickels ($0.05), and pennies ($0.01), calculates the total, and validates the payment.
- **Change Dispensing:** Automatically calculates and dispenses the exact change, rounded to two decimal places.
- **Status Reporting:** Typing `report` prints the current resource quantities (water, milk, coffee) and total profits.
- **Maintenance Turn-off:** A secret maintenance command (`off`) powers down the simulator (terminates the script).

## 📂 Project Structure
- `main.py` – coordinates the main customer prompts, coin values, ingredient checks, and brewing logs.
- `data.py` – contains the beverage recipe dictionary, resource quantities, and total profit margins.
- `Coffee+Machine+Program+Requirements.pdf` – the business requirements document guiding the program's development.

## 🎓 Key Learnings
- Designing procedural solutions with decoupled helper functions.
- Managing application states using global dict variables from external files (`data.py`).
- Operating on floating-point currencies safely and outputting formatted results (`f"${change:.2f}"`).
- Implementing multi-resource verification checks using loops.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python main.py
```

**Special Commands:**
* `report` – prints the machine's current status.
* `off` – powers off the machine.
