import pygame
import random
import time

# INITILIZING
pygame.init()

# Media 
player = pygame.image.load("./images/Player.png")
background = pygame.image.load("./images/AnimatedStreet.png")
background_music = pygame.mixer.music.load('./musics/week10_materials_background.wav')
pygame.mixer.music.play(-1)


# Window
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RACER")
pygame.display.set_icon(player)


# variables
clock = pygame.time.Clock()
SCORE = 0
SPEED = 5
COIN = 0
check = 5

ads =False

# DESIGN
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, pygame.Color("black"))
                        


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen.get_width()-40), 0)
        self.speed = 5
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            SCORE += 1
            self.rect.center = (random.randint(30, 370), 0)
        global check
        if COIN >= check:
            check += 5
            self.speed += 1


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/coin.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen.get_width()-40), 0)
    
    def move(self):
        self.rect.move_ip(0, 2)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 5)
            screen.blit(self.image, self.rect)
    
    def update(self):
        global COIN
        COIN += 1
        self.rect.top = 0
        self.rect.center = (random.randint(30, 370), 5)
        screen.blit(self.image, self.rect)


class Coin_3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/3_coin.webp")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen.get_width()-40), 0)
    
    def move(self):
        self.rect.move_ip(0, 1)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 5)
            screen.blit(self.image, self.rect)
    
    def update(self):
        global COIN
        COIN += 3
        self.rect.top = 0
        self.rect.center = (random.randint(30, 370), 5)
        screen.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen.get_width():
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)



P1 = Player()
E1 = Enemy()
C1 = Coin()
C3 = Coin_3()

enemies = pygame.sprite.Group()
enemies.add(E1)


coins = pygame.sprite.Group()
coins.add(C1)
coins_3 = pygame.sprite.Group()
coins_3.add(C3)

all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(C3)



inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)




running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
            # pygame.quit()
        if event.type == inc_speed:
            SPEED += 0.5

    screen.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, (0, 0, 0))
    screen.blit(scores, (10, 10))
    scores_coin = font_small.render(str(COIN), True, (0, 0, 0))
    screen.blit(scores_coin, (screen.get_width()- 30, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, coins):
        C1.update()
        
     
    if pygame.sprite.spritecollideany(P1, coins_3):
        C3.update()
    
    C3.move()
    C1.move()
    
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("./musics/week10_materials_crash.wav").play()
        time.sleep(0.5)
        
        screen.fill(pygame.Color("red"))
        screen.blit(game_over, (30, 250))
        screen.blit(font_small.render(f"Total score:{str(SCORE)}", True, (0, 0, 0)), (150, 320))
        screen.blit(font_small.render(f"Total coin:{str(COIN)}", True, (0, 0, 0)), (150, 350))
        pygame.display.update()
        
        
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        running  = False
        

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
