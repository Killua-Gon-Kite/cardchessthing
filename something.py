import random
import sys, pygame

pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((1200, 1800))
  
# Initialing Color
color = (255, 255, 255)
  
# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()
