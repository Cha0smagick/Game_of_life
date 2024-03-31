import pygame
import numpy as np

# Definición de variables globales
WIDTH, HEIGHT = 1280, 720
CELL_SIZE = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Función para inicializar la matriz de células aleatoriamente
def random_grid():
    return np.random.choice([0, 1], size=(ROWS, COLS), p=[0.5, 0.5])

# Función para actualizar el estado de las células en cada turno
def update(grid):
    new_grid = grid.copy()
    for i in range(1, ROWS-1):
        for j in range(1, COLS-1):
            neighbors = np.sum(grid[(i-1):(i+2), (j-1):(j+2)]) - grid[i, j]
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

# Función para dibujar la cuadrícula
def draw_grid(screen, grid):
    screen.fill(BLACK)
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Función principal del juego
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de la Vida")
    clock = pygame.time.Clock()

    grid = random_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update(grid)
        draw_grid(screen, grid)

        pygame.display.flip()
        clock.tick(10)  # Ajusta la velocidad del juego (cambiar si es necesario)

    pygame.quit()

if __name__ == "__main__":
    main()
