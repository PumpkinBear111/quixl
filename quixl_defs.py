import pygame

# Screen Draw
def drawPixelGrid(screen, art, size, pixelDisplaySize):
    x = -1
    y = 0
    for pixel in art:
        x += 1
        if x >= size:
            x = 0
            y += 1
        if (pixel[0] == -1):
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
            pygame.draw.rect(screen, pixel, pygame.Rect(pixelDisplaySize * x, pixelDisplaySize * y, pixelDisplaySize,
                                                        pixelDisplaySize))
def drawUI(screen):
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(512, 0, 1, 512))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(512 + 10 - 2, 8, 259, 304))
    for i in range(255):
        pygame.draw.rect(screen, (i, 0, 0), pygame.Rect(512+10+i, 10, 1, 75))
        pygame.draw.rect(screen, (0, i, 0), pygame.Rect(512+10+i, 85, 1, 75))
        pygame.draw.rect(screen, (0, 0, i), pygame.Rect(512+10+i, 160, 1, 75))
        pygame.draw.rect(screen, (i, i, i), pygame.Rect(512+10+i, 235, 1, 75))

# Input