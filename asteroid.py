import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)
        self.x = x
        self.y = y


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rotate = random.uniform(20, 50)
        new_angle_R = pygame.Vector2.rotate(self.velocity, rotate)
        new_angle_L = pygame.Vector2.rotate(self.velocity, -rotate)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        AsteroidR = Asteroid(self.position.x, self.position.y, new_radius)
        AsteroidL = Asteroid(self.position.x, self.position.y, new_radius)
        AsteroidR.velocity = new_angle_R * 1.2
        AsteroidL.velocity = new_angle_L * 1.2