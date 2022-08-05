import math
from random import random

import pygame
from PIL import Image

import _quixl, _watermark

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

_watermark.init()

while running:
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,screen.get_width(),screen.get_height()))

    _quixl.drawPixelGrid(screen, art, size, pixelDisplaySize, showMiddle, showGrid, showAlpha)
    _quixl.drawUI(screen, colorSelection)
    _quixl.drawColorOverlay(screen, colorSelection, pygame.mouse.get_pos())

    if showWatermark:
        _watermark.draw(screen)

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
                x = -1
                y = 0
                i = -1

                img = Image.open("quixl.png")
                pygame.display.set_icon(pygame.image.load('quixl.png'))

                imgw, imgh = img.size
                print(imgw)
                size = imgw
                art = [()] * (size * size)
                pixelDisplaySize = 512/size

                img = img.load()
                for pixel in art:
                    i += 1
                    x += 1
                    if x >= size:
                        x = 0
                        y += 1
                    if (img[x,y] == (0,0,0,0)):
                        art[i] = (-1,-1,-1)
                    else:
                        r,g,b,a = img[x,y]
                        art[i] = (r,g,b)

                print("Image loaded")
                print(art)
            if (event.key == pygame.K_n or event.key == pygame.K_BACKSPACE or event.key == pygame.K_r or event.key == pygame.K_x):
                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("New")
            if (event.key == pygame.K_ESCAPE): running = False

            if (event.key == pygame.K_1):
                size = 4
                art = [()] * (size * size)
                pixelDisplaySize = 512/size

                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("New 4x4")
            if (event.key == pygame.K_2):
                size = 8
                art = [()] * (size * size)
                pixelDisplaySize = 512/size

                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("New 8x8")
            if (event.key == pygame.K_3):
                size = 16
                art = [()] * (size * size)
                pixelDisplaySize = 512/size

                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("New 16x16")
            if (event.key == pygame.K_4):
                size = 32
                art = [()] * (size * size)
                pixelDisplaySize = 512/size

                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("New 32x32")
            if (event.key == pygame.K_5):
                size = 64
                art = [()] * (size * size)
                pixelDisplaySize = 512/size

                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("New 64x64")
            if (event.key == pygame.K_6):
                size = 128
                art = [()] * (size * size)
                pixelDisplaySize = 512/size

                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("New 128x128")

            if (event.key == pygame.K_t): showMiddle = not showMiddle
            if (event.key == pygame.K_g): showGrid = not showGrid
            if (event.key == pygame.K_j):
                print("Jumbling")
                for index in range(size*size):
                    art[index] = (round(random()*255),round(random()*255),round(random()*255))
            if (event.key == pygame.K_w): showWatermark = not showWatermark
            #if (event.key == pygame.K_a): showAlpha = not showAlpha
    if mousedown:
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
