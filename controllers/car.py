import math, pygame, requests, httpie, time
from . import rotate_image
from models import HighScores, Score

class Car:
    """ Main class that cars can inherit from """

    def __init__(self, max_speed, rotation_speed):
        self.max_speed = max_speed
        self.rotation_speed = rotation_speed
        self.x, self.y = self.START_POS
        self.img = self.IMG
        self.speed = 0
        self.acceleration = 0.1
        self.angle = 90

    def rotate(self, left=False, right=False):
        """ Rotates the car based on the key pressed """
        if left:
            self.angle += self.rotation_speed
        elif right:
            self.angle -= self.rotation_speed

    def draw(self, WINDOW):
        """ Rotates image by center instead of a corner """
        rotate_image(WINDOW, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        """ Increases speed based on acceleration with the cap at max_speed """
        self.speed = min(self.speed + self.acceleration, self.max_speed)
        self.move()

    def move_backwards(self):
        """ Moves car backwards with max speed at less than half of the max_speed """
        self.speed = max(self.speed - self.acceleration, -self.max_speed / 3)
        self.move()

    def move(self):
        """ 
        SOH CAH TOA
        Ability to move in 2 dimensions
        Converts angle into radians
        Calculates displacement needed to move in x direction using angle and speed
        """
        angle_radian = math.radians(self.angle)
        vert_displacement = math.cos(angle_radian) * self.speed
        horz_displacement = math.sin(angle_radian) * self.speed

        self.y -= vert_displacement
        self.x -= horz_displacement

    def reduce_speed(self):
        """ Reduce speed based on acceleration / 2 with the cap at 0 to prevent negative speed """
        self.speed = max(self.speed - self.acceleration / 2, 0)
        self.move()

    def collision(self, mask, x=0, y=0):
        """ Gets mask of the car in use and checks it with the border mask to see if car collides with the border """
        car_mask = pygame.mask.from_surface(self.img)
        collision_difference = (int(self.x - x), int(self.y - y))
        collide_point = mask.overlap(car_mask, collision_difference)
        return collide_point

    def collided(self):
        self.speed = -self.speed
        self.move()

    def restart(self, start_time, name):
        """ Restarts the game when you hit the finish line """
        high_score = HighScores()
        self.x, self.y = self.START_POS
        self.angle = 90
        self.speed = 0
        finish_time = time.time() - start_time
        new_score = Score(name, finish_time)
        high_score.add(new_score)
        high_score.save()
        print("--------------------")
        print("Your lap time is:")
        print("%.2f" % finish_time + " seconds")
        print("--------------------")
