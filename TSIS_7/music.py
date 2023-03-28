# import pygame


# pygame.init()


# musics = []

# song_end =  pygame.USEREVENT + 1
# pygame.mixer.music.set_endevent(song_end)

# musics.append(pygame.mixer.music.load("crash-adams-feat.-king-vvibe-destination-freestyle.mp3"))
# musics.append(pygame.mixer.music.load("Crash Adams — Give Me A Kiss (Official Lyric Video) (www.lightaudio.ru).mp3"))
# print(musics)

# def play_next_song():
#     global musics
#     musics = musics[1:] + [musics[0]]
#     pygame.mixer.music.load(musics[0])
#     pygame.mixer.music.play()

# import random

# currently_playing_song = None
# def play_a_different_song():
#     global currently_playing_song, musics
#     next_song = random.choice(musics)
#     while next_song == currently_playing_song:
#         next_song = random.choice(musics)
#     _currently_playing_song = next_song
#     pygame.mixer.music.load(next_song)
#     pygame.mixer.music.play()


# WIDTH, HEIGHT = 700, 700
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()
# pygame.display.set_caption("Music")



# working = True


# pygame.mixer.music.play()
# while working:
#     screen.fill((145, 145, 188))

#     for event in pygame.event.get():
#         if (event.type is pygame.QUIT) or (event.type is song_end):
#             print("the song ended!")
#             working = False
        
    
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.K_RIGHT]:
#         play_a_different_song()


#     if pressed[pygame.K_SPACE]:
#         if pygame.mixer.music.pause():
#             pygame.mixer.music.unpause()
#         if pygame.mixer.music.unpause():
#             pygame.mixer.music.pause()


#     clock.tick(60)
#     pygame.display.flip()


import pygame


pygame.init()


musics = []
musics.append("crash-adams-feat.-king-vvibe-destination-freestyle.mp3")
musics.append("Crash Adams — Give Me A Kiss (Official Lyric Video) (www.lightaudio.ru).mp3")

pygame.mixer.music.load(musics[0])
musics.pop(0)
pygame.mixer.music.play()

pygame.mixer.music.load(musics[0])
musics.pop(0)


WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



working = True
while working:
    screen.fill((145, 145, 188))

    for event in pygame.event.get():
        if (event.type is pygame.QUIT):
            print("the song ended!")
            working = False
        
    if len(musics) > 0:
        pygame.mixer.music.queue(musics[0])
        musics.pop(0)

    clock.tick(60)
    pygame.display.flip()

