import pygame

# Initializing
pygame.init()
pygame.mixer.init()

# Clock
clock = pygame.time.Clock()

musics = ['./music/first.mp3', './music/second.mp3']
currently_playing_music = 0

# Surface
screen = pygame.display.set_mode((400, 100))
pygame.display.set_caption("Music player")

# Starting the music
music = pygame.mixer.music.load(musics[currently_playing_music])
pygame.mixer.music.play()

# ICON
image = pygame.image.load("./images/unnamed.png")
size_of_icon = pygame.transform.scale(image, (100,80))
position_of_icon = (10, 10)


# Design
colors = [(128, 128, 128), (255, 255, 255), (255, 224, 32)] # gray, white, yellow
font = pygame.font.SysFont('Comicsansms', 24)


running = True
while running:

    # Cloth window event
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False
            

        # Bottoms 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else: pygame.mixer.music.unpause()
            
            elif event.key == pygame.K_LEFT:
                currently_playing_music  = (currently_playing_music - 1) % len(musics)
                pygame.mixer.music.load(musics[currently_playing_music])
                pygame.mixer.music.play()

            elif event.key == pygame.K_RIGHT:
                currently_playing_music  = (currently_playing_music + 1) % len(musics)
                pygame.mixer.music.load(musics[currently_playing_music])
                pygame.mixer.music.play()
    
    # Background color
    screen.fill(colors[0])

    # Text
    text = font.render(musics[currently_playing_music],True, colors[2])
    
    # Show the text and image 
    screen.blit(text,(140, 50))
    screen.blit(size_of_icon, position_of_icon)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

