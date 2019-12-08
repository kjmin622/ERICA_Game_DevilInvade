import pygame as pg
from Player import *
from Floor import *
from file_link import *

def Menu(floor, player, level):
    pg.init()
    
    white = (255,255,255)
    darkGray = (10,10,10)
    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade")
    clock = pg.time.Clock()
    done = False

    Escape = False #메뉴창 나가기
    GameDone = False #게임 종료
   
    attack_value = font_tvn.render(str(round(player.get_power(),2)),True, white)
    attack_speed = font_tvn.render(str(round((1.0/player.get_as()),2)),True,white)
    move_speed = font_tvn.render(str(player.get_speed()),True,white)
    level_ = font_tvn.render(str(level+1),True,darkGray)

    a_v = font_tvn.render("공격력: ", True, white)
    a_s = font_tvn.render("공격속도: ",True,white)
    m_s = font_tvn.render("이동속도: ",True,white)
    lv = font_tvn.render("Level: ", True, darkGray)
    
    #지도 만들기
    init_map = floor.get_map()
    maps = [[],[],[],[],[]]

    now_position = floor.get_where()
    boss_position = floor.get_bossRoom()
    for i in range(5):
        for k in range(6):
            if(now_position == [i,k]):
                now_position = [48+k*104,125+i*78]
            if(boss_position == [i,k]):
                boss_position = [48+k*104,125+i*78]


            if(init_map[i][k]):
                maps[i].append([48+k*104,125+i*78])
            else:
                maps[i].append([0,0])

    

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
        
        pg.draw.rect(screen,(255,200,150),(0,0,720,540))
        pg.draw.rect(screen,(30,15,0),(0,0,720,80))

        screen.blit(a_v,(40,20))
        screen.blit(a_s,(260,20))
        screen.blit(m_s,(480,20))
        screen.blit(attack_value,(140,20))
        screen.blit(attack_speed,(380,20))
        screen.blit(move_speed,(600,20)) 
        for i in range(5):
            for k in range(6):
                if(maps[i][k] != [0,0]):
                    color = (100,100,100)
                    if(now_position == maps[i][k]):
                        color = (0,50,0)
                    elif(boss_position == maps[i][k]):
                        color = (100,0,0)
                    elif(not floor.get_room_position(i,k).create_enemy()):
                        color = (200,100,0)
                    
                    pg.draw.rect(screen,color,(maps[i][k][0]+5,maps[i][k][1]+5,94,68))

        screen.blit(lv,(565,490))
        screen.blit(level_,(665,490))

        pg.display.flip()
