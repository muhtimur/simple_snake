import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры окна и ячеек сетки
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Инициализация змейки
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (GRID_SIZE, 0)

# Инициализация еды
food = (WIDTH // 2, HEIGHT // 2)

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Обработка клавиш для управления змейкой
    if keys[pygame.K_UP] and snake_direction != (0, GRID_SIZE):
        snake_direction = (0, -GRID_SIZE)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -GRID_SIZE):
        snake_direction = (0, GRID_SIZE)
    elif keys[pygame.K_LEFT] and snake_direction != (GRID_SIZE, 0):
        snake_direction = (-GRID_SIZE, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-GRID_SIZE, 0):
        snake_direction = (GRID_SIZE, 0)

    # Обновление положения змейки
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Проверка столкновения с границами экрана
    if (
        new_head[0] < 0 or
        new_head[0] >= WIDTH or
        new_head[1] < 0 or
        new_head[1] >= HEIGHT
    ):
        pygame.quit()
        sys.exit()

    # Проверка столкновения с самой собой
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()

    # Проверка поедания еды
    if new_head == food:
        food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
    else:
        snake.pop()

    # Отрисовка
    screen.fill(BLACK)

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    #Отрисовка еды
    pygame.draw.rect(screen, WHITE, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    pygame.display.flip()

    # Задержка (регулируйте, чтобы изменить скорость)
    pygame.time.delay(100)
