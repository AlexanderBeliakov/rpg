import pygame
import sys
import random
import math

from settings import *
from player import Player
from monsters import Monster

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Игра")

all_sprites = pygame.sprite.Group()
monsters = []

player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(player)

# Создание монстров
for _ in range(5):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    monster = Monster(x, y)
    all_sprites.add(monster)
    monsters.append(monster)


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Выбор предмета из инвентаря
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player.select_item()

        # Атака по нажатию левой кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.attack(monsters)

    # Движение игрока
    player.move()

    # Движение монстров и атака
    for monster in monsters:
        monster.move_towards_player(player)
        distance = math.hypot(player.rect.x - monster.rect.x, player.rect.y - monster.rect.y)
        if distance < 50:
            monster.attack(player)

    # Отрисовка всех спрайтов
    for entity in all_sprites:
        window.blit(entity.image, entity.rect)
        entity.draw_health_bar(window)

    # Отображение инвентаря и выбранного предмета
    font = pygame.font.SysFont(None, 24)
    inventory_text = font.render(f'Инвентарь: {player.selected_item}', True, (0, 0, 0))
    window.blit(inventory_text, (10, 10))

    # Проверка здоровья игрока
    if player.health <= 0:
        running = False
        print("Игра окончена!")

    pygame.display.flip()

pygame.quit()
sys.exit()