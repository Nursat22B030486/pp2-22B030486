import pygame
import datetime
import math

# Initializing
pygame.init()
pygame.font.init()

# constants
colors = [(255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 224, 32)]

width, height = (600, 600)
h_width, h_height = width // 2, height // 2
radius =  h_height - 50
radiuses = { 'sec' : radius, 'min' : radius - 30, 'hour' : radius-80 , 'main_lines' : radius-40}

clock = pygame.time.Clock()

clock12 = dict(zip(range(12), range(0, 360, 30)))
clock60 = dict(zip(range(60), range(0, 360, 6)))

running = True


# FUNCTIONS
def get_clock_position(clock_dict, clock_hand, key):
    x = h_width - radiuses[key] * math.cos(math.radians(clock_dict[clock_hand]) + math.pi / 2) 
    y = h_height + radiuses[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2) 
    return x, y



# Design
font = pygame.font.SysFont('Verdana', 40)


# Surface
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")


# LOOP
while running:
    
    # Background's color
    screen.fill(colors[2])

    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Text 
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second
    text = font.render(now.strftime("%H:%M:%S"), True, colors[3], pygame.Color('light green'))
    screen.blit(text, (10, 10))


    # Drawing
    pygame.draw.circle(screen, colors[0], (300, 300), radius=radius)
    pygame.draw.line(screen, colors[1], (h_width, h_height), get_clock_position(clock60, second,'sec'), width=4)
    pygame.draw.line(screen, colors[1], (h_width, h_height), get_clock_position(clock60, minute, 'min'), width=8)
    pygame.draw.line(screen, colors[1], (h_width, h_height), get_clock_position(clock12, hour, 'hour'), width=12)
    
    # Drawing the hour's lines
    


    # Part of loop
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
