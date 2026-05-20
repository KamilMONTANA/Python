# 🌀 Day 6: Escaping the Maze

An interactive 2D grid-based maze game created with **Pygame**. The program generates a completely randomized, solvable maze layout on launch using the Depth-First Search (DFS) algorithm with backtracking, challenging the player to navigate from start to finish as fast as possible.

## 🎯 Project Goal
To implement algorithmic generation (DFS), understand the concept of stacks (LIFO), handle graphics/game loops, and intercept keyboard inputs using Pygame.

## ✨ Features
- **Dynamic Maze Generation:** The DFS generator carves paths through a grid of walls, guaranteeing that at least one valid path exists to the escape portal.
- **Fluid Keyboard Control:** Move a red player block using the standard keyboard arrow keys. Collision checks prevent traversing through active walls.
- **Escape Timer:** Tracks the duration of the run. Reaching the green exit square completes the run and shows a victory screen with the elapsed time in minutes and seconds.
- **Visual Rendering:** High-performance 2D cell-based graphics drawn directly on the Pygame canvas.

## 📂 Project Structure
- `EscapingTheMaze.py` – the singular script containing the grid/cell declarations, stack logic, DFS algorithm, and the main game render loop.

## 🎓 Key Learnings
- Declaring class models (`Cell`) that keep track of grid coordinates, wall state flags, and visitation status.
- Writing a recursive backtracking algorithm using an array-based stack to generate clean, solvable maze corridors.
- Setting up the **Pygame** engine: configuring viewport resolutions, setting window captions, drawing primitive borders/rects, rendering system fonts, and capping FPS via a game clock.
- Structuring a classic game frame cycle: *Process Events -> Read User Actions -> Update State -> Render -> Flip Screen Buffer*.

## ⚙️ Requirements & Installation
This project requires the external **Pygame** module.

### Install Pygame:
```bash
pip install pygame
```

### Run the Game:
```bash
python EscapingTheMaze.py
```
