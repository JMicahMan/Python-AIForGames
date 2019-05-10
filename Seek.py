import pygame
import math
from random import randint
from random import uniform


width = 1000
height = 1000
fps = 60
color = (255, 0, 0)

sqrSize = 32
sqrSpeed = 5


class sqr(pygame.sprite.Sprite):
    def __init__(self):
        self.group = all_sprites
        pygame.sprite.Sprite.__init__(self, self.group)
        self.image = pygame,Surface((sqrSize, sqrSize))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0, width), randint(0, height))
        self.acc = vec(0, 0)
        self.rect.center = self.pos

    def followMouse(self):
        mpos = pygame.mouse.get_pos()
        self.acc = (mpos - self.pos).normalize