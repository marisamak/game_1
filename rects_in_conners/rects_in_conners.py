import colors
import random
import pygame
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

width = 100
height = 75

rects = []

running = True

rects.append(pygame.Rect(0, 0, width, height))

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].topright = (screen_width, 0)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, screen_height)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (screen_width, screen_height)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].center = (screen_width//2, screen_height//2)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    wallpaper = colors.different_colors_()
    screen.fill(wallpaper)

    for rect in rects:
        color = colors.different_colors_()
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    pygame.time.delay(random.randint(500, 700))

pygame.quit()
