import pygame as pg
import os
from file_link import *

def GUI():
    pg.init()
    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade")
    clock = pg.time.Clock()
    done = False
    
    black = (0,0,0)
    white = (255,255,255)
    background = (30,15,0)

    now_score = font_tvn.render("도움말",True,white)

    esc = font_tvn.render("돌아가기: ESC", True, white)

    while not done :
        clock.tick(24)

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                done = True

            elif(event.type == pg.KEYUP):
                if(event.key == pg.K_ESCAPE):
                    done = True

        screen.blit(help_image,(0,0))
        screen.blit(wall_forest_image,(0,0))

     
        screen.blit(now_score,(40,10))
     
        screen.blit(esc,(480,490))




        pg.display.flip()


