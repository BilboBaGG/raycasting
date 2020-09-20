import math

# game settings

FPS = 100

WIDTH = 500
HEIGHT = 500

DIAGONAL = int(math.sqrt(WIDTH ** 2 + HEIGHT ** 2))

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# blocks settings

TILE = 50

# ray casting

FOV = math.pi / 3
HALF_FOV = FOV / 2
QUANT_RAYS = 100
MAX_DEPTH = DIAGONAL
DELTA_ANGLE = FOV / QUANT_RAYS

SCALE = WIDTH // QUANT_RAYS
DIST = QUANT_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * TILE

# player settings

PLAYER_POS = (HALF_WIDTH, HALF_HEIGHT)
PLAYER_SPEED = 4
RADIUS = 6

# base colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GRAY = (120,120,120)
