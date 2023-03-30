import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("The last task")
clock = pygame.time.Clock()

x = 30
y = 30



working = True

while working:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            working = False

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius=25)

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_DOWN]:
        if 0 <= y and y < HEIGHT-30:
            y += 20
    if pressed[pygame.K_LEFT]:
        if 30 < x and x <= HEIGHT-30:
            x -= 20
    if pressed[pygame.K_UP]:
        if 30 < y and y <= HEIGHT-30:
            y -= 20
    if pressed[pygame.K_RIGHT]:
        if 0 <= x and x < HEIGHT-30:    
            x += 20   

    pygame.display.flip()
    clock.tick(30)



