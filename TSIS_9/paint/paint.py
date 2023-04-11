from settings import *
import math

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
painting = []
RGB = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return

class Button_1(GameObject):
    def __init__(self):
        self.size = 50
        self.rect = pygame.draw.rect(
            screen,
            BLACK,
            (
                140,
                20,
                self.size+20,
                self.size,
            ),
            width = 3,
        )
        self.square = pygame.draw.rect(
            screen,
            BLACK,
            (
                350,
                20,
                self.size,
                self.size,
            ),
            width = 3,
        )
        self.circle = pygame.draw.circle(
            screen,
            BLACK,
            (
                245,
                45
            ),
            radius=self.size // 2,
            width=3
        )
        self.eraser = pygame.image.load(".././images/9041260_eraser_fill_icon.png")
        self.eraser = pygame.transform.scale(self.eraser, (50, 50))
        self.rect_1 = self.eraser.get_rect()
        self.rect_1.center = (305, 45)
        self.square = pygame.draw.rect(
            screen,
            BLACK,
            (
                350,
                20,
                self.size//2,
                self.size//2,
            ),
            width = 3
        )
        self.r_triangle = pygame.draw.polygon(
            screen,
            BLACK, 
            [(375, 20), (375, 45), (400, 45)],  
        )
        self.eq_triangle = pygame.draw.polygon(
            screen,
            BLACK, 
            [(350, 70), (375/2,70-(math.sqrt(3)*25)/2), (375, 70)],
            width=3
        )
        self.rhombus = pygame.transform.scale(pygame.image.load(".././images/9805339.png"), (self.size//2, self.size//2))
        self.rhombus_rect = self.rhombus.get_rect()
        self.rhombus_rect.center = (390, 58) 
        self.pen= pygame.transform.scale(pygame.image.load(".././images/pen.png"), (self.size//2, self.size//2))
        self.pen_rect = self.pen.get_rect()
        self.pen_rect.center = (440, 45) 
        
        


    
    def draw(self):
        pygame.draw.rect(
            screen,
            BLACK,
            (
                140,
                20,
                self.size+20,
                self.size,
            ),
            width = 3
        )
        pygame.draw.circle(
            screen,
            BLACK,
            (
                245,
                45
            ),
            radius=self.size // 2,
            width= 3,
        )
        screen.blit(self.eraser, self.rect_1)
        pygame.draw.rect(
            screen,
            BLACK,
            (
                350,
                20,
                self.size//2,
                self.size//2,
            ),
            width = 3
        )
        pygame.draw.polygon(
            screen,
            BLACK, 
            ([380, 20], (380, 43), (403, 43)),
            width = 3  
        )
        eq_triangle = pygame.draw.polygon(
            screen,
            BLACK, 
            [(350, 70), (350+25/2,70-(math.sqrt(3)*25)/2), (375, 70)],
            width=3
        )
        screen.blit(self.rhombus, self.rhombus_rect)
        screen.blit(self.pen, self.pen_rect)
    
class Pen(GameObject):
    def __init__(self, size, color, *arg, **kwargs):
        self.points: list[Point,] = []
        self.size = size
        self.color = color

    def draw(self):
        for ind, point in enumerate(self.points[:-1]):
            next_point = self.points[ind+1]
            pygame.draw.line(
                screen,
                self.color,
                start_pos=(point.x, point.y),
                end_pos=(next_point.x, next_point.y),
                width=self.size
            )
        
    def update(self, current_pos):
        self.points.append(Point(*current_pos))

def draw_menu(current_pen, current_color):
    pygame.draw.rect(screen, GREY, (0, 0, WIDTH, 100))
    pygame.draw.line(screen, BLACK, (0, 100), (WIDTH, 100), 3)
    size_pen_small = pygame.draw.rect(screen, BLACK, (20, 20, 50, 50))
    pygame.draw.circle(screen, WHITE, (45, 45), 10)
    size_pen_big = pygame.draw.rect(screen, BLACK, (80, 20, 50, 50))
    pygame.draw.circle(screen, WHITE, (105, 45), 5)
    pen_list = [ size_pen_small, size_pen_big, ]

    if current_pen == 10:
        pygame.draw.rect(screen, GREEN, (20, 20, 50, 50), 3)
    elif current_pen == 5:
        pygame.draw.rect(screen, GREEN, (80, 20, 50, 50), 3)

    pygame.draw.circle(screen, current_color, (480, 45), 15)
    

    blue = pygame.draw.rect(screen, BLUE, (WIDTH-35, 20, 25, 25))
    red = pygame.draw.rect(screen, RED, (WIDTH-35, 45, 25, 25))
    green = pygame.draw.rect(screen, GREEN, (WIDTH-60, 20, 25, 25))
    yellow = pygame.draw.rect(screen, YELLOW, (WIDTH-60, 45, 25, 25))
    white = pygame.draw.rect(screen, WHITE, (WIDTH-85, 20, 25, 25))
    black = pygame.draw.rect(screen, BLACK, (WIDTH-85, 45, 25, 25))
    color_section = [blue, red, green, yellow, white, black]
    RGB = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255), (0, 0, 0)]

    return pen_list, color_section, RGB

class Rectangle(GameObject):
    def __init__(self, size, color, start_pos, *arg, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = color
        self.size = size

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            screen,
            self.color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Square(GameObject):
    def __init__(self, size, color, start_pos, *arg, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = color
        self.size = size

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            screen,
            self.color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_x - start_pos_x,
            ),
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Circle(GameObject):
    def __init__(self, size, color, start_pos, *args, **kwargs):
        self.size = size
        self.color = color 
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.ellipse(
            screen,
            self.color,
            # (
            #     start_pos_x+abs(end_pos_x - start_pos_x)//2, 
            #     start_pos_y+abs(end_pos_x - start_pos_x)//2
            # ),
            # radius= abs(end_pos_x - start_pos_x)//2,
            (   start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=self.size
        )
    
    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Eraser(GameObject):
    def __init__(self, size, *args, **kwargs):
        self.points: list[Point,] = []
        self.size = size

    def draw(self):
        for ind, point in enumerate(self.points[:-1]):
            next_point = self.points[ind+1]
            pygame.draw.line(
                screen,
                WHITE,
                start_pos=(point.x, point.y),
                end_pos=(next_point.x, next_point.y),
                width=self.size
            )
        
    def update(self, current_pos):
        self.points.append(Point(*current_pos))

class Right_triangle(GameObject):
    def __init__(self,size, color, start_pos, *arg):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = color
        self.size = size
        

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)



        pygame.draw.polygon(
            screen,
            self.color,
            [
                (start_pos_x, start_pos_y),
                (end_pos_x, end_pos_y),
                (min(self.start_pos.x, self.end_pos.x),max(self.start_pos.y, self.end_pos.y)),
            ],
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Equilateral_triangle(GameObject):
    def __init__(self,size, color, start_pos, *arg):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = color
        self.size = size
        

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        height = (abs(start_pos_x - end_pos_x)*math.sqrt(3))/2

        pygame.draw.polygon(
            screen,
            self.color,
            [
                (start_pos_x, start_pos_y),
                (end_pos_x, end_pos_y),
                # (max(self.start_pos.x-(end_pos_x-start_pos_x), max(end_pos_x, start_pos_x) - end_pos_x),max(self.start_pos.y, self.end_pos.y))
                (start_pos_x - (end_pos_x - start_pos_x), start_pos_y + (end_pos_y-start_pos_y)),
            ],
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Rhombus(GameObject):
    def __init__(self,size, color, start_pos, *arg):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = color
        self.size = size
        

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        

        pygame.draw.polygon(
            screen,
            self.color,
            [
                (start_pos_x, start_pos_y),
                (start_pos_x+math.hypot(end_pos_x-start_pos_x, end_pos_y-start_pos_y),start_pos_y),
                (end_pos_x+math.hypot(end_pos_x-start_pos_x, end_pos_y-start_pos_y),end_pos_y),
                (end_pos_x,end_pos_y)
            ],
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


game_obj = GameObject()
current_shape = Pen
active_obj = game_obj
buttons = Button_1()
objects = [
    buttons,
   
]
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BACKGROUND_COLOR)

    mouse = pygame.mouse.get_pos()
    if mouse[1] > 100:
        pygame.draw.circle(screen, active_color, mouse, active_pen)
    pens, colors, RGB =  draw_menu(active_pen, active_color)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for _ in range(len(pens)):
                if pens[_].collidepoint(event.pos):
                    active_pen = 10 - (_ * 5)
            
            
            for _ in range(len(colors)):
                if colors[_].collidepoint(event.pos):
                    active_color = RGB[_]


            if buttons.rect.collidepoint(event.pos):
                current_shape = Rectangle
            elif buttons.circle.collidepoint(event.pos):
                current_shape = Circle
            elif buttons.square.collidepoint(event.pos):
                current_shape = Square
            elif buttons.r_triangle.collidepoint(event.pos):
                current_shape = Right_triangle
            elif buttons.eq_triangle.collidepoint(event.pos):
                current_shape = Equilateral_triangle
            elif buttons.rhombus_rect.collidepoint(event.pos):
                current_shape = Rhombus
            elif buttons.pen_rect.collidepoint(event.pos):
                current_shape = Pen
            elif buttons.rect_1.collidepoint(event.pos):
                current_shape = Eraser
                active_color = RGB[4]
            else:
                active_obj = current_shape(active_pen, active_color,start_pos=event.pos)
                objects.append(active_obj)  # type: ignore


        if event.type == pygame.MOUSEMOTION:
            active_obj.update(current_pos = pygame.mouse.get_pos())
        
        if event.type == pygame.MOUSEBUTTONUP:
            active_obj = game_obj
            
    for obj in objects:
        obj.draw()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()