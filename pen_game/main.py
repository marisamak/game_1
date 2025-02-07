import pygame
import all_colors
import random
import music
import characters

pygame.init()

size = (0, 0)

pygame.display.set_caption("Game")

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

running = True

music.play_music()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    BACKGROUND = all_colors.different_colors_()

    screen.fill(BACKGROUND)

    characters.different_circles(screen)

    pygame.display.flip()

    pygame.time.delay(random.randint(300, 500))

pygame.quit()
