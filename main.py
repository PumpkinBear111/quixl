import pygame

size = 8
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("quixl")

pixelDisplaySize = screen.get_width()/size

running = True

art = [(0,0,0)]*(size*size)

print(art)

i = -1
for color in art:
    i += 1
    art[i] = (-1,-1,-1)

print(art)

while running:
    x = -1
    y = 0
    for pixel in art:
        x += 1
        if x >= size:
            x = 0
            y += 1
        if (pixel[0] == -1):
            pygame.draw.rect(screen, (240,240,240), pygame.Rect(pixelDisplaySize*x, pixelDisplaySize*y, pixelDisplaySize, pixelDisplaySize))
            if (x%2 == 0 and y%2 == 0):
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(pixelDisplaySize*x, pixelDisplaySize*y, pixelDisplaySize, pixelDisplaySize))
            if ((x+1)%2 == 0 and (y+1)%2 == 0):
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(pixelDisplaySize*x, pixelDisplaySize*y, pixelDisplaySize, pixelDisplaySize))
        else:
            pygame.draw.rect(screen, pixel, pygame.Rect(pixelDisplaySize*x, pixelDisplaySize*y, pixelDisplaySize, pixelDisplaySize))

    pygame.display.flip()

    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False