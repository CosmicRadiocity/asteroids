import pygame
from circleshape import CircleShape
from constants import POWERUP_TYPES, POWERUP_RADIUS

# TYPE 1 = Life | TYPE 2 = Shield | TYPE 3 = Speed boost

class PowerUp(CircleShape):

    def __init__(self, x, y, type):
        super().__init__(x, y, POWERUP_RADIUS)
        self.type = type

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if self.type == 1:
            pygame.draw.line(screen, "green", (self.position.x - POWERUP_RADIUS, self.position.y), (self.position.x + POWERUP_RADIUS, self.position.y), 5)
            pygame.draw.line(screen, "green", (self.position.x, self.position.y - POWERUP_RADIUS), (self.position.x, self.position.y + POWERUP_RADIUS), 5)
        if self.type == 2:
            pygame.draw.rect(screen, "blue", pygame.Rect(self.position.x, self.position.y, POWERUP_RADIUS, POWERUP_RADIUS), 2)
        if self.type == 3:
            triangle = self.triangle()
            pygame.draw.polygon(screen, "yellow", triangle, 2)