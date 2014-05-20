#coding: UTF-8
import pygame
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE
 
blue = (0, 0, 255)
black = (0, 0, 0)
 
def init():
    pygame.init()
 
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Graficadora")
 
    return screen
 
def translate((x, y)):
    return (x + 320, 240 - y)
screen = init()
 
dx = 0.5
x = 0
def f(x):
    return x**2 / 100
        
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keyboard = pygame.key.get_pressed()
    if keyboard[K_ESCAPE]:
        exit()
    
    try:
        start_pos = (int(x), int(f(x)))
        end_pos = (int(x+dx), int(f(x+dx)))
        x += dx
    except ZeroDivisionError:
        break
    if x > 640:
        x = 0
    pygame.draw.line(screen, blue, translate(start_pos), translate(end_pos))
    pygame.display.flip()