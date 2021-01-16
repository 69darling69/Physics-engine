if __name__ == "__main__":
  import random
  import math
  import pygame as pg
  from particle import Particle
  #from parameters import *

  # Window size
  WIDTH = 500
  HEIGHT = 500

  FPS = 60

  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  RED = (255, 0, 0)
  BLUE = (0, 0, 255)

  window = pg.display.set_mode((WIDTH, HEIGHT))

  isPressed = False

  particles = list()

  while True:
    window.fill(WHITE)
    for event in pg.event.get():

      if event.type == pg.QUIT:
        pg.quit()

      elif (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1):
        isPressed = True
        startPos = pg.mouse.get_pos()

      elif (event.type == pg.MOUSEBUTTONUP) and (event.button == 1):
        isPressed = False
        endPos = pg.mouse.get_pos()
        if endPos != startPos:
          particles.append(Particle(pg.math.Vector2(startPos[0], startPos[1]), math.sqrt((startPos[0] - endPos[0])**2 + (startPos[1] - endPos[1])**2)))

    if isPressed:
        pg.draw.circle(window, BLUE, startPos, math.sqrt((startPos[0] - pg.mouse.get_pos()[0])**2 + (startPos[1] - pg.mouse.get_pos()[1])**2))

    for particle in particles:
      particle.update(window, particles)
      particle.draw(window)

    pg.display.flip()
    pg.time.Clock().tick(FPS)
