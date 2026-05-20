# 🎨 Day 18: Turtle & GUI

A collection of graphics projects built in Python utilizing the built-in **Turtle** library. The projects showcase advanced vector drawings, RGB color modes, random walks, and color palette extraction to recreate Damien Hirst's dot paintings.

## 🎯 Project Goal
To understand the fundamentals of computer graphics in Python, manage screen coordinates, work with RGB color arrays, and use external color profiling libraries.

## ✨ Project Contents

### 1. 🎨 Hirst Painting (`hirst-painting.py`)
- Recreates Damien Hirst's signature dot painting on a grid layout.
- Uses `colorgram` (commented out after extracting the palette) to scan an input image (`image.jpg`) for dominant colors.
- Draws a 19x19 grid of dots in random colors selected from the extracted color palette.

### 2. 🌀 Spirograph (`spirograph.py`)
- Generates a classic spirograph design.
- Dynamically turns the turtle by fractional degrees in a loop, drawing intersecting circles in random RGB colors.

### 3. 🎲 Random Walk (`turtleRandomWalk.py`)
- Simulates a random walk. The turtle steps in random directions (0, 90, 180, 270 degrees) at maximum speed with a thicker line width.
- Every segment is drawn in a unique, dynamically generated RGB color.

### 4. 🐢 Graphics Basics (`lesson1.py`)
- An introduction to the Turtle module, featuring shapes (from triangles up to decagons) with alternating colors.

## 📂 Project Structure
- `hirst-painting.py` – grid dots drawing program.
- `spirograph.py` – spirograph rendering program.
- `turtleRandomWalk.py` – random path drawing program.
- `lesson1.py` – introductory shapes program.
- `image.jpg` – reference image used for color extraction.

## 🎓 Key Learnings
- Controlling turtle movements (`forward`, `backward`, `left`, `right`, `dot`, `penup`, `pendown`, `speed`, `hideturtle`).
- Working with custom RGB color modes using `t.colormode(255)`.
- Using `colorgram` to extract dominant colors from reference images.
- Developing geometry-based algorithms (e.g., calculating angles for regular polygons using the formula `360 / sides`).

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python hirst-painting.py
```
