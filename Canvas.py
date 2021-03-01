import pygame
import numpy as np
import time

pygame.init()

size = width, height = 600, 600
bg = 50, 50, 50

screen = pygame.display.set_mode(size)

cellsX = cellsY = 50

cellsWidth = width / cellsX
cellsHeight = height / cellsY

tableState = np.zeros((cellsX, cellsY))

tableState[22, 22] = 1
tableState[23, 22] = 1
tableState[24, 22] = 1
tableState[24, 23] = 1
tableState[23, 21] = 1

tableState[25, 40] = 1
tableState[26, 40] = 1
tableState[27, 40] = 1
tableState[28, 40] = 1
tableState[29, 40] = 1

tableState[5, 40] = 1
tableState[4, 40] = 1
tableState[3, 40] = 1
tableState[2, 39] = 1
tableState[1, 39] = 1
tableState[49, 39] = 1

tableState[8, 40] = 1
tableState[9, 40] = 1
tableState[10, 40] = 1
tableState[11, 39] = 1
tableState[12, 39] = 1
tableState[13, 39] = 1
tableState[15, 39] = 1
tableState[16, 39] = 1
tableState[17, 39] = 1

tableState[5, 49] = 1
tableState[4, 49] = 1
tableState[3, 49] = 1

play = True

while 1:

    newTableState = np.copy(tableState)
    screen.fill(bg)
    keyboradPress = pygame.event.get()

    for event in keyboradPress:
        if event.type == pygame.KEYDOWN:
            play = not play

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            X,Y = pygame.mouse.get_pos()
            celc, cely = int(np.floor(X/cellsWidth)),int(np.floor(Y/cellsHeight))
            newTableState[celc,cely] = not mouseClick[2]


    for j in range(0, cellsX):
        for i in range(0, cellsY):
            if play:


                neighborsCells = tableState[(i + 1) % cellsX, (j - 1) % cellsY] + \
                                tableState[(i + 1) % cellsX, j % cellsY] + \
                                tableState[(i + 1) % cellsX, (j + 1) % cellsY] + \
                                tableState[i % cellsX, (j - 1) % cellsY] + \
                                tableState[i % cellsX, (j + 1) % cellsY] + \
                                tableState[(i - 1) % cellsX, (j - 1) % cellsY] + \
                                tableState[(i - 1) % cellsX, j % cellsY] + \
                                tableState[(i - 1) % cellsX, (j + 1) % cellsY]
                # tableState[(x) % cellsX, (y) % cellsY]


                if tableState[i, j] == 0 and neighborsCells == 3:
                    newTableState[i, j] = 1
                elif tableState[i, j] == 1 and (neighborsCells < 2 or neighborsCells > 3):
                    newTableState[i, j] = 0


            poly = [(i * cellsWidth, j * cellsHeight),
                    ((i + 1) * cellsWidth, j * cellsHeight),
                    ((i + 1) * cellsWidth, (j + 1) * cellsHeight),
                    (i * cellsWidth, (j + 1) * cellsHeight)]

            pygame.draw.polygon(screen, (88, 94, 150), poly, int(abs(1 - tableState[i, j])))
            
    tableState = np.copy(newTableState)
    time.sleep(0.1)
    pygame.display.flip()
