import os
import time
import pygame
from pygame.locals import *
import random
import math

#outros_scripts
#import marcos_alpha
#import main_03
#import ending

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=800
screen_height=600
WINSIZE = [screen_width, screen_height]
WINCENTER = [screen_width/2, screen_height/2]
screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

#defs das estrelas
def init_star():
    "creates new star values"
    dir = random.randrange(100000)
    velmult = random.random()*.6+.4
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    return vel, WINCENTER[:]

def initialize_stars():
    "creates a new starfield"
    stars = []
    for x in range(NUMSTARS):
        star = init_star()
        vel, pos = star
        steps = random.randint(0, WINCENTER[0])
        pos[0] = pos[0] + (vel[0] * steps)
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * .09)
        vel[1] = vel[1] * (steps * .09)
        stars.append(star)
    move_stars(stars)
    return stars

def draw_stars(surface, stars, color):
    "used to draw (and clear) the stars"
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)

def move_stars(stars):
    "animate the star values"
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            vel[:], pos[:] = init_star()
        else:
            vel[0] = vel[0] * 1.05
            vel[1] = vel[1] * 1.05

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "bebas.ttf"
font1 = "munro.ttf"

ref = pygame.image.load("pos_game_01.jpg")

# Game Framerate
clock = pygame.time.Clock()
FPS=60
NUMSTARS = 150

def teorica(screen): 
    
    running = True
    
    # - mainloop -      
    #screen.fill(white)
    screen.blit(ref, (0,0))
    
    #text
    text_back=text_format("NEXT", font, 35, red)
    back_rect=text_back.get_rect()
    screen.blit(text_back, (screen_width/2 - (back_rect[2]/2), 490))
    
    # - draws -
    pygame.display.flip()
    
    #time.sleep(1)
    
    # - FPS -
    while running:
        
        # - events -
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #main_menu(screen)
                    agradecimentos(screen)
                    
def agradecimentos(screen): 
    
    running = True
    
    # - mainloop -      
    screen.fill(black)
    
    text_back1=text_format("THANK YOU FOR PLAYING", font1, 35, white)
    back1_rect=text_back1.get_rect()
    screen.blit(text_back1, (screen_width/2 - (back1_rect[2]/2), 240))
    
    text_back2=text_format("See you space cowboy...", font1, 30, white)
    back2_rect=text_back2.get_rect()
    screen.blit(text_back2, (screen_width/2 - (back2_rect[2]/2), 285))
    """
    text_back5=text_format("* Icaro Meidem", font1, 35, white)
    back5_rect=text_back5.get_rect()
    screen.blit(text_back5, (screen_width/2 - (back5_rect[2]/2), 240))
    
    text_back6=text_format("* Marcos Faria", font1, 35, white)
    back6_rect=text_back6.get_rect()
    screen.blit(text_back6, (screen_width/2 - (back6_rect[2]/2), 285))
    """
    #text
    text_back=text_format("EXIT", font, 35, red)
    back_rect=text_back.get_rect()
    screen.blit(text_back, (screen_width/2 - (back_rect[2]/2), 490))
    
    # - draws -
    pygame.display.flip()
    
    #time.sleep(1)
    
    # - FPS -
    while running:
        
        # - events -
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #main_menu(screen)
                    pygame.quit()
                    quit()

def about_screen(screen):
    
    running = True
    #flag=True
    
    # - mainloop -      

    screen.fill(black)
    #text
    
    text_back1=text_format("    Coding, art and scientific knowledge by:", font1, 35, white)
    back1_rect=text_back1.get_rect()
    screen.blit(text_back1, (screen_width/2 - (back1_rect[2]/2), 55))
    
    text_back2=text_format("* Daniel Mendes", font1, 35, white)
    back2_rect=text_back2.get_rect()
    screen.blit(text_back2, (screen_width/2 - (back2_rect[2]/2), 105))
    
    text_back3=text_format("* Everson Henrique", font1, 35, white)
    back3_rect=text_back3.get_rect()
    screen.blit(text_back3, (screen_width/2 - (back3_rect[2]/2), 150))
    
    text_back4=text_format("* Gabriella Correa", font1, 35, white)
    back4_rect=text_back4.get_rect()
    screen.blit(text_back4, (screen_width/2 - (back4_rect[2]/2), 195))
    
    text_back5=text_format("* Icaro Meidem", font1, 35, white)
    back5_rect=text_back5.get_rect()
    screen.blit(text_back5, (screen_width/2 - (back5_rect[2]/2), 240))
    
    text_back6=text_format("* Marcos Faria", font1, 35, white)
    back6_rect=text_back6.get_rect()
    screen.blit(text_back6, (screen_width/2 - (back6_rect[2]/2), 285))
    
    text_back=text_format("BACK", font, 35, red)
    back_rect=text_back.get_rect()
    screen.blit(text_back, (screen_width/2 - (back_rect[2]/2), 490))
    
    # - draws -
    pygame.display.flip()
    
    #time.sleep(1)
    
    # - FPS -
    while running:
        
        # - events -
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu(screen)

# Main Menu
def main_menu(screen):

    menu=True
    selected="start"
    
    #flags
    start_flag=1
    about_flag=0
    quit_flag=0
    #done_estrelas = 0
    
    random.seed()
    stars = initialize_stars()
    
    #background:
    #screen.fill(black)
    #screen.blit(bg, (0,0))

    while menu:
        screen.blit(bg, (0,0))
        draw_stars(screen, stars, black)
        move_stars(stars)
        draw_stars(screen, stars, white)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if start_flag==1:
                        selected="quit"
                        start_flag=0
                        quit_flag=1
                    elif about_flag==1:
                        selected="start"
                        about_flag=0
                        start_flag=1
                    elif quit_flag==1:
                        selected="about"
                        quit_flag=0
                        about_flag=1
                    
                elif event.key==pygame.K_DOWN:
                    if start_flag==1:
                        selected="about"
                        start_flag=0
                        about_flag=1
                    elif about_flag==1:
                        selected="quit"
                        about_flag=0
                        quit_flag=1
                    elif quit_flag==1:
                        selected="start"
                        quit_flag=0
                        start_flag=1             
                    
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        info_start(screen)
                    if selected=="about":
                        about_screen(screen)
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        
        #title=text_format("Sourcecodester", font, 90, yellow)
        if selected=="start":
            text_start=text_format("START", font, 35, red)
        else:
            text_start = text_format("START", font, 35, white)
        if selected=="about":
            text_about=text_format("ABOUT", font, 35, red)
        else:
            text_about = text_format("ABOUT", font, 35, white)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 35, red)
        else:
            text_quit = text_format("QUIT", font, 35, white)

        #title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        about_rect=text_about.get_rect()
        quit_rect=text_quit.get_rect()
        
        # Main Menu Text
        #screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 400))
        screen.blit(text_about, (screen_width/2 - (about_rect[2]/2), 445))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 490))
        
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("python test game alpha")

#controle de screen

#Initialize the Game

teorica(screen)
pygame.quit()
quit()