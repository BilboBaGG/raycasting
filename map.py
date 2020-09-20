from settings import *

text_map = [
    'WWWWWWWWWW',
    'W..W.....W',
    'W.WW..WW.W',
    'W........W',
    'W.WW.....W',
    'W........W',
    'W..W.....W',
    'W.....WW.W',
    'W.W.W..W.W',
    'WWWWWWWWWW'
]

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
