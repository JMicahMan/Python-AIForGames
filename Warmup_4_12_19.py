import pygame


def sqrinasqr():
    screen = pygame.display.set_mode((400, 400))
    sqr = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(130,130,40,30))
    othrsqr = pygame.surface.rect(1 , (0, 255, 0), pygame.Surface.Rect(130, 130,40))
    if (sqr[2] == othrsqr[2]):
        print ("Is in Sqr")
    else:
        print ("not in Sqr")

