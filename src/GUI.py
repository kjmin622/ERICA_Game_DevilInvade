import pygame as pg
pg.init()
size = [720, 640]
screen = pg.display.set_mode(size)
pg.display.set_caption("Devil Invade") #game title
done = False
clock = pg.time.Clock()

white = (255,255,255) #기본 색깔
black = (0,0,0)

#image = pg.image.load("../image/enemy/mob1.png").convert_alpha()
# 이미지 예시

#pg.draw.rect(screen, 색깔, [x,y,x크기, y크기], 각도)
# 직사각형 그리기

while not done :

    clock.tick(8)

    for event in pg.event.get():
        if event.type == pg.QUIT :
            done = True
    
    screen.fill(white)

    #인터페이스, 추후에 이미지로 바꾸기
    pg.draw.rect(screen, black, [0,0,720,100], 0)
    pg.draw.rect(screen, black, [0,580,720,60], 0)
    




    pg.display.flip()


