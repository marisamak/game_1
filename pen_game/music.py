import pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('песня.mp3')
pygame.mixer.music.play(-1)