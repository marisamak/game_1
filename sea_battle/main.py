import pygame
import pygame.mixer
pygame. init()
pygame.mixer.init()

shot_sound = pygame.mixer.Sound("shot.mp3")
explosion_sound = pygame.mixer.Sound("explosion.mp3")
fail_sound = pygame.mixer.Sound("fail.mp3")

pygame.mixer.music.load("soundtrack.mp3")

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
shot_sound.set_volume(0.6)

FPS = 120

clock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 480))

screen_rect = screen.get_rect()

MAIN_BACKGROUND_COLOR = (255, 255, 255)
MISSILE_COLOR = (255, 0, 0)
SHIP_COLOR = (0, 0, 255)
GAME_OVER_COLOR = (0, 0, 0)
WIN_COLOR = (0, 255, 0)
background_color = MAIN_BACKGROUND_COLOR

ship = pygame.Rect(300, 200, 50, 100)

ship.right = screen_rect.right
ship.centery = screen_rect.centery

missile = pygame.Rect(50, 50, 10, 10)

missile.left = screen_rect.left
missile.centery = screen_rect.centery

missile_speed_x = 0
missile_speed_y = 0

ship_speed_y = 1

ship_alive = True
missile_alive = True

missile_launched = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not missile_launched:
                missile_launched = True
                missile_speed_y = 0
                missile_speed_x = 3
                pygame.mixer.music.stop()
                shot_sound.play()

            elif event.key == pygame.K_w and not missile_launched:
                missile_speed_y = -2

            elif event.key == pygame.K_s and not missile_launched:
                missile_speed_y = 2

    if missile_alive:
        missile.move_ip(missile_speed_x, missile_speed_y)

        if not missile.colliderect(screen_rect):
            missile_alive = False
            background_color = GAME_OVER_COLOR
            pygame.mixer.music.stop()
            fail_sound.play()

        if ship_alive and missile.colliderect(ship):
            missile_alive = False
            ship_alive = False
            background_color = WIN_COLOR
            explosion_sound.play()

    if ship_alive:
        ship.move_ip(0, ship_speed_y)

        if ship.bottom > screen_rect.bottom or ship.top < screen_rect.top:
            ship_speed_y = -ship_speed_y

    screen.fill(background_color)

    if ship_alive:
        pygame.draw.rect(screen, SHIP_COLOR, ship)

    if missile_alive:
        pygame.draw.rect(screen, MISSILE_COLOR, missile)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
