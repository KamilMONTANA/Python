# 🐢 Day 19: Instances, State, Higher Order Functions & Event Listeners

A pair of graphics projects built in Python using the **Turtle** module. The projects showcase event listeners (keyboard controls), higher-order functions (passing functions as arguments), and working with multiple object instances that track their states independently.

## 🎯 Project Goal
To learn and apply three core programming concepts: intercepting input events, implementing higher-order functions, and instantiating multiple objects from a single class blueprint while maintaining distinct individual attributes.

## ✨ Project Contents

### 1. 🐢 Turtle Race with Bets (`turtle_race_with_bets.py`)
- A race featuring six turtles of different colors.
- **Betting Prompt:** Prompts the user via a popup window to guess which turtle will win the race by entering a color.
- **Multiple Instances & States:** Spawns six distinct `Turtle` objects, places them at the starting line, and randomly moves them forward in a `while` loop.
- **Winner Determination:** The first turtle to cross the finish line (`xcor() > 230`) stops the race, and the program compares its color with the user's bet to print the result.

### 2. 🎨 Etch-a-Sketch (`etch_a_sketch.py`)
- A virtual sketching canvas controlled by the keyboard.
- **Controls:**
  - `W` – Move forward.
  - `S` – Move backward.
  - `A` – Turn counter-clockwise.
  - `D` – Turn clockwise.
  - `C` – Clear the drawing canvas and reset the turtle's position.

## 📂 Project Structure
- `turtle_race_with_bets.py` – the turtle racing game with user betting prompts.
- `etch_a_sketch.py` – the keyboard-controlled sketching application.

## 🎓 Key Learnings
- Binding key presses to execution triggers using `screen.listen()` and `screen.onkey()`.
- Passing functions as arguments to other functions (implementing **Higher-Order Functions**) using Python's `lambda` syntax.
- Visualizing class blueprints and individual object instances – six turtles are spawned from the same `Turtle` class, but each holds a unique color, coordinate pair, and moving speed.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python turtle_race_with_bets.py
```
