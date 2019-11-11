import pygame as pg

def main():
    pg.init()

    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade") #game title
    clock = pg.time.Clock()
    
    Left = False
    Right = False
    Up = False
    Down = False

    #image
    image1 = pg.image.load("../image/background/main_bg1.png")
    image2 = pg.image.load("../image/background/main_bg2.png")
    image3 = pg.image.load("../image/background/main_bg3.png")

    #font
    font_tvn = pg.font.Font("../font/tvn.ttf",110)

    #start animation
    t=15
    while t!=0 :
        clock.tick(24)
        t -= 1
        screen.blit(image1,(0,0))
        pg.display.flip()
    t=3
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()
    t=10
    while t!=0 :
        clock.tick(24)
        t-=1
        screen.blit(image1,(0,0))
        pg.display.flip()
    t=3
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()
    t=6
    while t!=0 :
        clock.tick(24)
        t-=1
        screen.blit(image1,(0,0))
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()
    t=3
    while t!=0 :
        clock.tick(24)
        t-=1
        screen.blit(image1,(0,0))
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        screen.blit(image1,(0,0))
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        screen.blit(image1,(0,0))
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        screen.blit(image1,(0,0))
        pg.display.flip()
    t=2
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()
    t=4
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        screen.blit(image3,(0,0))
        pg.display.flip()
    t=8
    while t!=0 :
        clock.tick(24)
        t-=1
        pg.draw.rect(screen,(0,0,0),[0,0,720,540],0)
        pg.display.flip()



    while True :
        
        clock.tick(24)
        screen.blit(image2,(0,0))
        text_title = font_tvn.render("Devil Invade",True, (100,0,0))
        screen.blit(text_title,(160,60))
       

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
            
            


