import pygame
import sys

import random


# INITIALIZING
pygame.init()

#  WINDOW
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Variables
BLOCK_SIZE = 40
clock = pygame.time.Clock()
musics = ["./musics/atakujuschaja-zmeja.mp3", "./musics/suck-in-whoosh_z1rryr4u.mp3", "./musics/week10_materials_background.wav"]
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
text = font.render("GAME OVER",True, (0, 0, 0)) 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x = WIDTH // BLOCK_SIZE // 2,
                y = HEIGHT // BLOCK_SIZE // 2,
            ), 
            Point(
                x = WIDTH // BLOCK_SIZE // 2 + 1,
                y = HEIGHT // BLOCK_SIZE // 2,
            ), 
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, pygame.Color("red"),
            pygame.Rect(
                head.x * BLOCK_SIZE, 
                head.y *BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                screen,
                pygame.Color("blue"),
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )


    def move(self, dx, dy):
        for idx in range(len(self.body)-1, 0, -1):
            self.body[idx].x = self.body[idx-1].x
            self.body[idx].y = self.body[idx-1].y
        self.body[0].x += dx
        self.body[0].y += dy

        # if self.body[0].x > WIDTH // BLOCK_SIZE:
        #     self.body[0].x = 0
        # elif self.body[0].x < 0:
        #     self.body[0].x = WIDTH // BLOCK_SIZE
        # elif self.body[0].y < 0:
        #     self.body[0].y = WIDTH // BLOCK_SIZE
        # elif self.body[0].y > HEIGHT // BLOCK_SIZE:
        #     self.body[0].y = 0
        if not 0 <= self.body[0].x < WIDTH // BLOCK_SIZE:
            pygame.quit()
            sys.exit()
        elif not 0 <= self.body[0].y  < HEIGHT // BLOCK_SIZE:
            pygame.quit()
            sys.exit()
        
        for block in range(len(self.body)-1,1, -1):
            if self.body[block] == self.body[0]:
                pygame.quit()
                sys.exit()

        

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, pygame.Color("grey"), start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, pygame.Color("grey"), start_pos=(0, y), end_pos=(WIDTH, y), width=1)

def show_points(scores, levels):
    screen.blit(scores, (10, 10))
    screen.blit(levels, (screen.get_width()-50, 10))


class Poison:
    def __init__(self, x, y):
        self.location = Point(x,y)
        self.image = pygame.image.load("./images/poison-bottle-3826.png")

    def show(self):
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        screen.blit(self.image, (self.location.x * BLOCK_SIZE,self.location.y * BLOCK_SIZE))

class Food:
    def __init__(self, x, y):
        self.location = Point(x,y)
        

    
    def draw(self):
        pygame.draw.rect(
            screen,
            pygame.Color("green"),
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


class Fruit:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("./images/fruit.webp"), (BLOCK_SIZE,BLOCK_SIZE))
        self.location = Point(x, y)
        self.time = 15


    def draw(self):
        screen.blit(self.image, pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    
    def update(self):
        self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        self.draw()
        self.time = 15
        


def main():
    running = True
    food = Food(5, 5)
    fruit = Fruit(8 ,7)
    snake = Snake()
    dx, dy = 0, 0 
    SCORE = 1
    LEVEL = 0
    poison = Poison(6, 8)
    fps = 5
    



    pygame.mixer.music.load(musics[2])
    pygame.mixer.music.play(-1)

    while running:
        screen.fill(pygame.Color("white"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                        if dy != 1:
                            dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    if dy != -1:
                        dx, dy = 0, 1
                elif event.key == pygame.K_RIGHT:
                    if dx != -1:
                        dx, dy = 1, 0
                elif event.key == pygame.K_LEFT:
                    if dx != 1:  
                        dx, dy = -1, 0
            

        
        snake.move(dx, dy)
         
        
        if  snake.check_collision(food):
            SCORE += 1
            if SCORE%7 == 0:
                LEVEL += 1
                fps += 2
            pygame.mixer.Sound(musics[1]).play()

            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        if  snake.check_collision(fruit):
            SCORE += (random.randint(0,7))
            if SCORE%7 == 0:
                LEVEL += 1
                fps += 2
            pygame.mixer.Sound(musics[1]).play()

            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            fruit.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            fruit.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            fruit.time = 15
       
       

        if snake.check_collision(poison):
            SCORE -= 1
            pygame.mixer.Sound(musics[0]).play()
            if len(snake.body) > 1:
                snake.body.pop()
            else:
                running = False
            poison.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            poison.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        
        #  TEXT
        scores = font.render(f'{str(SCORE-1)}', True, (0, 0, 0))
        level = font.render(f'{str(LEVEL)}', True, (0, 0, 0))


        fruit.time -= 1
        
        snake.draw()
        food.draw()
        if fruit.time != 0:
            fruit.draw()
        else:
            fruit.update()

        poison.show()
        draw_grid()
        show_points(scores, level)

        pygame.display.flip()
        clock.tick(fps)
            


if __name__ == '__main__':
    main()


