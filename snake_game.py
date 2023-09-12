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
delta_x, delta_y = 0, 0

apple_x, apple_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10

body_list = [(x, y)]

clock = pygame.time.Clock()
  
def snake():
    global x, y, apple_x, apple_y
    x = (x + delta_x)%width
    y = (y + delta_y)%height
    
    body_list.append((x,y))
    
    if apple_x == x and apple_y == y:
        while ((apple_x, apple_y) in body_list):
            apple_x, apple_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10
    else:
        del body_list[0]
        
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), [apple_x, apple_y, 10, 10])
    for (i,j) in body_list:
        pygame.draw.rect(screen, (255, 255, 255), [i, j, 10, 10])
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
                if (delta_x != 10):
                    delta_x = -10
                delta_y = 0
            elif(event.key == pygame.K_RIGHT):
                if (delta_x != -10):
                    delta_x = 10
                delta_y = 0
            elif(event.key == pygame.K_UP):
                delta_x = 0
                if (delta_y != 10):
                    delta_y = -10
            elif(event.key == pygame.K_DOWN):
                delta_x = 0
                if(delta_y != -10):
                    delta_y = 10
            else:
                continue
            snake()
    if(not events):
        snake()
    clock.tick(10)