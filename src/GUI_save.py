import pygame as pg
import os
from file_link import *

def GUI(now = 0):
    pg.init()
    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade")
    clock = pg.time.Clock()
    done = False
    
    black = (0,0,0)
    white = (255,255,255)
    background = (30,15,0)

    number = []
    for i in range(1,10):
        number.append(font_tvn.render(str(i)+":",True,white))

    scored = load()
    score = []
    for i in scored :
        score.append(font_tvn.render(str(i), True,white))

    now_score = font_tvn.render("이번 점수:"+str(now),True,white)

    esc = font_tvn.render("돌아가기: ESC", True, white)

    while not done :
        clock.tick(24)

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                done = True

            elif(event.type == pg.KEYUP):
                if(event.key == pg.K_ESCAPE):
                    done = True

        screen.blit(ground_image,(0,0))
        screen.blit(wall_forest_image,(0,0))

        for i in range(1,10,2):
            screen.blit(number[i-1],(100,75+(i-1)*43))

        for i in range(2,10,2):
            screen.blit(number[i-1],(360,75+(i-1)*43))
        
        k = 1
        for i in score :
            if(k%2 == 1) :
                screen.blit(i,(150,75+(k-1)*43))
            else :
                screen.blit(i,(410,75+(k-1)*43))
            k += 1

        if(now > 0):
            screen.blit(now_score,(40,10))

        screen.blit(esc,(480,490))




        pg.display.flip()


def save(score):
    f = open("save","a",encoding='utf-8');
    f.write(str(score)+"\n")
    f.close()

def load():
    if(not os.path.isfile("save")):
        f = open("save","w")
        f.close()

    f = open("save","r",encoding='utf-8');
    stri = f.read()
    arr = stri.split("\n")
    arr = arr[0:-1]
    
    numarr = []
    for i in arr :
        numarr.append(int(i))

    numarr.sort(reverse = True)

    answer = []
    count = 10
    for i in numarr :
        count -= 1
        if(count == 0) : break
        answer.append(i)

    f.close()
    f = open("save","w")
    for i in answer :
        f.write(str(i)+"\n")
    f.close()
    return answer
