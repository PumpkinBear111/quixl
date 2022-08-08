# Quixl uses the GNU General Public License v3.0, also known as GNU GPLv3. Check '/COPYING' for more information

lastMousePos = (0,0)
data = {}

# Init and Exit
def createData(screen):
    import os
    import pygame
    global data
    drawUI(screen, (0,0,0), False)
    data["displaybg"] = screen

def onClose():
    #import os
    #os.rmdir("tmp_quixl_running")
    pass

# Screen Draw
def drawPixelGrid(screen, art, size, pixelDisplaySize, showMiddle, showGrid, showAlpha):
    import pygame
    x = -1
    y = 0
    for pixel in art:
        x += 1
        if x >= size:
            x = 0
            y += 1
        if showGrid: pygame.draw.rect(screen, (125,125,125), pygame.Rect(pixelDisplaySize*x-1, pixelDisplaySize*y-1, pixelDisplaySize+2, pixelDisplaySize+2))
        if pixel[0] == -1 and showAlpha:
            pygame.draw.rect(screen, (240, 240, 240),
                             pygame.Rect(pixelDisplaySize * x, pixelDisplaySize * y, pixelDisplaySize,
                                         pixelDisplaySize))
            if (x % 2 == 0 and y % 2 == 0):
                pygame.draw.rect(screen, (250, 250, 250),
                                 pygame.Rect(pixelDisplaySize * x, pixelDisplaySize * y, pixelDisplaySize,
                                             pixelDisplaySize))
            if ((x + 1) % 2 == 0 and (y + 1) % 2 == 0):
                pygame.draw.rect(screen, (250, 250, 250),
                                 pygame.Rect(pixelDisplaySize * x, pixelDisplaySize * y, pixelDisplaySize,
                                             pixelDisplaySize))
        else:
            if not showAlpha: pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,512,512))
            pygame.draw.rect(screen, pixel, pygame.Rect(pixelDisplaySize * x, pixelDisplaySize * y, pixelDisplaySize,
                                                        pixelDisplaySize))
    if showMiddle:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(256, 0, 2, 512))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 256, 512, 2))
def drawUI(screen, currentColor, live):
    import pygame

    if live:
        pygame.draw.rect(screen, (200,200,200), pygame.Rect(512, 0, 1, 512))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(512 + 10 - 2, 8, 259, 184))
        for i in range(255):
            pygame.draw.rect(screen, (i, 0, 0), pygame.Rect(512+10+i, 10, 1, 45))
            pygame.draw.rect(screen, (0, i, 0), pygame.Rect(512+10+i, 55, 1, 45))
            pygame.draw.rect(screen, (0, 0, i), pygame.Rect(512+10+i, 100, 1, 45))
            pygame.draw.rect(screen, (i, i, i), pygame.Rect(512+10+i, 145, 1, 45))

    if not live:
        cr, cg, cb = currentColor
        pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cr, 10, 2, 45))
        pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cg, 55, 2, 45))
        pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cb, 100, 2, 45))
        if (cr == cg == cb): pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cb, 145, 2, 45))

    border = (150,150,150)
    height = 200

    # Color Presets

    if not live: return
    # Grayscale Selection
    pygame.draw.rect(screen, border, pygame.Rect(522, height, 50, 30))
    pygame.draw.rect(screen, (000,000,000), pygame.Rect(524, height+2, 46, 26))

    pygame.draw.rect(screen, border, pygame.Rect(582, height, 50, 30))
    pygame.draw.rect(screen, (85,85,85), pygame.Rect(584, height+2, 46, 26))

    pygame.draw.rect(screen, border, pygame.Rect(642, height, 50, 30))
    pygame.draw.rect(screen, (170,170,170), pygame.Rect(644, height+2, 46, 26))

    pygame.draw.rect(screen, border, pygame.Rect(702, height, 50, 30))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(704, height+2, 46, 26))

    # RGB Full
    pygame.draw.rect(screen, border, pygame.Rect(522, height+40, 50, 30))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(524, height+42, 46, 26))

    pygame.draw.rect(screen, border, pygame.Rect(582, height+40, 50, 30))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(584, height+42, 46, 26))

    pygame.draw.rect(screen, border, pygame.Rect(642, height+40, 50, 30))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(644, height+42, 46, 26))

    # RGB Combos
    pygame.draw.rect(screen, border, pygame.Rect(522, height+80, 50, 30))
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(524, height+82, 46, 26))

    pygame.draw.rect(screen, border, pygame.Rect(582, height+80, 50, 30))
    pygame.draw.rect(screen, (0,255,255), pygame.Rect(584, height+82, 46, 26))

    pygame.draw.rect(screen, border, pygame.Rect(642, height+80, 50, 30))
    pygame.draw.rect(screen, (255,0,255), pygame.Rect(644, height+82, 46, 26))

    # Lighten/Darken
    #arrowColor = (255,255,255)
    #if cr+cg+cb >= 382.5: arrowColor = (0,0,0)

    #pygame.draw.rect(screen, border, pygame.Rect(702, height+40, 50, 30))
    #pygame.draw.rect(screen, (min(cr+10,255),min(cg+10,255),min(cb+10,255)), pygame.Rect(704, height+42, 46, 26))
    #pygame.draw.line(screen, arrowColor, (727, height+45), (727, height+65))
    #pygame.draw.line(screen, arrowColor, (727, height+45), (732, height+50))
    #pygame.draw.line(screen, arrowColor, (727, height+45), (722, height+50))

    #pygame.draw.rect(screen, border, pygame.Rect(702, height+80, 50, 30))
    #pygame.draw.rect(screen, (max(cr-10,0),max(cg-10,0),max(cb-10,0)), pygame.Rect(704, height+82, 46, 26))
    #pygame.draw.line(screen, arrowColor, (727, height+85), (727, height+105))
    #pygame.draw.line(screen, arrowColor, (727, height+105), (732, height+100))
    #pygame.draw.line(screen, arrowColor, (727, height+105), (722, height+100))

    # Non-Color UI
    pygame.draw.rect(screen, (150,150,150), pygame.Rect(522, 335, 255, 150))
