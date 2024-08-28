from pygame import *
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.position = Vector2(x, y)
        self.rotation = 0
        self.timer = 0
        #self.add(*groups)

    
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self,dt):
        forward = Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        self.timer -= dt
        keys = key.get_pressed()

        if keys[K_a]:
            self.rotate(-dt)
        if keys[K_d]:
            self.rotate(dt)
        if keys[K_w]:
            self.move(dt)
        if keys[K_s]:
            self.move(-dt)
        if keys[K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer <= 0:
            bullet = Shot(self.position.x, self.position.y)
            bullet.velocity = Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN