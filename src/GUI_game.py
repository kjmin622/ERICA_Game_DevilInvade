import pygame as pg
import Player
import Bullet
import Enemy
import Map
import Skill
import Crash
from enemy import Mob1
from enemy import Mob2
from enemy import Mob3



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


    #key 명령
    #move
    MoveLeft = False
    MoveRight = False
    MoveUp = False
    MoveDown = False
    Skill_1 = [False,False,False,False]

    player = Player.Player(300,300,10,10)  #플레이어 객체 생성
    skill = Skill.Skill() #스킬 객체 생성  
    b_list = [] # 총알 객체 생성 
    e_list = [] # 적 객체 생성
     
    #image
    bullet_image = pg.image.load("../image/enemy/BULLET.png")
    ground_image = pg.image.load("../image/background/ground.png")
    wall_forest_image =pg.image.load("../image/background/wall_forest.png")
    ldoor_image = pg.image.load("../image/background/door_left.png")
    rdoor_image = pg.image.load("../image/background/door_right.png")
    udoor_image = pg.image.load("../image/background/door_up.png")
    ddoor_image = pg.image.load("../image/background/door_down.png")
    mob1_image = pg.image.load("../image/enemy/mob_01.png")
    mob2_image = pg.image.load("../image/enemy/mob_02.png")
    skill1_1_0_image = pg.image.load("../image/skill/skill1_1_0.png")
    skill1_1_1_image = pg.image.load("../image/skill/skill1_1_1.png")
    skill1_1_2_image = pg.image.load("../image/skill/skill1_1_2.png")
    skill1_1_3_image = pg.image.load("../image/skill/skill1_1_3.png")
    skill1_2_image = pg.image.load("../image/skill/skill1_2.png")
    player0_image = pg.image.load("../image/player/player.png")
    
    #skill global
    sub_d = 0
    skill1_time = 0
    skill1_a = [0,0]
    skill1_e = []

    #sound
    pg.mixer.init()
    back_music = pg.mixer.Sound('../sound/main.wav')
    back_music.play(-1)

    #font
    font_tvn = pg.font.Font("../font/tvn.ttf", 50)

    
    #map test
    room = Map.Room([True,False,True,False])
    e_list = room.get_e_list()

    while not done :

        clock.tick(24)
        for event in pg.event.get():
            if event.type == pg.QUIT : #종료
                done = True
                return True
            
            if event.type == pg.KEYDOWN :# 키 눌렀을 때 
                if event.key == ord('a'):
                    Skill_1[2] = True
                elif event.key == ord('w'):
                    Skill_1[0] = True
                elif event.key == ord('s'):
                    Skill_1[1] = True
                elif event.key == ord('d'):
                    Skill_1[3] = True
                if event.key == pg.K_LEFT:
                  MoveLeft = True
                if event.key == pg.K_RIGHT:
                    MoveRight = True
                if event.key == pg.K_UP:
                    MoveUp = True
                if event.key == pg.K_DOWN:
                    MoveDown = True

            if event.type == pg.KEYUP : #//
                if event.key == ord('a'):
                    Skill_1[2] = False
                if event.key == ord('w'):
                    Skill_1[0] = False
                if event.key == ord('s'):
                    Skill_1[1] = False
                if event.key == ord('d'):
                    Skill_1[3] = False
                if event.key == pg.K_LEFT:
                    MoveLeft = False
                if event.key == pg.K_RIGHT:
                    MoveRight = False
                if event.key == pg.K_UP:
                    MoveUp = False
                if event.key == pg.K_DOWN:
                    MoveDown = False
    
        screen.blit(ground_image,(0,0)) #땅
        screen.blit(wall_forest_image,(0,0)) #벽
        
        if(not e_list):
            if(room.get_door()[0]==True):
                screen.blit(udoor_image,(0,0))
            if(room.get_door()[1]==True):
                screen.blit(ddoor_image,(0,0))
            if(room.get_door()[2]==True):
                screen.blit(ldoor_image,(0,0))
            if(room.get_door()[3]==True):
                screen.blit(rdoor_image,(0,0))

        #HP
        text_hp = font_tvn.render("HP:",True,white)
        text_slash = font_tvn.render("/",True,white)
        text_hp_now = font_tvn.render(str(player.get_hp()),True,white)
        text_max_hp = font_tvn.render(str(player.get_max_hp()),True,white)
        screen.blit(text_hp,(40,8))
        screen.blit(text_slash,(130,8))
        screen.blit(text_hp_now, (100,8))
        screen.blit(text_max_hp, (155,8))
    
        #적########################################################
        for enemy in e_list :
            #특수효과들
            enemy.moving(player)
            enemy.shot(player,b_list)
            enemy.create(e_list, b_list, player)
            #######################################
            Crash.E_bump_list(enemy,e_list)
            enemy.body_hit(player)
            screen.blit(pg.image.load(enemy.get_image()),(enemy.get_x(), enemy.get_y()))
            if(enemy.death()):
                e_list.remove(enemy)
                del(enemy)

        #플레이어###################################################
         #스킬
         #스킬 1
        skill.cool_1()
        if((Skill_1[0] or Skill_1[1]) and skill.get_cooltime()[0]==0):
            sub_d = (Skill_1[1] and 1 or 0)
            player.set_direction(sub_d)
            skill1_a = skill.position(player,200)
            for enemy in e_list :
                if(skill.skill_1(player,enemy)):
                    skill1_e.append([enemy.get_x()+enemy.get_width()-15, enemy.get_y()+enemy.get_height()-55])
            skill.make_cool_1(player)
            skill1_time = 3

        if((Skill_1[2] or Skill_1[3]) and skill.get_cooltime()[0]==0):
            sub_d = (Skill_1[2] and 2 or 3)
            player.set_direction(sub_d)
            skill1_a = skill.position(player,200)
            for enemy in e_list :
                if(skill.skill_1(player,enemy)):
                    skill1_e.append([enemy.get_x()+enemy.get_width()-15, enemy.get_y()+enemy.get_height()-55])
            skill.make_cool_1(player)
            skill1_time = 3

        if(skill1_time != 0):
            if(sub_d<=1):
                screen.blit(sub_d==1 and skill1_1_1_image or skill1_1_0_image,(skill1_a[0],skill1_a[1]))
            else:
                screen.blit(sub_d==2 and skill1_1_2_image or skill1_1_3_image,(skill1_a[0],skill1_a[1]))
            for e in skill1_e:
                screen.blit(skill1_2_image, (e[0], e[1]))
            skill1_time -= 1
        else:
            del skill1_e[:]
        
        #이동
        if(MoveLeft):
            player.set_direction(2)
            player.move(45,45)
        if(MoveRight):
            player.set_direction(3)
            player.move(45,45)
        if(MoveUp):
            player.set_direction(0)
            player.move(45,45)
        if(MoveDown):
            player.set_direction(1)
            player.move(45,45)
       
       #문에 닿았니?
        touchdoor = room.enter_door(player, e_list)
        if(touchdoor!=-1):
            print(touchdoor)
       
        #무적 해제중
        player.inv_minus()
        
        #죽음
        if(player.death()):
            return 0 #죽었을 때 어떻게 할지 구현해야 함
        
        screen.blit(player0_image,(player.get_x(), player.get_y()-20))

        ########################################################
        
        #총알 list##############################################
        for bullet in b_list :
            if(bullet.hit_del(player)):
                b_list.remove(bullet)
                del(bullet)
            else:
                screen.blit(bullet_image,(bullet.get_x()-3,bullet.get_y()-3))
        
       
        pg.display.flip()
