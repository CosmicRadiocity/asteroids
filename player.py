import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.lives = 3
        self.hit_cooldown = 0
        self.shield_cooldown = 0
        self.boost_cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        color = "white"
        if self.hit_cooldown > 0:
            color = "red"
        elif self.shield_cooldown > 0:
            color = "blue"
        elif self.boost_cooldown > 0:
            color = "yellow"
        pygame.draw.polygon(screen, color, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt
        self.hit_cooldown -= dt
        self.boost_cooldown -= dt
        self.shield_cooldown -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(-dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shot_cooldown < 0:
            if self.boost_cooldown > 0:
                bullet = Shot(self.position.x, self.position.y, True)
            else: 
                bullet = Shot(self.position.x, self.position.y, False)
            bullet.velocity = pygame.Vector2(0 ,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            if self.boost_cooldown > 0:
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN / 2
            else:
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

