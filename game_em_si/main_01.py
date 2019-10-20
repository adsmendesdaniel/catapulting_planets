import os
import pygame
from pygame.locals import *

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

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

# Game Framerate
clock = pygame.time.Clock()
FPS=60

# Main Menu
def main_menu():

    menu=True
    selected="start"
    
    #flags
    start_flag=1
    about_flag=0
    quit_flag=0

    while menu:
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
                        print("Start")
                    if selected=="about":
                        print("About")
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(black)
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
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

#Initialize the Game
main_menu()
pygame.quit()
quit()

"""
import pygame
# --- constants ---
WIDTH = 320
HEIGHT = 110
FPS = 5

# --- class ---

class Button(object):
    def __init__(self, position, size, color, text):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)
        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        self.image.blit(text, text_rect)
        # set after centering text
        self.rect.topleft = position
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

def stage1(screen):
    button1 = Button((5, 5), (100, 100), (0,255,0), "GO 1")
    button2 = Button((215, 5), (100, 100), (0,255,0), "EXIT")
    # - mainloop -
    clock = pygame.time.Clock()
    running = True
    while running:
        # - events -
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if button1.is_clicked(event):
                # go to stage2
                stage2(screen)
            if button2.is_clicked(event):
                # exit
                pygame.quit()
                exit()
        # - draws -
        screen.fill((255,0,0))    
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()
        # - FPS -
        clock.tick(FPS)

def stage2(screen):
    button1 = Button((5, 5), (100, 100), (255,0,0), "GO 2")
    button2 = Button((215, 5), (100, 100), (255,0,0), "BACK")
    # - mainloop -
    clock = pygame.time.Clock()
    running = True
    while running:
        # - events -
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if button1.is_clicked(event):
                stage3(screen)
            if button2.is_clicked(event):
                return

        # - draws -
        screen.fill((0,255,0))    
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()
        # - FPS -
        clock.tick(FPS)

def stage3(screen):
    button2 = Button((215, 5), (100, 100), (0,0,255), "BACK")
    # - mainloop -
    clock = pygame.time.Clock()
    running = True
    while running:
        # - events -
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button2.is_clicked(event):
                return
        # - draws -
        screen.fill((128,128,128))    
        button2.draw(screen)
        pygame.display.flip()
        # - FPS -
        clock.tick(FPS)

# --- main ---
# - init -
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# - start -
stage1(screen)
# - end -
pygame.quit()
"""