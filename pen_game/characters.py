import pygame
import random

def different_circles(screen):
    for i in range(10):
        width, height = screen.get_size()

        x = random.randint(0,width)
        y = random.randint(0,height)
        radius = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), radius)