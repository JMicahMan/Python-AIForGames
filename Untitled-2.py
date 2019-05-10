import pygame



def main():
    pygame.init()

    screen = pygame.display.set_mode((400, 400))
    sqr = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(130,130,40,30))
    pygame.display.set_caption("The Game")
    running = True


if __name__=="_main_":
    main()


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()