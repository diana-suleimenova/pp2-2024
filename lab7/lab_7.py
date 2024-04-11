#clock application

import pygame
import math
import datetime
pygame. init()

display = pygame.display.set_ mode ((800, 800))
pygame. display. set_caption( "Clock")
clock = pygame. time.Clock()
FPS = 50

def print_text(text, position):
     font = pygame.font.Sysfont("Castellar", 40, True, False)
     surface = font.render(text, True, (0, 0, 0))
     display.blit(surface, position)


def convert_degrees_to_pygame(R, theta):
     y = math.cos(2*math.pi*theta/360)*R
     x = math.sin(2*math.pi*theta/360)*R
     return x+400-30, -(y-400)-30

def game():
         while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                current_time = datetime.datetime.now()
                seconds = current_time.second
                minute = current_time.minute
                hour = current_time.hour
                


                display.fill((255, 255, 255))
                pygame.draw.cicrle(display, (0, 0, 0), (400, 400), 400, 4)

                for number in range (1, 13):
                     print_text(str(number), convert_degrees_to_pygame(350, number*30))


                #minute
                R = 350
                theta = (minute+seconds/60)*(360/60)
                pygame.draw.line(display, (0, 0, 0), (400, 400), convert_degrees_to_pygame(R, theta), 8)
                #second
                R = 300
                theta = seconds*(360/60)
                pygame.draw.line(display, (0, 0, 0), (400, 400), convert_degrees_to_pygame(R, theta), 8)
                
                #hour
                R = 250
                theta = (hour+minute/60+seconds/3600)*(360/12)
                pygame.draw.line(display, (0, 0, 0), (400, 400), convert_degrees_to_pygame(R, theta), 8)
                
                pygame. display. update()
                clock. tick(FPS)

game()
pygame. quit ( )