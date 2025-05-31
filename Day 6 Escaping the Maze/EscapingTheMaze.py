import pygame
import random
import sys
import time

print("Starting the game...")

# --- Ustawienia ---
CELL_SIZE = 20
COLS, ROWS = 25, 20
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
FPS = 30

# --- Klasy i funkcje labiryntu ---
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        # Walls: top, right, bottom, left
        self.walls = [True, True, True, True]
        self.visited = False

    def draw(self, surf):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.walls[0]:
            pygame.draw.line(surf, pygame.Color('white'), (x, y), (x + CELL_SIZE, y))
        if self.walls[1]:
            pygame.draw.line(surf, pygame.Color('white'), (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
        if self.walls[2]:
            pygame.draw.line(surf, pygame.Color('white'), (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE))
        if self.walls[3]:
            pygame.draw.line(surf, pygame.Color('white'), (x, y + CELL_SIZE), (x, y))

def index(x, y):
    if 0 <= x < COLS and 0 <= y < ROWS:
        return x + y * COLS
    return None

def remove_walls(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    if dx == 1:
        a.walls[3] = b.walls[1] = False
    elif dx == -1:
        a.walls[1] = b.walls[3] = False
    elif dy == 1:
        a.walls[0] = b.walls[2] = False
    elif dy == -1:
        a.walls[2] = b.walls[0] = False

def generate_maze():
    grid = [Cell(x, y) for y in range(ROWS) for x in range(COLS)]
    stack = []
    current = grid[0]
    current.visited = True
    while True:
        # 1. Znajdź nieodwiedzonych sąsiadów
        neighbors = []
        for dir, (dx, dy) in enumerate([(0,-1),(1,0),(0,1),(-1,0)]):
            ni = index(current.x + dx, current.y + dy)
            if ni is not None and not grid[ni].visited:
                neighbors.append(grid[ni])
        # 2. Jeśli są, wybierz losowo i usuń ściany, idź dalej
        if neighbors:
            next_cell = random.choice(neighbors)
            remove_walls(current, next_cell)
            stack.append(current)
            current = next_cell
            current.visited = True
        # 3. Jeśli brak, wróć do poprzedniego
        elif stack:
            current = stack.pop()
        else:
            break
    return grid

# --- Inicjalizacja gry ---
print("Initializing Pygame...")
pygame.init()
print("Creating window...")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()
print("Generating maze...")
grid = generate_maze()

# Gracz (start w lewym górnym rogu)
player_x, player_y = 0, 0

# Pozycja wyjścia
exit_pos = (COLS - 1, ROWS - 1)

# Czas startu gry
start_time = time.time()
escape_time = 0

# --- Pętla gry ---
running = True
won = False
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ruch gracza
    keys = pygame.key.get_pressed()
    cell = grid[index(player_x, player_y)]
    if keys[pygame.K_LEFT] and not cell.walls[3]:
        player_x -= 1
    if keys[pygame.K_RIGHT] and not cell.walls[1]:
        player_x += 1
    if keys[pygame.K_UP] and not cell.walls[0]:
        player_y -= 1
    if keys[pygame.K_DOWN] and not cell.walls[2]:
        player_y += 1

    # Sprawdzenie zwycięstwa
    if (player_x, player_y) == exit_pos and not won:
        won = True
        escape_time = time.time() - start_time

    # Rysowanie
    screen.fill(pygame.Color('black'))
    for c in grid:
        c.draw(screen)

    # Wyjście
    ex, ey = exit_pos
    pygame.draw.rect(screen, pygame.Color('green'),
                     (ex*CELL_SIZE+2, ey*CELL_SIZE+2, CELL_SIZE-4, CELL_SIZE-4))

    # Gracz
    pygame.draw.rect(screen, pygame.Color('red'),
                     (player_x*CELL_SIZE+2, player_y*CELL_SIZE+2, CELL_SIZE-4, CELL_SIZE-4))

    # Ekran zwycięstwa
    if won:
        font = pygame.font.SysFont(None, 48)
        minutes = int(escape_time // 60)
        seconds = int(escape_time % 60)
        text_lines = [
            "GRATULACJE!",
            f"Uciekłeś z labiryntu w czasie: {minutes}:{seconds:02d}"
        ]
        for i, line in enumerate(text_lines):
            text = font.render(line, True, pygame.Color('yellow'))
            rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 30 + i*60))
            screen.blit(text, rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
