import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #-------------------------------------------------------------------------
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #-------------------------------------------------------------------------
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    #-------------------------------------------------------------------------
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #-------------------------------------------------------------------------
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #-------------------------------------------------------------------------
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in asteroids:
            if player.collision(object):
                print("Game over!")
                return
        updatable.update(dt)
        
        pygame.Surface.fill(screen, (0, 0, 0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock.tick(clock, 60) / 1000

if __name__ == "__main__":
    main()
