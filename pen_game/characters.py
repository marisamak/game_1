import pygame
import random

def different_circles(screen):
    for i in range(10):
        x = random.randint(0,640)
        y = random.randint(0,480)
        radius = random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), radius)