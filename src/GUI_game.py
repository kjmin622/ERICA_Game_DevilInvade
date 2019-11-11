import pygame as pg
import Player
import Bullet
import Enemy



def play_game() :

    
    pg.init()

    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade") #game title
    clock = pg.time.Clock()
    done = False
    white = (255,255,255) #기본 색깔
    black = (0,0,0)
    wall = (100,100,100)


    #이동 명령
    MoveLeft = False
    MoveRight = False
    MoveUp = False
    MoveDown = False

    player = Player.Player(300,300,10,10)  #플레이어 객체 생성 
    b_list = [] # 총알 객체 생성 
    e_list = [] # 적 객체 생성

    e_list.append(Enemy.Enemy(150,150,1,0,10,1,40,40))

    
    #image
    bullet_image = pg.image.load("../image/enemy/BULLET.png")
    mob1_image = pg.image.load("../image/enemy/mob_01.png")
    mob2_image = pg.image.load("../image/enemy/mob_02.png")

    #sound
    pg.mixer.init()
    back_music = pg.mixer.Sound('../sound/main.wav')
    back_music.play(-1)

    #font
    font_tvn = pg.font.Font("../font/tvn.ttf", 50)


    while not done :

        clock.tick(24)
        for event in pg.event.get():
            if event.type == pg.QUIT : #종료
                done = True
                return True
            
            if event.type == pg.KEYDOWN :# 키 눌렀을 때 
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

        #wall, later, image
        pg.draw.rect(screen,wall,[0,0,720,70],0)
        pg.draw.rect(screen,wall,[0,0,70,540],0)
        pg.draw.rect(screen,wall,[0,470,720,70],0)
        pg.draw.rect(screen,wall,[650,0,70,540],0)

        #door, later, image
        pg.draw.rect(screen,black,[320,10,80,60],0)
        pg.draw.rect(screen,black,[10,230,60,80],0)
        pg.draw.rect(screen,black,[650,230,60,80],0)
        pg.draw.rect(screen,black,[320,470,80,60],0)

        #HP
        text_hp = font_tvn.render("HP:",True,white)
        text_slash = font_tvn.render("/",True,white)
        text_hp_now = font_tvn.render(str(player.get_hp()),True,white)
        text_max_hp = font_tvn.render(str(player.get_max_hp()),True,white)
        screen.blit(text_hp,(40,8))
        screen.blit(text_slash,(130,8))
        screen.blit(text_hp_now, (100,8))
        screen.blit(text_max_hp, (155,8))
    

        #플레이어
        #플레이어 이동
        if(MoveLeft):
            player.set_direction(2)
            player.move(45,65)
        if(MoveRight):
            player.set_direction(3)
            player.move(45,65)
        if(MoveUp):
            player.set_direction(0)
            player.move(45,65)
        if(MoveDown):
            player.set_direction(1)
            player.move(45,65)

        #무적 해제중
        player.inv_minus()

        #총알 list
        for bullet in b_list :
            bullet.move(-30,-30)
            if(bullet.hit_del(player)):
                b_list.remove(bullet)
                del(bullet)
            else:
                screen.blit(bullet_image,(bullet.get_x(),bullet.get_y()))
            
    #적 list
        for enemy in e_list :
            enemy.move(enemy.get_width(), enemy.get_height())
            enemy.body_hit(player)
            screen.blit(mob2_image,(enemy.get_x(), enemy.get_y()))
        
            #pg.draw.rect(screen,black,[enemy.get_x(), enemy.get_y(), enemy.get_width(), enemy.get_height()],0)
            

        if(player.death()):
            return 0 #죽었을 때 어떻게 할지 구현해야 함 
        pg.draw.rect(screen, black, [player.get_x(), player.get_y(), 45,65],0)

        pg.display.flip()
