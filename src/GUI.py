import pygame as pg
import Player


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

player = Player.Player(300,300,10,10)

MoveLeft = False
MoveRight = False
MoveUp = False
MoveDown = False
while not done :

    clock.tick(12)

    for event in pg.event.get():
        if event.type == pg.QUIT : #종료
            done = True

        if event.type == pg.KEYDOWN : #키 눌렀을 때 
            if event.key == pg.K_LEFT:
                MoveLeft = True
            if event.key == pg.K_RIGHT:
                MoveRight = True
            if event.key == pg.K_UP:
                MoveUp = True
            if event.key == pg.K_DOWN:
                MoveDown = True

        if event.type == pg.KEYUP : #//
            if event.key == pg.K_LEFT:
                MoveLeft = False
            if event.key == pg.K_RIGHT:
                MoveRight = False
            if event.key == pg.K_UP:
                MoveUp = False
            if event.key == pg.K_DOWN:
                MoveDown = False
    
    screen.fill(white)

    #인터페이스, 추후에 이미지로 바꾸기
    pg.draw.rect(screen, black, [0,0,720,100], 0)
    pg.draw.rect(screen, black, [0,580,720,60], 0)
    
    
    if(MoveLeft):
        player.set_direction(2)
        player.move()

    if(MoveRight):
        player.set_direction(3)
        player.move()
    
    if(MoveUp):
        player.set_direction(0)
        player.move()

    if(MoveDown):
        player.set_direction(1)
        player.move()
        

    pg.draw.rect(screen, black, [player.get_x(), player.get_y(), 30,60],0)

    pg.display.flip()


