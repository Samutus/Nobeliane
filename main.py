import time

from classGame import Game
import pygame
import pygame

pygame.init()
# -------Importation des images-------

title = pygame.image.load('ressources/title.png')
play = pygame.image.load('ressources/play.png')

bg1 = pygame.image.load('gif_bg/frame_00_delay-0.1s.gif')
bg2 = pygame.image.load('gif_bg/frame_01_delay-0.1s.gif')
bg3 = pygame.image.load('gif_bg/frame_02_delay-0.1s.gif')
bg4 = pygame.image.load('gif_bg/frame_03_delay-0.1s.gif')
bg5 = pygame.image.load('gif_bg/frame_04_delay-0.1s.gif')
bg6 = pygame.image.load('gif_bg/frame_05_delay-0.1s.gif')
bg6bis = pygame.image.load('gif_bg/frame_06_delay-0.1s.gif')
bg7 = pygame.image.load('gif_bg/frame_07_delay-0.1s.gif')
bg8 = pygame.image.load('gif_bg/frame_08_delay-0.1s.gif')
bg9 = pygame.image.load('gif_bg/frame_09_delay-0.1s.gif')
bg10 = pygame.image.load('gif_bg/frame_10_delay-0.1s.gif')
bg11 = pygame.image.load('gif_bg/frame_11_delay-0.1s.gif')
bg12 = pygame.image.load('gif_bg/frame_12_delay-0.1s.gif')
bg13 = pygame.image.load('gif_bg/frame_13_delay-0.1s.gif')
bg14 = pygame.image.load('gif_bg/frame_14_delay-0.1s.gif')
bg15 = pygame.image.load('gif_bg/frame_15_delay-0.1s.gif')
bg16 = pygame.image.load('gif_bg/frame_16_delay-0.1s.gif')
bg17 = pygame.image.load('gif_bg/frame_17_delay-0.1s.gif')
bg18 = pygame.image.load('gif_bg/frame_18_delay-0.1s.gif')
bg19 = pygame.image.load('gif_bg/frame_19_delay-0.1s.gif')
bg20 = pygame.image.load('gif_bg/frame_20_delay-0.1s.gif')
bg21 = pygame.image.load('gif_bg/frame_21_delay-0.1s.gif')
bg22 = pygame.image.load('gif_bg/frame_22_delay-0.1s.gif')
bg23 = pygame.image.load('gif_bg/frame_23_delay-0.1s.gif')
bg24 = pygame.image.load('gif_bg/frame_24_delay-0.1s.gif')
bg25 = pygame.image.load('gif_bg/frame_25_delay-0.1s.gif')
bg26 = pygame.image.load('gif_bg/frame_26_delay-0.1s.gif')
bg27 = pygame.image.load('gif_bg/frame_27_delay-0.1s.gif')
bg28 = pygame.image.load('gif_bg/frame_28_delay-0.1s.gif')
bg29 = pygame.image.load('gif_bg/frame_29_delay-0.1s.gif')
bg30 = pygame.image.load('gif_bg/frame_30_delay-0.1s.gif')
bg31 = pygame.image.load('gif_bg/frame_31_delay-0.1s.gif')
bg32 = pygame.image.load('gif_bg/frame_32_delay-0.1s.gif')
bg33 = pygame.image.load('gif_bg/frame_33_delay-0.1s.gif')
bg34 = pygame.image.load('gif_bg/frame_34_delay-0.1s.gif')
bg35 = pygame.image.load('gif_bg/frame_35_delay-0.1s.gif')
bg36 = pygame.image.load('gif_bg/frame_36_delay-0.1s.gif')
bg37 = pygame.image.load('gif_bg/frame_37_delay-0.1s.gif')
bg38 = pygame.image.load('gif_bg/frame_38_delay-0.1s.gif')
bg39 = pygame.image.load('gif_bg/frame_39_delay-0.1s.gif')

# -------définition de la fenêtre-------
pygame.display.set_caption('Nobeliane')
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
x = screen.get_size()[0]
y = screen.get_size()[1]
bg = [bg1, bg2, bg3, bg4, bg5, bg6, bg6bis, bg7, bg8, bg9, bg10, bg12, bg13, bg14, bg15, bg16, bg17, bg18, bg19, bg20,
      bg21, bg22, bg23, bg24, bg25, bg26, bg27, bg28, bg29, bg30, bg31, bg32, bg33, bg34, bg35, bg36, bg37, bg38, bg39]

# -------Initialisation de la musique et son -------
file = 'ressources/main_theme.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# ------Bouttons------
play_size = pygame.transform.scale(play, (340, 90))
play_place = screen.get_rect(midbottom=(x - (x / 9.8), y + (y / 1.9)))

running = True
while running:
    for i in range(len(bg) - 1):

        screen.blit(pygame.transform.scale(bg[i], (x, y)), (0, 0))

        screen.blit(title, (screen.get_rect(midbottom=(x - 340, y + (y / 8.2)))))

        e = screen.blit(play_size, play_place)

        time.sleep(0.1)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if e.collidepoint(pygame.mouse.get_pos()):
                    pygame.init()
                    classGame = Game()
                    classGame.run()
            if event.type == pygame.QUIT:
                running = False
