import pygame
import datetime


pygame.init()
WIDTH, HEIGHT = 600, 600
screen= pygame.display.set_mode((WIDTH, HEIGHT))

#images
M_clock = pygame.image.load('images/clock_1.jpeg')
M_right = pygame.image.load('images/min_1.png')
M_left = pygame.image.load('images/sec_1.png')

m_clock = pygame.transform.scale(M_clock, (770, 600))
m_right = pygame.transform.scale(M_right, (300, 300))
m_left = pygame.transform.scale(M_left, (300, 300))
botton = pygame.image.load('./images/1.png').convert_alpha()
size_botton = pygame.transform.scale(botton, (30, 30))

# m_left = pygame.transform.flip(m_left, True, True)
# Design of text
font = pygame.font.SysFont('Comicsansms', 30)


def rotate_image(image, angle, x, y):
    new_image = pygame.transform.rotate(image, angle)
    new_rect = new_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return new_image, new_rect

running = True
while running:
    # Time
    today = datetime.datetime.now()
    minute = today.minute
    second = today.second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #angle
    x = ((minute - 1)* -6)%360
    y = ((-6)*(second))%360

    #rot_center
    rotated_right, rect_1 = rotate_image(m_right, x, 300, 300)
    rotated_left, rect_2 = rotate_image(m_left, y, 300, 300)
    
    # TEXT
    clock_text = font.render(today.strftime("%H:%M:%S"), True, pygame.Color("blue"))
    
    
    # UPDATES
    screen.blit(m_clock, (-85, 0))
    screen.blit(clock_text, (10, 10))
    screen.blit(rotated_right, rect_1)
    screen.blit(rotated_left, rect_2)
    screen.blit(size_botton, (WIDTH // 2 - 15, HEIGHT // 2 - 15))

    pygame.display.update()

pygame.quit()