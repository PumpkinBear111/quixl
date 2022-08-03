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

def drawColorOverlay(screen, colorSelection, mousePos):
    import pygame
    x, y = mousePos
    w,h = pygame.display.get_window_size()
    pygame.draw.circle(screen, (255,255,255), (min(x+30, w-12), min(y+30, 500)), 12)
    pygame.draw.circle(screen, (0,0,0), (min(x+30, w-12), min(y+30, 500)), 11)
    pygame.draw.circle(screen, colorSelection, (min(x+30, w-12), min(y+30, 500)), 10)

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
