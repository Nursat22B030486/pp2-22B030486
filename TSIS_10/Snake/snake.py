import psycopg2
from _database import *
from random import randint
import pygame, sys 
from settings import *
import time

username = input("Please, enter username: \n")
play = False
change = None

if does_exists(username):
    print("This username is already registred")
    show_previous_result(username)
    wish = input("Do you want to play again?! \n   (Yes / No) \n")
    if wish == "Yes":
        play = True
        change = 'update'
    else:
        print("Have a good day!")
else:
    play = True
    change = 'insert'
    


if play == True:
    pygame.init()
    clock = pygame.time.Clock()
    
    # window
    screen = pygame.display.set_mode(size) 
    pygame.display.set_caption('Snake')
    

    # function which draws grass
    def draw_grass():
        for i in range(0, grid_number):
            if i%2 == 0:
                for j in range(0, grid_number):
                    if j%2 == 0:
                        pygame.draw.rect(screen, colors['grass_color'], (i*grid_size, j*grid_size, grid_size, grid_size))
            else:
                for j in range(0, grid_number):
                    if j%2 != 0:
                        pygame.draw.rect(screen, colors['grass_color'], (i*grid_size, j*grid_size, grid_size, grid_size))

    def show_score(score):
        text = font.render(f'Score: {score}', True, (0,0,0))
        screen.blit(text, ((WIDTH-540,HEIGHT-60)))
    
    def show_level(level):
        text = font.render(f'Level: {level}', True, (0,0,0))
        screen.blit(text, ((WIDTH-365,HEIGHT-60)))
    
    def show_speed(speed):
        text = font.render(f'Speed: {speed}', True, (0,0,0))
        screen.blit(text, ((WIDTH-200,HEIGHT-60)))


    # CLass point
    class Vector2:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Wall:
      def __init__(self):
        self.body = []
        self.load_wall(level)
        self.draw()

      def load_wall(self,lvl):
        with open(f'levels/level{lvl}.txt', 'r') as f:
            wall_body = f.readlines()

        for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
               if value == '#':
                  self.body.append([j*grid_size,i*grid_size])

      def draw(self):
        for x,y in self.body:
            pygame.draw.rect(screen,(255,255,0),(x,y,grid_size,grid_size))

    class Snake:
        def __init__(self):
            self.body = [Vector2(7,10), Vector2(6,10)]
            self.dx = 0
            self.dy = 1


        def draw_snake(self):
            pygame.draw.rect(screen, colors['snake_head'], (self.body[0].x *grid_size, self.body[0].y *grid_size, grid_size, grid_size))
            for block in self.body[1:]:
                pygame.draw.rect(screen, colors['snake_color'], (block.x*grid_size, block.y*grid_size, grid_size, grid_size))

        def move(self):
            for i in range(len(self.body)-1, 0, -1):
                self.body[i].x = self.body[i-1].x
                self.body[i].y = self.body[i-1].y
            
            self.body[0].x += dx
            self.body[0].y += dy
            

        def check_collision(self, food):
            if food.location.x != self.body[0].x:
                return False
            if food.location.y != self.body[0].y:
                return False
            return True
        
        def check_fail(self):
      
            # 1 case
            if self.body[0].x < 0 or self.body[0].x > grid_number-1 or self.body[0].y < 0 or self.body[0].y > grid_number-1:
                self.game_over()
            # 2 case
            for block in self.body[1:]:
                if block == self.body[0]:
                    self.game_over()
            # 3 case
            for block in wall.body:
                if block == (self.body[0].x*grid_size, self.body[0].y*grid_size):
                    self.game_over()
            if len(self.body) <= 1:
                self.game_over()
                

        def game_over(self):
            # after game over send results to database
            if change == 'insert':
                inserting_data(username,level,score,speed)
            else:
                update_data(level, score, speed, username)
            time.sleep(3)
            pygame.quit()
            sys.exit()

                
    class Food: 
        def __init__(self, x, y):
            self.image = foods[0]
            self.location = Vector2(x, y)
        
        def draw(self):
            food_rect = pygame.Rect(self.location.x*grid_size, self.location.y*grid_size, grid_size, grid_size)
            screen.blit(self.image, food_rect)

        def update(self):
            self.location.x = randint(0, grid_number-1)
            self.location.y = randint(0, grid_number-1)
            self.draw()
    
    class Poison:
        def __init__(self, x, y):
            self.location = Vector2(x,y)
            self.image = foods[2]

        def show(self):
            self.image = pygame.transform.scale(self.image, (grid_size, grid_size))
            screen.blit(self.image, (self.location.x * grid_size,self.location.y * grid_size))
        
        def update(self):
            self.location.x = randint(0, grid_number-1)
            self.location.y = randint(0, grid_number-1)
            self.show()
    

    class Fruit:
        def __init__(self, x, y):
            self.image = foods[1]
            self.location = Vector2(x, y)
            self.timer = 15
            
        def draw(self):
            self.image = pygame.transform.scale(self.image, (grid_size, grid_size))
            screen.blit(self.image, (self.location.x * grid_size,self.location.y * grid_size))
        
        def update(self):
            self.location.x = randint(0, grid_number-1)
            self.location.y = randint(0, grid_number-1)
            self.draw()
            self.timer = 15
            
    # Objects
    snake = Snake()
    food = Food(randint(0, grid_number-1), randint(0, grid_number-1))
    fruit = Fruit(randint(0, grid_number-1), randint(0, grid_number-1))
    poison = Poison(randint(0, grid_number-1), randint(0, grid_number-1))
    wall = Wall()

    run = True
    while run:
        screen.fill(colors["bg_color"])
        draw_grass()

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_UP:
                    if dy != 1:
                        dx = 0
                        dy = -1
        
                if event.key  == pygame.K_DOWN:
                    if dy != -1:
                        dx = 0
                        dy = 1
        
                if event.key  == pygame.K_LEFT:
                    if dx != 1:
                        dx = -1
                        dy = 0
        
                if event.key  == pygame.K_RIGHT:
                    if dx != -1:
                        dx = 1
                        dy = 0
                if event.key  == pygame.K_SPACE:
                    time.sleep(5)

                snake.dx = dx
                snake.dy = dy
        
        # Checking collision of food and snake
        if snake.check_collision(food):
            score += 1
            pygame.mixer.Sound(musics[1]).play()
            snake.body.append(Vector2(snake.body[len(snake.body)-1].x, snake.body[len(snake.body)-1].y))
            food.update()
        fruit.timer -= 1
        
        if fruit.timer == 0:
            fruit.update()
        
        if snake.check_collision(fruit):
            score += 4
            fruit.update()
            pygame.mixer.Sound(musics[1]).play()
            snake.body.append(Vector2(snake.body[len(snake.body)-1].x, snake.body[len(snake.body)-1].y))
            
        
        if snake.check_collision(poison):
            score -= 1
            pygame.mixer.Sound(musics[0]).play()

            if len(snake.body) > 1:
                snake.body.pop()
            else:
                run = False
            poison.update()

        if score > (level) * 5:
            level += 1
            speed += 2
            # wall.load_wall(0)
            wall.load_wall(level)

        show_level(level)
        show_score(score)
        show_speed(speed)

        wall.draw()
        poison.show()
        fruit.draw()
        food.draw()
        snake.move()
        snake.draw_snake()
        snake.check_fail()
        
        for block in snake.body[1:]:
            while block == food.location:
               food.update()
        
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()