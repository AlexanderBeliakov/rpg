import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, color, health):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.health = health
        self.max_health = health

    def draw_health_bar(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.rect.x, self.rect.y - 10, 40, 5))
        health_percentage = self.health / self.max_health
        pygame.draw.rect(surface, (0, 255, 0), (self.rect.x, self.rect.y - 10, 40 * health_percentage, 5))
