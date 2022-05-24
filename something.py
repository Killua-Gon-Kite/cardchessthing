import random
import sys, pygame

pygame.init()
  
surface = pygame.display.set_mode((1200, 1800))
  
color = (255, 255, 255)

surface = pygame.display.set_mode((1200, 1800))
  
color = (255, 255, 255)
  
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()