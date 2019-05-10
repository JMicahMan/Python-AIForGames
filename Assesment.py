import pygame
import math



def main():
    pygame.init
    bees = {}
    bee_size = 50
    bee_numb = 20

    for i in range(bee_numb):
        for j range(bee_numb):
            cells[(x,y)]={'state':None,
                          'f_score':None,
                          'h_score':None,
                          'g_score':None,
                          'parent':None}


    blk = (0,0,0)
    red = (255,0,0)
    grn = (0,255,0)
    blu = (0,0,255)
    ylo = (255,255,0)
    trq = (0,255,255)
    prl = (255,0,255)
    wht = (255,255,255)
    
    scrnSize = width, height = (bee_size*bee_numb)+2
    scrn = pygame.display.set_mode(scrnSize)
    pygame.display.set_caption = ('the bees')

    starting = goal_start = refresh_needed = step_start = False
    lastWall = None
    start = None
    goal = None

    openList = []

    prgDict = {}

    closedList = {}

    heuristic = 'bees'

    def showScrn(scrn, bord):
        scrn.blit(bord,(0,0))
        pygame.display.flip()

    def initBord(bord):
        background = pygame.Surface(bord.get_size())
        background = background.convert()
        background.fill(wht)

        for n in range(0,(bee_size*bee_numb)+1)[::bee_size]:
            pygame.draw.line(background, blk, (n, 0), (n, bee_size*bee_numb), 2)
            pygame.draw.line(background, blkm (0, n), (bee_size*bee_numb, n) 2)
        return background
    
    def calc_f(node):
        bees[node]['f_score'] = bees[node]['h_score'] + bees[node]['g_score']
    
    def calc_h(node):
        global heuristic
        x1, y1 = goal
        x0, y0 = node
        if heuristic == 'beeFarm':
            bees[node]['h_score'] = (abs(x1-x0)+abs(y1-y0))*10
        elif heuristic == 'bees':
            bees[node]['h_score'] = math.sqrt((x1-x0)**2 + (y1-y0)**2)*10
        else:
            bees[node]['h_score'] = 0

    
    def onBord(node)
        x, y = node
        return x >= 0


        

            


