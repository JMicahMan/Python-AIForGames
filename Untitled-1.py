import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))


squr = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(130,130,40,30))




done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

