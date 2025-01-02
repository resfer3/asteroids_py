import pygame
from constants import *
from circleshape import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  # FPS
  clock = pygame.time.Clock()
  dt = 0

   # groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  # fill groups
  Player.containers = (updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  
   # generate player
  x_center = SCREEN_WIDTH / 2
  y_center = SCREEN_HEIGHT / 2
  player = Player(x_center, y_center)

 # generate asteroids
  asteroid_field = AsteroidField()


  while(True):
    # close window
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return   
    
    #print(f"Updatable group size: {len(updatable)}")
    #print(f"Drawable group size: {len(drawable)}")
    #print(f"Asteroids group size: {len(asteroids)}")

    # update game
    for item in updatable:
      item.update(dt)

    for asteroid in asteroids:
      if player.collision(asteroid):
        print("Game Over")
        return

    # fill the screen with a black background
    screen.fill((0, 0, 0))
    
    # draw objects
    for art in drawable:
      art.draw(screen)

    # reset view
    pygame.display.flip()
    
    # 60 FPS 
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
