import pygame as pg
import math
import random

class Particle:
  position = pg.math.Vector2()
  velocity = pg.math.Vector2()
  color = pg.Color(100, 100, 100)
  radius = 25
  elasticity = .75
  mass = 1
  resistance = .00005

  def __init__(self, position, radius = 25):
    self.position = position
    self.velocity = pg.math.Vector2(0.0, 0.0)
    self.mass = self.radius = radius

  def applyForce(self, force):
        self.velocity += force

  def draw(self, window):
    pg.draw.circle(window, self.color, self.position, self.radius)

  def update(self, window, particles):
    for another in particles:
        if another != self:
            # Check collide
            if ((another.position.x - self.position.x)**2 + (another.position.y - self.position.y)**2) < (another.radius + self.radius)**2:
                #TODO: simillary to another
                # Set position before collide
                self.position += (another.position - self.position).normalize() * (math.dist(another.position, self.position) - self.radius - another.radius) / 2
                # Change velocity vector
                self.velocity -= self.elasticity * 2 * another.mass / (self.mass + another.mass) * (self.position - another.position) * (self.velocity - another.velocity).dot(self.position - another.position) / (self.position - another.position).length()**2
    if window.get_size()[1] - self.radius < self.position[1]:
        self.position -= pg.math.Vector2(0, 1) * (self.position.y + self.radius - window.get_size()[1])
        #TODO: change apply force like collision
        self.applyForce(pg.math.Vector2(0, math.ceil(-abs(self.velocity.y * (1 + self.elasticity)))))
    self.applyForce(pg.math.Vector2(0, 1))
    # Resistance:
    # F = 6 * Pi * k * r * v
    self.applyForce(-self.velocity.normalize() * 6 * math.pi * self.resistance * self.radius * self.velocity.length())
    #self.velocity *= (1 - self.resistance)
    self.position += self.velocity
