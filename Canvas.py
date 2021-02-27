import pygame
import numpy as np
import time
import math

pygame.init()

Size = width, height = 600, 600
Bg = 60, 60, 60

Screen = pygame.display.set_mode(Size)
Screen.fill(Bg)

CellsX = CellsY = 50

CellsWidth = (width) / CellsX
CellsHeight = (height) / CellsY

while 1:
    for x in range(CellsX):
        for y in range(CellsY):

    pygame.display.flip()