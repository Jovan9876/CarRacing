import pygame
import time

def resize(img, factor):
    """ Scales an image by a x amount"""
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def rotate_image(window, image, top_left, angle):
    """ Takes an image and returns a rotated image based on angle """
    rotated = pygame.transform.rotate(image, angle) # rotates image from top left
    new_image = rotated.get_rect(
        center=image.get_rect(topleft=top_left).center)
    window.blit(rotated, new_image.topleft)

def draw_images(WINDOW, images, player_car):
    """ Draws images from list of images passed along with position"""
    for img, pos in images:
        WINDOW.blit(img, pos)

    player_car.draw(WINDOW)
    pygame.display.update()

def race_time():

    start_time = time.time()

    return start_time