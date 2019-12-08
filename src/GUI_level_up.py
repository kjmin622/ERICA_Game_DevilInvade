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

    while not done :
        clock.tick(24)

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                player.add_max_hp(1)
                done = True

            elif(event.type == pg.KEYUP):
                if(event.key == ord('1')):
                    player.add_max_hp(1)
                    done = True
                elif(event.key == ord('2')):
                    player.add_power(0.5)
                    done = True
                elif(event.key == ord('3')):
                    player.add_as(-0.09375)
                    done = True
                elif(event.key == ord('4')):
                    player.add_speed(1)
                    done = True


 
