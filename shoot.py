from circleshape import CircleShape
from constants import BULLET_RADIUS, WHITE
import pygame

class Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt