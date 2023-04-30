import pygame
pygame.init() 

WIDTH, HEIGHT = 800, 800
size = (WIDTH, HEIGHT)
grid_size = 40
grid_number = 20

colors = {
    'bg_color': (175,215,70),
    'grass_color': (167,209,61),
    'snake_head' : (0, 0, 255),
    'snake_color': (255,0,0)}

fps = 5

# TExt design
font = pygame.font.SysFont('Cooper Black',grid_size)

#  Movement]
dx = 0
dy = 0

# Foods
foods = [
            pygame.transform.scale(pygame.image.load('./images/apple.png'), (grid_size, grid_size)),
            pygame.transform.scale(pygame.image.load('./images/fruit.webp'), (grid_size, grid_size)),
            pygame.transform.scale(pygame.image.load('./images/poison-bottle-3826.png'), (grid_size, grid_size))
]
#  MUSICS
musics = ["./musics/atakujuschaja-zmeja.mp3", "./musics/suck-in-whoosh_z1rryr4u.mp3", "./musics/week10_materials_background.wav"]

# DATA
score = 0
level = 0
speed = fps