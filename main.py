import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import PowerUp

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (enemies, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, bullets)
PowerUp.containers = (drawable, powerups)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field_obj = AsteroidField()
    font = pygame.font.Font(None, 64)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for obj in enemies:
            if obj.is_colliding(player_obj):
                if player_obj.lives > 0:
                    if player_obj.hit_cooldown <= 0 and player_obj.shield_cooldown <= 0:
                        player_obj.lives -= 1
                        player_obj.hit_cooldown = PLAYER_HIT_COOLDOWN
                else:
                    print("Game over!")
                    sys.exit()
            for bullet in bullets:
                if obj.is_colliding(bullet):
                    obj.split()
                    bullet.kill()
                    score += obj.radius

        for obj in powerups:
            if obj.is_colliding(player_obj):
                obj.kill()
                if obj.type == 1 and player_obj.lives < 5:
                    player_obj.lives += 1
                elif obj.type == 2:
                    player_obj.shield_cooldown = PLAYER_SHIELD_COOLDOWN
                elif obj.type == 3 and player_obj.boost_cooldown <= 0:
                    player_obj.boost_cooldown = PLAYER_BOOST_COOLDOWN

        for obj in drawable:
            obj.draw(screen)
        hud = font.render(f"Score = {score} | Lives = {player_obj.lives}", False, "white")
        hudpos = hud.get_rect(centerx=SCREEN_WIDTH/5, y=10)
        screen.blit(hud, hudpos)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()