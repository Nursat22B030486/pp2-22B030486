import pygame 
import datetime
import os
from rotate import *

# Initializing
pygame.init()

# Window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey\'s clock')


# Media
M_clock = pygame.image.load("./images/clock.png").convert_alpha()
m_minute = pygame.image.load("./images/min_1.png").convert_alpha()
m_second = pygame.image.load("./images/sec_1.png").convert_alpha()
botton = pygame.image.load('./images/1.png').convert_alpha()

clock = pygame.time.Clock()

# Data of images
M_clock = pygame.transform.scale(M_clock, (800, 800))
rect_1 = M_clock.get_rect()
rect_1.center = (WIDTH // 2, HEIGHT // 2)
right = pygame.transform.scale(m_minute, (150, 150))
rect_2 = right.get_rect()
rect_2.topleft = (WIDTH // 2, HEIGHT - 550)
left = pygame.transform.scale(m_second, (150, 150))
rect_3 = left.get_rect()
rect_3.topleft = (WIDTH // 2, HEIGHT - 550)
size_botton = pygame.transform.scale(botton, (30, 30))


# Design of text
font = pygame.font.SysFont('Comicsansms', 30)



# Game LOOP
working = True
while working:
    # BACKGROUND
    screen.fill((0, 0, 0))

    # END EVENT
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            working = False
    
    
    # Time
    today = datetime.datetime.now()
    minute = today.minute
    second = today.second

    x = (-minute* 6)%360
    y = ((-6)*second)%360

    #rot_center
    rot_right, x = rot_center(right, x, 150, 150)
    rot_left, y = rot_center(left, y, 150, 150)
    # UPDATES
    screen.blit(M_clock, rect_1)
    screen.blit(rot_right, rect_2)
    screen.blit(rot_left, rect_3)
    screen.blit(size_botton, (WIDTH // 2 - 15, HEIGHT // 2 - 15))
    
    

    # Text
    clock_text = font.render(today.strftime("%H:%M:%S"), True, pygame.Color("blue"))
    screen.blit(clock_text, (10, 10))

    pygame.display.flip()
    clock.tick(1)



