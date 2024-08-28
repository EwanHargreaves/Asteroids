from constants import SHOT_RADIUS
from circleshape import CircleShape
from pygame import *

class Shot(CircleShape):
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        white = (255,255,255)
        draw.circle(screen, white, self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
