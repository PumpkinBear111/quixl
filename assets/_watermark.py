# Quixl uses the GNU General Public License v3.0, also known as GNU GPLv3. Check '[Install Directory]/COPYING' for more information

watermark_black = None
watermark_white = None

def init():
    import pygame, json
    global watermark_black, watermark_white

    configFile = open("config.json")
    config = json.load(configFile)
    configFile.close()

    watermark_font = pygame.font.SysFont("Roboto-Regular.ttf", config["watermark"]["font-size"])
    watermark_black = watermark_font.render(config["watermark"]["text"], True, (0, 0, 0))
    watermark_black.set_alpha(50)
    watermark_white = watermark_font.render(config["watermark"]["text"], True, (255, 255, 255))
    watermark_white.set_alpha(50)

def draw(screen):
    screen.blit(watermark_black, (0, 000))
    screen.blit(watermark_white, (0, 100))
    screen.blit(watermark_black, (0, 200))
    screen.blit(watermark_white, (0, 300))
    screen.blit(watermark_black, (0, 400))