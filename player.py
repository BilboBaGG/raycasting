from settings import *
import pygame
import math
from map import world_map

class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED
        self.x, self.y = PLAYER_POS
        self.angle = 0

    # getter
    def get_pos(self):
        return (int(self.x), int(self.y))

    # move function
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and ((self.x + self.speed * cos_a) // TILE * TILE, (self.y + self.speed * sin_a) // TILE * TILE) not in world_map:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        if keys[pygame.K_s] and ((self.y - self.speed * sin_a) // TILE * TILE, (self.x - self.speed * cos_a) // TILE * TILE) not in world_map:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        if keys[pygame.K_a] and ((self.x + self.speed * sin_a) // TILE * TILE, (self.y - self.speed * cos_a) // TILE * TILE) not in world_map:
            self.x += self.speed * sin_a
            self.y += -self.speed * cos_a
        if keys[pygame.K_d] and ((self.x - self.speed * sin_a) // TILE * TILE, (self.y + self.speed * cos_a) // TILE * TILE) not in world_map:
            self.x += -self.speed * sin_a
            self.y += self.speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.1
        if keys[pygame.K_RIGHT]:
            self.angle += 0.1
