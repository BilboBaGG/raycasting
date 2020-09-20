import pygame
from settings import *
from map import world_map
import time

def ray_casting(display1, player_pos, player_angle):
    all_depth = MAX_DEPTH * QUANT_RAYS
    #now_depth = 1
    angle = player_angle - HALF_FOV
    x0, y0 = player_pos
    #beg = time.time()
    for ray in range(QUANT_RAYS):
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)
        for depth in range(1,MAX_DEPTH):
            x = x0 + depth * cos_a
            y = y0 + depth * sin_a
            #now_depth += 1
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                proj_height = PROJ_COEFF / depth * 6
                col = 255 / (1 + depth* depth * 0.0001)
                color = (col,col,0)
                if pygame.key.get_pressed()[pygame.K_LSHIFT]:
                    sit = -20
                else:
                    sit = 0
                pygame.draw.rect(display1,color,(ray * SCALE, HALF_HEIGHT - proj_height // 2 + sit, SCALE , proj_height))
                break

        #pygame.draw.line(display1, DARK_GRAY, player_pos,(x,y), 2)
        angle += DELTA_ANGLE
    #end = time.time()
    #time.sleep(all_depth * (end - beg)/now_depth - (end - beg))
