import pygame
from pygame.locals import *
import sys, os
import time

pygame.init()
pygame.display.set_caption('Paintme')
mouse = pygame.mouse
fpsClock = pygame.time.Clock()

width = 720
height = 440

window = pygame.display.set_mode((width, height))
canvas = window.copy()

BLACK = pygame.Color( 0 ,  0 ,  0 )
WHITE = pygame.Color(255, 255, 255)

left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
canvas.fill(WHITE)
prevcod=pygame.mouse.get_pos()
while True:
  for event in pygame.event.get():
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif left_pressed:
      cod=pygame.mouse.get_pos()
      #pygame.draw.circle(canvas, BLACK, (cod),5)
      print(cod)
      pygame.draw.line(canvas, BLACK, prevcod, cod, 5) 
      prevcod=cod
  window.fill(WHITE)
  window.blit(canvas, (0, 0))
  time.sleep(0.05)
  #pygame.draw.circle(window, BLACK, (pygame.mouse.get_pos()), 5)
  pygame.display.update()