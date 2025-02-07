import pygame
import all_colors
import random

pygame.init()

# Запускаем полноэкранный режим
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Меняем color_index случайным образом
    all_colors.color_index = random.randint(0, len(all_colors.COLORS) - 1)

    # Устанавливаем новый цвет фона
    if all_colors.color_index == 7:
        BACKGROUND = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        BACKGROUND = all_colors.COLORS[all_colors.color_index]

    # Обновляем экран
    screen.fill(BACKGROUND)
    pygame.display.flip()

    # Делаем задержку перед следующим кадром
    pygame.time.delay(500)  # 500 мс = 0.5 сек

pygame.quit()

