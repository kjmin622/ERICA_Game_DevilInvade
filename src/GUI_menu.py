import pygame as pg
from file_link import *

def Menu():
    pg.init()
    
    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade")
    clock = pg.time.Clock()
    done = False

    Escape = False #메뉴창 나가기
    GameDone = False #게임 종료
    
    while not done :
        clock.tick(24)

        for event in pg.event.get():
            if(event.type == pg.QUIT) :
                done = True
                return 2

            if(event.type == pg.KEYUP):
                if(event.key == pg.K_ESCAPE):
                    return 1
                if(event.key == ord('p')):
                    return 2
        
        pg.draw.rect(screen,(255,255,255),(0,0,720,540))
        pg.display.flip()