def drawColorOverlay(screen, colorSelection, mousePos):
    if colorSelection == (-1,-1,-1): return
    import pygame
    x, y = mousePos
    w,h = pygame.display.get_window_size()

    pygame.draw.circle(screen, (0,0,0), (x+1, y+1), 1)

    pygame.draw.circle(screen, (255,255,255), (min(x+30, w-12), min(y+30, 500)), 12)
    pygame.draw.circle(screen, (0,0,0), (min(x+30, w-12), min(y+30, 500)), 11)
    pygame.draw.circle(screen, colorSelection, (min(x+30, w-12), min(y+30, 500)), 10)
def drawComplex(screen, font, colorSelection):
    r,g,b = colorSelection
    rgb = font.render(f"rgb({r},{g},{b})", True, (160,160,160))
    screen.blit(rgb, (522,180))
def optimizedScreenClear(screen, mousepos):
    mx, my = mousepos
    import pygame
    global lastMousePos

    lmx, lmy = lastMousePos
    if (abs(lmx-mx) >= 30 or abs(lmy-my) >= 30): pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,screen.get_width(),screen.get_height()))
    lastMousePos = mousepos

    if mx < 450: return

    pygame.draw.rect(screen, (255,255,255), pygame.Rect(lmx-50, lmy-50, 100, 100))

# Input
def colorPresetSelection(currentColor):
    import pygame
    x, y = pygame.mouse.get_pos()
    if y < 200: return currentColor

    if 200 <= y <= 230:
        if 522 <= x <= 572: return (0,0,0)
        if 582 <= x <= 632: return (85,85,85)
        if 642 <= x <= 692: return (170,170,170)
        if 702 <= x <= 752: return (255,255,255)
    if 240 <= y <= 270:
        if 522 <= x <= 572: return (255,0,0)
        if 582 <= x <= 632: return (0,255,0)
        if 642 <= x <= 692: return (0,0,255)
    if 280 <= y <= 310:
        if 522 <= x <= 572: return (255,255,0)
        if 582 <= x <= 632: return (0,255,255)
        if 642 <= x <= 692: return (255,0,255)

    return currentColor
def colorSliderInput(currentColor):
    import pygame
    x, y = pygame.mouse.get_pos()
    if 522 <= x <= 777:
        cr, cg, cb = currentColor
        if 55 >= y >= 10: currentColor = (x - 522, cg, cb)
        if 100 >= y >= 55: currentColor = (cr, x - 522, cb)
        if 145 >= y >= 100: currentColor = (cr, cg, x - 522)
        if 190 >= y >= 145: currentColor = (x - 522, x - 522, x - 522)
    return currentColor
def leftClickDraw(art, size, colorSelection):
    import pygame, math
    x, y = pygame.mouse.get_pos()
    if (x <= 511):
        x = math.floor(x / (512 / size))
        y = math.floor(y / (512 / size))
        index = x + size * y
        art[index] = colorSelection
    return art
def rightClickErase(art, size):
    import pygame, math
    x, y = pygame.mouse.get_pos()
    if (x <= 511):
        x = math.floor(x / (512 / size))
        y = math.floor(y / (512 / size))
        index = x + size * y
        art[index] = (-1, -1, -1)
    return art

# Image Files
def saveImage(art, size):
    from PIL import Image
    import pygame

    x = -1
    y = 0
    img = Image.new('RGBA', (size, size))
    for pixel in art:
        x += 1
        if x >= size:
            x = 0
            y += 1
        if (pixel[0] == -1):
            img.putpixel((x, y), (0, 0, 0, 0))
        else:
            img.putpixel((x, y), pixel)
    img.save('quixl.png')
    print("Image saved")

    pygame.display.set_icon(pygame.image.load('quixl.png'))
def openImage():
    import pygame
    from PIL import Image

    x = -1
    y = 0
    i = -1

    img = Image.open("quixl.png")
    pygame.display.set_icon(pygame.image.load('quixl.png'))

    imgw, imgh = img.size
    print(imgw)
    size = imgw
    art = [()] * (size * size)
    pixelDisplaySize = 512 / size

    img = img.load()
    for pixel in art:
        i += 1
        x += 1
        if x >= size:
            x = 0
            y += 1
        if (img[x, y] == (0, 0, 0, 0)):
            art[i] = (-1, -1, -1)
        else:
            r, g, b, a = img[x, y]
            art[i] = (r, g, b)

    return (art, size, pixelDisplaySize)