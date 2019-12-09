import pygame as pg
import Player
from file_link import *

def Level_up(player):
    pg.init()
    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade")
    clock = pg.time.Clock()
    done = False

    white = (255,255,255)
    background = (30,15,0)
    
    text1 = font_tvn.render("1",True,white)
    text2 = font_tvn.render("2",True,white)
    text3 = font_tvn.render("3",True,white)
    text4 = font_tvn.render("4",True,white)

    while not done :
        clock.tick(24)

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                player.add_max_hp(1)
                done = True

            elif(event.type == pg.KEYUP):
                if(event.key == ord('1')):
                    player.add_max_hp(2)
                    done = True
                elif(event.key == ord('2')):
                    player.add_power(0.5)
                    done = True
                elif(event.key == ord('3')):
                    player.add_as(-0.125)
                    done = True
                elif(event.key == ord('4')):
                    player.add_speed(1)
                    done = True

        screen.blit(skill_interface_image,(0,0))
        screen.blit(text1,(100,320))
        screen.blit(text2,(270,320))
        screen.blit(text3,(450,320))
        screen.blit(text4,(620,320))
        
        pg.display.flip()

 
