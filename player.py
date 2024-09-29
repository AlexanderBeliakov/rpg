from entity import Entity
from settings import *

import pygame

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 0, 255), 100)
        self.speed = 5
        self.inventory = ['Меч', 'Щит', 'Зелье']
        self.selected_item = self.inventory[0]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def select_item(self):
        index = self.inventory.index(self.selected_item)
        index = (index + 1) % len(self.inventory)
        self.selected_item = self.inventory[index]

    def attack(self, monsters, all_sprites):
        for monster in monsters:
            if self.rect.colliderect(monster.rect):
                monster.health -= 20
                if monster.health <= 0:
                    monsters.remove(monster)
                    all_sprites.remove(monster)