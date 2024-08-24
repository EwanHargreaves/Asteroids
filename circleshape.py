import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        white = (255,255,255)
        pygame.draw.polygon(screen,white,self.triangle(),width=2)


    def update(self, dt):
        # sub-classes must override
        pass
    
    def collide(self, other_circle):
        distance = self.position.distance_to(other_circle.position)
        return (self.radius + other_circle.radius) >= distance