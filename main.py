# Jovan Sandhu (A01201367)
# Car Racing Game
# ACIT 2515


from controllers import PlayerCar, draw_images, resize, race_time
import pygame
import time

pygame.init()

BACKGROUND = resize(pygame.image.load("images/grass.png"), 3.5)
TRACK = pygame.image.load("images/track.png")

BORDER = pygame.image.load("images/border.png")
BORDER_MASK = pygame.mask.from_surface(BORDER)

FINISH = resize(pygame.image.load("images/finish.png"), 0.2)
NEW_FINISH = pygame.transform.rotate(FINISH, 90)
FINISH_MASK = pygame.mask.from_surface(NEW_FINISH)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("carGoVroom!")

FPS = 60

run = True
clock = pygame.time.Clock()

images = [(BACKGROUND, (0, 0)), (TRACK, (0, 0)),
          (NEW_FINISH, (250, 40)), (BORDER, (0, 0))]

player_car = PlayerCar(3, 3)
# enemy_car = EnemyCar(3, 3)


name = input("Please enter your name to store in the scoreboard: ")

time.sleep(2)
start_time = race_time()

while run:
    clock.tick(FPS)

    draw_images(WINDOW, images, player_car)
    moved = False

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    if key[pygame.K_a]:
        player_car.rotate(left=True)
    if key[pygame.K_d]:
        player_car.rotate(right=True)

    if key[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if key[pygame.K_s]:
        moved = True
        player_car.move_backwards()

    if player_car.collision(BORDER_MASK) != None:
        player_car.collided()

    finished = player_car.collision(FINISH_MASK, 250, 40)
    if finished != None:
        if finished[0] == 38:
            player_car.collided()
        else:
            player_car.restart(start_time, name)
            start_time = race_time()

    if moved == False:
        player_car.reduce_speed()


pygame.quit()
