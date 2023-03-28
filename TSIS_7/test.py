import pygame 

clock = pygame.time.Clock()

pygame.init()
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode(size = (HEIGHT, WIDTH))
pygame.display.set_caption("My first job")
x, y = 10, 10
running = True
while running:
    step = 15
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        y += step
    if pressed[pygame.K_UP]:
        y -= step
    if pressed[pygame.K_LEFT]:
        x -= step
    if pressed[pygame.K_RIGHT]:
        x += step
    
    pygame.draw.line(screen, (255, 0, 0), (0,0), (HEIGHT,WIDTH), width=2)
    pygame.draw.line(screen, (0, 255, 0), (0,HEIGHT), (0,WIDTH), width=2)
    pygame.draw.circle(screen, (122, 122, 122), (HEIGHT//2,WIDTH//2), radius=15, width=5)

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 90, 90))
    pygame.display.flip()
    clock.tick(60)