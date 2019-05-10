import math
import pygame

pygame.init()

#   A Bee that uses a* algorithim to move towards a flower
# without going through the black blobs

#Bee

bees = {}
beeSize = 200

#colors

blk = (0,0,0) 
wht = (255,255,255)
red = (255,0,0)
grn = (0,255,0)
blu = (0,0,255)
ylw = ()
cyn =
prp =

 
def main():   


    screen = pygame.display.set_mode((1000,1000))
    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




main()