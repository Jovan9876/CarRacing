import pygame
from . import Car, resize

PLAYER_CAR = resize(pygame.image.load("images/car.png"), 0.1)
# ENEMY_CAR = resize(pygame.image.load("images/cop.png"), 0.1)

class PlayerCar(Car):
    """ Players car class """
    IMG = PLAYER_CAR
    START_POS = (260, 80)


# class EnemyCar(Car):
#     """ Enemy car class """
#     IMG = ENEMY_CAR
#     START_POS = (260, 100)
