import math
from random import random

import pygame

import _quixl, _watermark

pygame.init()

size = 16
screen = pygame.display.set_mode((787, 512))
pygame.display.set_caption("quixl")

pixelDisplaySize = 512/size

running = True

art = [()]*(size*size)

print(art)

i = -1
for color in art:
    i += 1
    art[i] = (-1,-1,-1)

print(art)

mousedown = False
rightmousedown = False

colorSelection = (0,0,0)

showMiddle = False
showGrid = False
showAlpha = True
showWatermark = False

complexMode = False
complexFont = pygame.font.SysFont("Roboto-Regular.ttf", 16)

_watermark.init()

def createNew(width):
    global size, art, pixelDisplaySize
    size = width
    art = [()] * (size * size)
    pixelDisplaySize = 512 / size

    i = -1
    for color in art:
        i += 1
        art[i] = (-1, -1, -1)
    print(f"New {width}x{width}")

while running:
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,screen.get_width(),screen.get_height()))

    _quixl.drawPixelGrid(screen, art, size, pixelDisplaySize, showMiddle, showGrid, showAlpha)
    _quixl.drawUI(screen, colorSelection)
    _quixl.drawColorOverlay(screen, colorSelection, pygame.mouse.get_pos())
    if showWatermark: _watermark.draw(screen)
    if complexMode: _quixl.drawComplex(screen, complexFont, colorSelection)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: mousedown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: mousedown = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: rightmousedown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3: rightmousedown = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            x, y = pygame.mouse.get_pos()
            if (x <= 511):
                x = math.floor(x / (512 / size))
                y = math.floor(y / (512 / size))
                index = x + size * y
                colorSelection = art[index]
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_s): _quixl.saveImage(art, size)
            if (event.key == pygame.K_o):
                try:
                    art, size, pixelDisplaySize = _quixl.openImage()
                except(FileNotFoundError):
                    print("quixl.png could not be found")
            if (event.key == pygame.K_n or event.key == pygame.K_BACKSPACE or event.key == pygame.K_r or event.key == pygame.K_x): createNew(size)
            if (event.key == pygame.K_ESCAPE): running = False

            if (event.key == pygame.K_1): createNew(4)
            if (event.key == pygame.K_2): createNew(8)
            if (event.key == pygame.K_3): createNew(16)
            if (event.key == pygame.K_4): createNew(32)
            if (event.key == pygame.K_5): createNew(64)
            if (event.key == pygame.K_6): createNew(128)

            if (event.key == pygame.K_t): showMiddle = not showMiddle
            if (event.key == pygame.K_g): showGrid = not showGrid
            if (event.key == pygame.K_j):
                print("Jumbling")
                for index in range(size*size):
                    art[index] = (round(random()*255),round(random()*255),round(random()*255))
            if (event.key == pygame.K_w): showWatermark = not showWatermark

            if (event.key == pygame.K_c): complexMode = not complexMode

            if (event.key == pygame.K_RIGHTBRACKET):
                r,g,b = colorSelection
                colorSelection = (min(r+10, 255),min(g+10, 255),min(b+10, 255))
            if (event.key == pygame.K_LEFTBRACKET):
                r,g,b = colorSelection
                colorSelection = (max(r-10, 0),max(g-10, 0),max(b-10, 0))
            #if (event.key == pygame.K_a): showAlpha = not showAlpha
    if mousedown:
        colorSelection = _quixl.colorPresetSelection(colorSelection)
        x, y = pygame.mouse.get_pos()
        if (x <= 511):
            x = math.floor(x / (512 / size))
            y = math.floor(y / (512 / size))
            index = x + size * y
            art[index] = colorSelection
        else:
            if 522 <= x <= 777:
                cr, cg, cb = colorSelection
                if 85 >= y >= 10: colorSelection = (x-522,cg,cb)
                if 160 >= y >= 85: colorSelection = (cr,x-522,cb)
                if 235 >= y >= 160: colorSelection = (cr,cg,x-522)
                if 310 >= y >= 235: colorSelection = (x-522,x-522,x-522)
    if rightmousedown:
        x, y = pygame.mouse.get_pos()
        if (x <= 511):
            x = math.floor(x / (512 / size))
            y = math.floor(y / (512 / size))
            index = x + size * y
            art[index] = (-1,-1,-1)
