import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add groups to classes
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        screen.fill((0,0,0))

        for item in updatable:
            item.update(dt)
        for item in asteroids:
            collision = item.collide(player)
            if collision == True:
                print("Game over!")
                return
        for item in drawable:
            item.draw(screen)
        
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
        
        dt = clock.tick(60) / 1000
        pygame.display.flip()
        

if __name__ == "__main__":
    main()