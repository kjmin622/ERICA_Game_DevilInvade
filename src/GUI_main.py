import pygame as pg

def main():
    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade") #game title
    clock = pg.time.Clock()
    
    Left = False
    Right = False
    Up = False
    Down = False

    while True :

        clock.tick(24)

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                Down = True

            if(event.type == pg.KEYDOWN):

                if event.key == pg.K_LEFT:
                    Left = True
                if event.key == pg.K_RIGHT:
                    Right = True
                if event.key == pg.K_UP:
                    Up = True
                if event.key == pg.K_DOWN:
                    Down = True

            if(Down): #나가기
                return 0

            if(Left): #게임 시작
               
                return 1

            if(Right) : #기록
                return 2

            if(Up) : #제작자 및 각종 출처 
                return 3

        pg.display.flip()
            
            


