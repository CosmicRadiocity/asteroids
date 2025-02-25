import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (enemies, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, bullets)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field_obj = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for obj in enemies:
            if obj.is_colliding(player_obj):
                print("Game over!")
                sys.exit()
            for bullet in bullets:
                if obj.is_colliding(bullet):
                    obj.split()
                    bullet.kill()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()