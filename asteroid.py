from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    # stop if: asteroid is smallest
    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    # else: spawn 2 more asteroids
    random_angle = random.uniform(20, 50)
    #print(random_angle)
    # create new velocity with their angles
    velocity1 = self.velocity.rotate(random_angle)
    velocity2 = self.velocity.rotate(-random_angle)
    #print(velocity1)
    #print(velocity2)
    # compute new radius
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    #print(new_radius)
    # Create 2 new asteroids and set their velocity
    new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_1.velocity = velocity1 * 1.2
    new_asteroid_2.velocity = velocity2 * 1.2



    
