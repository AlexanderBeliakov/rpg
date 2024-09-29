import math

from entity import Entity

class Monster(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 0, 0), 50)
        self.speed = 2

    def move_towards_player(self, player):
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        distance = math.hypot(dx, dy)
        if distance > 0:
            dx, dy = dx / distance, dy / distance
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

    def attack(self, player):
        player.health -= 0.5
