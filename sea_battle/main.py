import pygame
import pygame.mixer

pygame.init()
pygame.mixer.init()

shot_sound = pygame.mixer.Sound("shot.mp3")
explosion_sound = pygame.mixer.Sound("explosion.mp3")
fail_sound = pygame.mixer.Sound("fail.mp3")

pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
shot_sound.set_volume(0.6)

FPS = 120
START_LIVES = 10
START_AMMO = 10
SHIP_LIVES = 3

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Space Battle")
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

MAIN_BACKGROUND_COLOR = (255, 255, 255)
MISSILE_COLOR = (255, 0, 0)
SHIP_COLOR = (0, 0, 255)
GAME_OVER_COLOR = (0, 0, 0)
WIN_COLOR = (0, 255, 0)
TEXT_COLOR = (0, 0, 0)
background_color = MAIN_BACKGROUND_COLOR

font = pygame.font.Font(None, 36)

def reset_game():
    global missile_alive, missile_launched, missile_speed_x, missile_speed_y, missile
    missile_alive = True
    missile_launched = False
    missile_speed_x = 0
    missile_speed_y = 0
    missile = pygame.Rect(50, 50, 10, 10)
    missile.left = screen_rect.left
    missile.centery = screen_rect.centery

def restart_game():
    global ship, ship_lives, lives, ammo, ship_alive, background_color
    ship_lives = SHIP_LIVES
    lives = START_LIVES
    ammo = START_AMMO
    ship_alive = True
    background_color = MAIN_BACKGROUND_COLOR
    ship = pygame.Rect(300, 200, 50, 100)
    ship.right = screen_rect.right
    ship.centery = screen_rect.centery
    reset_game()

lives = START_LIVES
ammo = START_AMMO
ship_lives = SHIP_LIVES
ship_alive = True
missile_alive = True
missile_launched = False

ship = pygame.Rect(300, 200, 50, 100)
ship.right = screen_rect.right
ship.centery = screen_rect.centery

missile = pygame.Rect(50, 50, 10, 10)
missile.left = screen_rect.left
missile.centery = screen_rect.centery

missile_speed_x = 0
missile_speed_y = 0
ship_speed_y = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE and not missile_launched and ammo > 0:
                missile_launched = True
                missile_speed_y = 0
                missile_speed_x = 3
                shot_sound.play()
                ammo -= 1

            elif event.key == pygame.K_w and not missile_launched:
                missile_speed_y = -2

            elif event.key == pygame.K_s and not missile_launched:
                missile_speed_y = 2

    if missile_alive:
        missile.move_ip(missile_speed_x, missile_speed_y)

        if not missile.colliderect(screen_rect):
            missile_alive = False
            fail_sound.play()
            lives -= 1
            if lives > 0:
                reset_game()
            else:
                background_color = GAME_OVER_COLOR

        if ship_alive and missile.colliderect(ship):
            missile_alive = False
            ship_lives -= 1
            if ship_lives > 0:
                explosion_sound.play()
                reset_game()
            else:
                ship_alive = False
                explosion_sound.play()
                background_color = WIN_COLOR
                pygame.time.delay(1000)
                restart_game()

    if ship_alive:
        ship.move_ip(0, ship_speed_y)
        if ship.bottom > screen_rect.bottom or ship.top < screen_rect.top:
            ship_speed_y = -ship_speed_y

    screen.fill(background_color)

    if ship_alive:
        pygame.draw.rect(screen, SHIP_COLOR, ship)
    if missile_alive:
        pygame.draw.rect(screen, MISSILE_COLOR, missile)

    lives_text = font.render(f"Жизни: {lives}", True, TEXT_COLOR)
    ammo_text = font.render(f"Снаряды: {ammo}", True, TEXT_COLOR)
    ship_lives_text = font.render(f"Жизни корабля: {ship_lives}", True, TEXT_COLOR)

    screen.blit(lives_text, (10, 10))
    screen.blit(ammo_text, (screen_rect.width - 160, 10))
    screen.blit(ship_lives_text, (screen_rect.width // 2 - 110, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()