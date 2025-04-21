import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x, y, boost=False):
        if boost:
            super().__init__(x, y, SHOT_RADIUS + 5)
        else:
            super().__init__(x, y, SHOT_RADIUS)
        self.boost = boost

    def draw(self, screen):
        if self.boost:
            color = "yellow"
        else:
            color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt