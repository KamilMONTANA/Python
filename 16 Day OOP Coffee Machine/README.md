# ☕ OOP Coffee Machine

A coffee machine simulator built following Object-Oriented Programming (OOP) principles in Python. This project demonstrates the practical application of classes, objects, and their interactions to create a scalable and readable application.

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements & Installation](#-requirements--installation)
- [How to Use](#-how-to-use)

## 🎯 About the Project

This simulator allows users to order one of three types of coffee (espresso, latte, cappuccino). The program manages limited resources (water, milk, coffee) and handles the payment process using virtual coins (quarters, dimes, nickels, pennies). The entire system is designed modularly, making it easy to maintain and expand.

## ✨ Features

- **Menu Management:** Dynamically generates the list of available drinks.
- **Resource Monitoring:** Automatically checks if there are enough ingredients before starting the brewing process.
- **Payment System:** Processes coin inputs, calculates change, and verifies transaction success.
- **Reporting:** Generates real-time reports on ingredient levels and total profits.
- **Service Mode:** Allows the machine to be powered down using the `off` command.

## 🏗 Project Structure

The project is divided into four main modules:

1. **`main.py`** – The entry point of the application, coordinating interaction between all modules.
2. **`menu.py`** – Contains the `MenuItem` and `Menu` classes responsible for the beverage database.
3. **`coffee_maker.py`** – Contains the `CoffeeMaker` class which manages resources and the coffee-making process.
4. **`money_machine.py`** – Contains the `MoneyMachine` class for handling coins and financial records.

## ⚙ Requirements & Installation

- **Python 3.x**
- No external dependencies (uses Python Standard Library only).

### Installation

1. Clone the repository or download the source files.
2. Open your terminal in the project directory.
3. Run the application:

   ```bash
   python lesson1.py
   ```

## 🚀 How to Use

1. Upon running, enter the name of the drink you'd like to order: `espresso`, `latte`, or `cappuccino`.
2. If resources are sufficient, you will be prompted to insert coins.
3. The program calculates if the amount is enough and provides change if necessary.
4. Once payment is confirmed, the machine prepares your coffee.

**Special Commands:**

- `report` – Displays the current status of water, milk, coffee, and total earnings.
- `off` – Shuts down the machine (exits the program).

---
*Created for educational purposes to demonstrate the power of Object-Oriented Programming.*
