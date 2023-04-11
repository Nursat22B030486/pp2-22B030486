
import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

active_pen = 0
active_color = WHITE

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOL_HEIGHT = HEIGHT - WIDTH

BACKGROUND_COLOR = WHITE

def get_font(size):
    return pygame.font.SysFont("comicsans", size)