import pygame 
import time
import os


pygame.init()
WIDTH, HEIGHT = 1100, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey\'s clock')
clock = pygame.time.Clock()

# mickey = 'C://Users//Kordabay Nursat//Desktop//KBTU\'\'22//Python//Git_hub//pp2-22B030486//TSIS_7//'

picture = pygame.image.load("mickeyclock.png").convert_alpha()


time.ctime()


rect = picture.get_rect()
rect.center = WIDTH//2, HEIGHT//2



working = True
while working:
    screen.fill((255, 255, 255))


    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            working = False
    screen.blit(picture, rect)
    # screen.blit(picture, (0, ))
    pygame.display.flip()
    clock.tick(60)