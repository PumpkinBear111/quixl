import math
import pygame
from PIL import Image

import quixl_defs

size = 8
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

while running:
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,screen.get_width(),screen.get_height()))

    quixl_defs.drawPixelGrid(screen, art, size, pixelDisplaySize)
    quixl_defs.drawUI(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: mousedown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: mousedown = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: rightmousedown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3: rightmousedown = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_s):
                x = -1
                y = 0
                img = Image.new('RGBA', (size, size))
                for pixel in art:
                    x += 1
                    if x >= size:
                        x = 0
                        y += 1
                    if (pixel[0] == -1):
                        img.putpixel((x, y), (0,0,0,0))
                    else:
                        img.putpixel((x, y), pixel)
                img.save('quixl.png')
                print("Image saved")
            if (event.key == pygame.K_o):
                x = -1
                y = 0
                i = -1

                img = Image.open("E:\Small Intellij Projects\quixl\quixl.png")

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
                        art[i] = img[x,y]
                print("Image loaded")
            if (event.key == pygame.K_n):
                i = -1
                for color in art:
                    i += 1
                    art[i] = (-1, -1, -1)
                print("Cleared")
    if mousedown:
        x, y = pygame.mouse.get_pos()
        if (x <= 511):
            x = math.floor(x / (512 / size))
            y = math.floor(y / (512 / size))
            index = x + size * y
            art[index] = (0,0,0)
    if rightmousedown:
        x, y = pygame.mouse.get_pos()
        if (x <= 511):
            x = math.floor(x / (512 / size))
            y = math.floor(y / (512 / size))
            index = x + size * y
            art[index] = (-1,-1,-1)
