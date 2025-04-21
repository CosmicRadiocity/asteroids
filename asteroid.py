import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LIFE_CHANCE, SHIELD_CHANCE, BOOST_CHANCE, SCREEN_HEIGHT, SCREEN_WIDTH
from powerup import PowerUp

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):  
        self.position += self.velocity * dt
        if(self.position.x - (self.radius * 2) > SCREEN_WIDTH):
            self.position.x = 0
        elif(self.position.x + (self.radius * 2) < 0):
            self.position.x = SCREEN_WIDTH
        if(self.position.y - (self.radius * 2) > SCREEN_HEIGHT):
            self.position.y = 0
        elif(self.position.y + (self.radius * 2) < 0):
            self.position.y = SCREEN_HEIGHT


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        ast1rot = self.velocity.rotate(angle)
        ast2rot = self.velocity.rotate(-angle)
        ast1rad = self.radius - ASTEROID_MIN_RADIUS
        ast2rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, ast1rad)
        ast1.velocity = ast1rot * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, ast2rad)
        ast2.velocity = ast2rot * 1.2
        powerup_chance = random.randint(0, 100)
        if powerup_chance <= LIFE_CHANCE:
            powerup = PowerUp(self.position.x, self.position.y, 1)
        elif powerup_chance <= SHIELD_CHANCE:
            powerup = PowerUp(self.position.x, self.position.y, 2)
        elif powerup_chance <= BOOST_CHANCE:
            powerup = PowerUp(self.position.x, self.position.y, 3)
