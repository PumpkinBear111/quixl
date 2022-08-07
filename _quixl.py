import math

print("Do not run '_quixl.py' to start Quixl. Instead run main.py")
lastMousePos = (0,0)

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
def drawUI(screen, currentColor):
    import pygame
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(512, 0, 1, 512))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(512 + 10 - 2, 8, 259, 304))
    for i in range(255):
        pygame.draw.rect(screen, (i, 0, 0), pygame.Rect(512+10+i, 10, 1, 75))
        pygame.draw.rect(screen, (0, i, 0), pygame.Rect(512+10+i, 85, 1, 75))
        pygame.draw.rect(screen, (0, 0, i), pygame.Rect(512+10+i, 160, 1, 75))
        pygame.draw.rect(screen, (i, i, i), pygame.Rect(512+10+i, 235, 1, 75))

    cr, cg, cb = currentColor
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cr, 10, 2, 75))
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cg, 85, 2, 75))
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cb, 160, 2, 75))
    if (cr == cg == cb): pygame.draw.rect(screen, (255,255,0), pygame.Rect(522+cb, 235, 2, 75))

    border = (150,150,150)

    # Color Presets

    # Grayscale Selection
    pygame.draw.rect(screen, border, pygame.Rect(522, 320, 50, 50))
    pygame.draw.rect(screen, (000,000,000), pygame.Rect(524, 322, 46, 46))

    pygame.draw.rect(screen, border, pygame.Rect(582, 320, 50, 50))
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(584, 322, 46, 46))

    pygame.draw.rect(screen, border, pygame.Rect(642, 320, 50, 50))
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(644, 322, 46, 46))

    pygame.draw.rect(screen, border, pygame.Rect(702, 320, 50, 50))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(704, 322, 46, 46))

    # RGB Full
    pygame.draw.rect(screen, border, pygame.Rect(522, 380, 50, 50))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(524, 382, 46, 46))

    pygame.draw.rect(screen, border, pygame.Rect(582, 380, 50, 50))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(584, 382, 46, 46))

    pygame.draw.rect(screen, border, pygame.Rect(642, 380, 50, 50))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(644, 382, 46, 46))

    # RGB Combos
    pygame.draw.rect(screen, border, pygame.Rect(522, 440, 50, 50))
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(524, 442, 46, 46))

    pygame.draw.rect(screen, border, pygame.Rect(582, 440, 50, 50))
    pygame.draw.rect(screen, (0,255,255), pygame.Rect(584, 442, 46, 46))

    pygame.draw.rect(screen, border, pygame.Rect(642, 440, 50, 50))
    pygame.draw.rect(screen, (255,0,255), pygame.Rect(644, 442, 46, 46))

    # Transparent
    #pygame.draw.rect(screen, border, pygame.Rect(702, 380, 50, 110))
    #pygame.draw.rect(screen, (255,255,255), pygame.Rect(704, 382, 46, 106))
    #pygame.draw.line(screen, (255,0,0), (707, 385), (747, 487))
    #pygame.draw.line(screen, (255,0,0), (706, 384), (746, 486))
    #pygame.draw.line(screen, (255,0,0), (705, 383), (745, 485))
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
    screen.blit(rgb, (522,300))
def optimizedScreenClear(screen, mousepos):
    mx, my = mousepos
    import pygame
    global lastMousePos
    lmx, lmy = lastMousePos

    if (abs(lmx-mx) >= 50 or abs(lmy-my) >= 50): pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,screen.get_width(),screen.get_height()))

    pygame.draw.rect(screen, (255,255,255), pygame.Rect(mx-50, my-50, 100, 100))

# Input
def colorPresetSelection(currentColor):
    import pygame
    x, y = pygame.mouse.get_pos()
    if y < 320: return currentColor

    if 320 <= y <= 370:
        if 522 <= x <= 572: return (0,0,0)
        if 582 <= x <= 632: return (100,100,100)
        if 642 <= x <= 692: return (200,200,200)
        if 702 <= x <= 752: return (255,255,255)
    if 380 <= y <= 430:
        if 522 <= x <= 572: return (255,0,0)
        if 582 <= x <= 632: return (0,255,0)
        if 642 <= x <= 692: return (0,0,255)
    if 440 <= y <= 490:
        if 522 <= x <= 572: return (255,255,0)
        if 582 <= x <= 632: return (0,255,255)
        if 642 <= x <= 692: return (255,0,255)

    return currentColor
def colorSliderInput(currentColor):
    import pygame
    x, y = pygame.mouse.get_pos()
    if 522 <= x <= 777:
        cr, cg, cb = currentColor
        if 85 >= y >= 10: currentColor = (x - 522, cg, cb)
        if 160 >= y >= 85: currentColor = (cr, x - 522, cb)
        if 235 >= y >= 160: currentColor = (cr, cg, x - 522)
        if 310 >= y >= 235: currentColor = (x - 522, x - 522, x - 522)
    return currentColor
def leftClickDraw(art, size, colorSelection):
    import pygame
    x, y = pygame.mouse.get_pos()
    if (x <= 511):
        x = math.floor(x / (512 / size))
        y = math.floor(y / (512 / size))
        index = x + size * y
        art[index] = colorSelection
    return art
def rightClickErase(art, size):
    import pygame
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