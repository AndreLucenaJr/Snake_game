#imports
import pygame, sys
from pygame.locals import*
import time
import random

pygame.init()

#set the game screen
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake Game')
pygame.display.update()

#Create the snake
x, y = 200, 200
delta_X, delta_y = 0, 0

def snake():
    global x, y
    x = x + delta_x
    y = y + delta_y
    pygame.draw.rect(screen, (255, 255, 255), [x, y, 10, 10])
    pygame.display.update()


#set the events
while True:
    events = pygame.event.get()
    for event in events:
        #set the Quit event
        if event.type == QUIT:
            quit() 
        #Set the move events of the snake
        if (event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):  
                delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                delta_x = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                delta_x = 0
                delta_y = -10
            elif(event.key == pygame.K_DOWN):
                delta_x = 0
                delta_y = 10
            else:
                continue
                
            snake()
