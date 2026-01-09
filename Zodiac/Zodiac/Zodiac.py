import pygame
import sys
import random

# Game settings
TILE_SIZE = 24
MAZE = [
    "##########################",
    "#........#...............#",
    "#.####.#.#.####.#######..#",
    "#.#  #.#.#.#  #.#     #..#",
    "#.####.#.#.####.#####.#..#",
    "#........#........#...#..#",
    "####.###########.###.###.#",
    "#.......................#",
    "#.####.#####.#######.####",
    "#.#  #.#   #.#     #.#  #",
    "#.####.#####.#####.#.####",
    "#.......................#",
    "##########################"
]

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def draw_maze(screen, maze, dots):
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == "#":
                pygame.draw.rect(screen, BLUE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif dots[y][x]:
                pygame.draw.circle(screen, WHITE, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 4)

def get_valid_moves(x, y, maze):
    moves = []
    height = len(maze)
    width = len(maze[0])
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != "#":
            moves.append((nx, ny))
    return moves

def main():
    pygame.init()
    width = len(MAZE[0]) * TILE_SIZE
    height = len(MAZE) * TILE_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simple Pac-Man with Ghost")

    # Pac-Man start position
    pacman_x, pacman_y = 1, 1
    # Ghost start position
    ghost_x, ghost_y = len(MAZE[0]) - 2, len(MAZE) - 2
    clock = pygame.time.Clock()

    # Dots
    dots = [[col == '.' for col in row] for row in MAZE]
    total_dots = sum(row.count('.') for row in MAZE)
    score = 0

    running = True
    win = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if win and event.type == pygame.KEYDOWN:
                running = False

        if not win:
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT]:
                dx = -1
            elif keys[pygame.K_RIGHT]:
                dx = 1
            elif keys[pygame.K_UP]:
                dy = -1
            elif keys[pygame.K_DOWN]:
                dy = 1

            # Move Pac-Man if not hitting a wall
            new_x = pacman_x + dx
            new_y = pacman_y + dy
            if 0 <= new_y < len(MAZE) and 0 <= new_x < len(MAZE[0]) and MAZE[new_y][new_x] != "#":
                pacman_x, pacman_y = new_x, new_y

            # Eat dot
            if dots[pacman_y][pacman_x]:
                dots[pacman_y][pacman_x] = False
                score += 1

            # Move ghost randomly
            ghost_moves = get_valid_moves(ghost_x, ghost_y, MAZE)
            if ghost_moves:
                ghost_x, ghost_y = random.choice(ghost_moves)

            # Check collision
            if pacman_x == ghost_x and pacman_y == ghost_y:
                # Reset game on collision
                pacman_x, pacman_y = 1, 1
                ghost_x, ghost_y = len(MAZE[0]) - 2, len(MAZE) - 2
                dots = [[col == '.' for col in row] for row in MAZE]
                score = 0

            # Check win condition
            if score >= total_dots:
                win = True

        screen.fill(BLACK)
        draw_maze(screen, MAZE, dots)
        # Draw Pac-Man
        pygame.draw.circle(
            screen,
            YELLOW,
            (pacman_x * TILE_SIZE + TILE_SIZE // 2, pacman_y * TILE_SIZE + TILE_SIZE // 2),
            TILE_SIZE // 2 - 2
        )
        # Draw Ghost
        pygame.draw.circle(
            screen,
            RED,
            (ghost_x * TILE_SIZE + TILE_SIZE // 2, ghost_y * TILE_SIZE + TILE_SIZE // 2),
            TILE_SIZE // 2 - 2
        )

        # Display score
        font = pygame.font.SysFont(None, 24)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (5, 5))

        if win:
            win_font = pygame.font.SysFont(None, 48)
            win_text = win_font.render("You Win!", True, YELLOW)
            screen.blit(win_text, (width // 2 - win_text.get_width() // 2, height // 2 - win_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()