import pygame as pg
pg.init()

size = [720, 580]

screen = pg.display.set_mode(size)

pg.display.set_caption("Devil Invade") #game title

done = False
clock = pg.time.Clock()

white = (255,255,255)

while not done :

    clock.tick(8)

    for event in pg.event.get():
        if event.type == pg.QUIT :
            done = True
    
    screen.fill(white)



    pg.display.flip()


