import pygame
from settings import *
from map import world_map
import time

def ray_casting(display, player_pos, player_angle):
    all_depth = MAX_DEPTH * QUATN_RAYS
    now_depth = 0
    angle = player_angle - HALF_FOV
    x0, y0 = player_pos
    beg = time.time()
    for ray in range(QUATN_RAYS):
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)
        for depth in range(MAX_DEPTH):
            x = x0 + depth * cos_a
            y = y0 + depth * sin_a
            now_depth += 1
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                break
        pygame.draw.line(display, DARK_GRAY, player_pos,(x,y), 2)
        angle += DELTA_ANGLE
    end = time.time()
    time.sleep(all_depth*(end - beg)/now_depth - (end - beg))
