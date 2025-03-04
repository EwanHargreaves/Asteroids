import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add groups to classes
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = shots, updatable, drawable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        screen.fill((0,0,0))

        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collide(player):
                print("Game over!")
                return

            for bullet in shots:
                if item.collide(bullet):
                    item.kill()
                    bullet.kill()
                    break
        for item in drawable:
            item.draw(screen)
        
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return
        
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()