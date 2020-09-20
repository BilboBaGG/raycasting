import pygame
from settings import *
from player import Player
import math
from map import *
from raycast import ray_casting

pygame.init()

display1 = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

runner = True

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display1.fill(BLACK)

    player.movement()
    ray_casting(display1, player.get_pos(), player.angle)

    pygame.draw.circle(display1, GREEN, player.get_pos(), RADIUS)

    for x, y in world_map:
        pygame.draw.rect(display1, WHITE, (x, y, TILE, TILE), 2)
    pygame.display.flip()
    clock.tick(FPS)
