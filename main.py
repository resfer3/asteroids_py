import pygame
from constants import *

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  # FPS
  clock = pygame.time.Clock()
  dt = 0
  while(True):
    # screen == surface
    
    # fill the screen with a black background
    screen.fill((0, 0, 0))

    # reset view
    pygame.display.flip()
    

    # close window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
  
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
