import pygame as pg
import Player
import Bullet
import Enemy
import Map
import MapList
import Skill
import Crash
import Floor
import random
import Heart
from enemy import Mob1
from enemy import Mob2
from enemy import Mob3

from file_link import *
#######################################
## image name
### bullet_image
### ground_image
### wall_forest_image
### ldoor_image
### rdoor_image
### udoor_image
### ddoor_image
### mob1_image
### mob2_image
### skill1_1_0_image
### skill1_1_1_image
### skill1_1_2_image
### skill1_1_3_image
### skill1_2_image
### player0_image
########################################
## font name
### font_tvn
########################################
## sound name
### back_music
########################################



def play_game() :

    pg.init()
    pg.mixer.init()

    size = [720,540]
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Devil Invade") #game title
    clock = pg.time.Clock()
    done = False

    white = (255,255,255)


    #key 명령
    #move
    MoveLeft = False
    MoveRight = False
    MoveUp = False
    MoveDown = False
    Skill_1 = [False,False,False,False]

    player = Player.Player(300,300,10,10)  #플레이어 객체 생성
    skill = Skill.Skill() #스킬 객체 생성

    b_list = [] # 총알 객체 리스트 
    e_list = [] # 적 객체 리스트
    h_list = [] # 추가생명 리스트
    
    #skill1
    sub_d = 0
    skill1_time = 0
    skill1_a = [0,0]
    skill1_e = []

    #main sound play
    back_music.play(-1)

    #map
    Floor_move = False  # True이면 Floor 새로 받아오기
    Floor_now = Floor.Floor()
    Room_now = Floor_now.get_room()
    Floor_level = 800
    boss_room = False
    ##########################################################
    ## 플레이 시작
    ##########################################################
    while not done :

        clock.tick(24)

        ##########################################################
        ## 키 입력 이벤트
        ##########################################################
        for event in pg.event.get():
            if event.type == pg.QUIT : #종료
                done = True
                return True
            
            if event.type == pg.KEYDOWN :# 키 눌렀을 때
                #skill 1###############################
                if event.key == ord('a'):
                    Skill_1[2] = True
                elif event.key == ord('w'):
                    Skill_1[0] = True
                elif event.key == ord('s'):
                    Skill_1[1] = True
                elif event.key == ord('d'):
                    Skill_1[3] = True

                #move #################################
                if event.key == pg.K_LEFT:
                  MoveLeft = True
                if event.key == pg.K_RIGHT:
                    MoveRight = True
                if event.key == pg.K_UP:
                    MoveUp = True
                if event.key == pg.K_DOWN:
                    MoveDown = True

            if event.type == pg.KEYUP : #키에서 땠을 때
                #skill 1###############################
                if event.key == ord('a'):
                    Skill_1[2] = False
                if event.key == ord('w'):
                    Skill_1[0] = False
                if event.key == ord('s'):
                    Skill_1[1] = False
                if event.key == ord('d'):
                    Skill_1[3] = False

                #move #################################
                if event.key == pg.K_LEFT:
                    MoveLeft = False
                if event.key == pg.K_RIGHT:
                    MoveRight = False
                if event.key == pg.K_UP:
                    MoveUp = False
                if event.key == pg.K_DOWN:
                    MoveDown = False

    ################################################################


    ################################################################
        
        
        #맵#########################################################
        #층이동
        if(Floor_move):
            Floor_move = False
            Floor_now = Floor.Floor()
            Room_now = Floor_now.get_room()

        #맵이동
        touchdoor = Room_now.enter_door(player, e_list)
        if(touchdoor!=-1): #맵이동
            Room_now = Floor_now.map_move(touchdoor, player)
            
            if(Floor_now.bossRoom() and Room_now.create_enemy()):
                boss_room = True
                e_list.append(Mob3.mob3(100,100))

            elif(Room_now.create_enemy()):
                e_list = MapList.map1(Floor_level)
                Floor_level -= 2
                boss_room = False

            else :
                boss_room = False

            h_list = []
            player.invincible(60)

        Room_now.visit()
            


        #적#########################################################

        for enemy in e_list :
            #특수효과들
            enemy.moving(player) 
            enemy.shot(player,b_list)
            enemy.create(e_list, b_list, player)
            ########################################################
            Crash.E_bump_list(enemy,e_list) #몬스터끼리 겹치지 않도록
            enemy.body_hit(player) # 몬스터와 플레이어의 피격 판정
            if(enemy.death()): # 몬스터 죽음
                if(random.randrange(0,10) == 9):
                    h_list.append(Heart.Heart(enemy.get_x(),enemy.get_y()))

                e_list.remove(enemy)
                del(enemy)

        #플레이어#########################################################
        ##스킬 1
        #
        #sub_d : 스킬의 방향
        #skill1_time : 스킬 이펙트 지속시간 
        #skill1_a : 플레이어가 스킬 쓴 좌표
        #skill1_e : 스킬에 맞은 적들 좌표
        
        skill.cool_1() #스킬 쿨타임 있을 시, 쿨타임 1프레임씩 해제

        ###스킬을 상, 하로 썼을 때 and 스킬 쿨타임이 0초일 때
        if((Skill_1[0] or Skill_1[1]) and skill.get_cooltime()[0]==0):
            sub_d = Skill_1[1] and 1 or 0
            player.set_direction(sub_d) #스킬의 방향으로 플레이어 방향 변경
            skill1_a = skill.position(player,200) #플레이어가 스킬 쓴 좌표 저장

            for enemy in e_list : #피격당한 적 좌표 위치 저장
                enemywhere = [enemy.get_x()+enemy.get_width()-15, enemy.get_y()+enemy.get_height()-55]
                if(skill.skill_1(player,enemy)):
                    skill1_e.append(enemywhere)

            #쿨타임 설정
            skill.make_cool_1(player)

            #스킬 이펙트 지속시간 
            skill1_time = 3
        
        ### 위의 스킬 좌, 우 버전
        if((Skill_1[2] or Skill_1[3]) and skill.get_cooltime()[0]==0):
            sub_d = (Skill_1[2] and 2 or 3)
            player.set_direction(sub_d)
            skill1_a = skill.position(player,200)
            for enemy in e_list :
                enemywhere = [enemy.get_x()+enemy.get_width()-15, enemy.get_y()+enemy.get_height()-55]
                if(skill.skill_1(player,enemy)):
                    skill1_e.append(enemywhere)
            skill.make_cool_1(player)
            skill1_time = 3
        
        #스킬 이펙트 지속시간이 끝나있으면 피격적 위치 리스트를 비운다
        if(skill1_time == 0):
            del skill1_e[:]
        
        #######################################################################
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
              
       ##########################################################################
        #무적 해제중
        player.inv_minus()
        
       ##########################################################################
       #하트 먹기
        for heart in h_list:
            if(heart.heart_crash(player)):
                h_list.remove(heart)
                del(heart)
       ##########################################################################
        #죽음
        if(player.death()):
            return 0 #죽었을 때 어떻게 할지 구현해야 함
        
        
        ########################################################
        
        #총알 list##############################################
        for bullet in b_list :
            if(bullet.hit_del(player)):
                b_list.remove(bullet)
                del(bullet)        

        #######################################################
        ## 이미지 출력 (아래에 놓일수록 상단 레이어)
        #######################################################
        # back ground
        screen.blit(ground_image,(0,0))
        screen.blit(wall_forest_image,(0,0))
        if(boss_room):
            screen.blit(boss_cover_image,(0,0))
        #######################################################
        # door
        if(not e_list):
            if(Room_now.get_door()[0]==True):
                screen.blit(udoor_image,(0,0))
            if(Room_now.get_door()[1]==True):
                screen.blit(ddoor_image,(0,0))
            if(Room_now.get_door()[2]==True):
                screen.blit(ldoor_image,(0,0))
            if(Room_now.get_door()[3]==True):
                screen.blit(rdoor_image,(0,0))

        ########################################################
        # HP
        text_hp = font_tvn.render("HP:",True,white)
        text_slash = font_tvn.render("/",True,white)
        text_hp_now = font_tvn.render(str(player.get_hp()),True,white)
        text_max_hp = font_tvn.render(str(player.get_max_hp()),True,white) 
        ##
        screen.blit(text_hp,(40,8))
        screen.blit(text_slash,(130,8))
        screen.blit(text_hp_now, (100,8))
        screen.blit(text_max_hp, (155,8))
        
        ########################################################
        # heart
        for heart in h_list:
           #heart_image
            screen.blit(heart_image,(heart.get_x(),heart.get_y()))
        ########################################################
        # enemy
        for enemy in e_list:
            screen.blit(pg.image.load(enemy.get_image()),(enemy.get_x(), enemy.get_y()))

        ########################################################
        #skill 1
        if(skill1_time != 0):
            if(sub_d<=1):
                screen.blit(sub_d==1 and skill1_1_1_image or skill1_1_0_image,(skill1_a[0],skill1_a[1]))
            else:
                screen.blit(sub_d==2 and skill1_1_2_image or skill1_1_3_image,(skill1_a[0],skill1_a[1]))
            for e in skill1_e:
                screen.blit(skill1_2_image, (e[0], e[1]))
            skill1_time -= 1

        ########################################################
        # player
        p_direction = player.get_direction()
        if(p_direction == 1):screen.blit(player0_image,(player.get_x(), player.get_y()-20))
        elif(p_direction == 0):screen.blit(player1_image,(player.get_x(), player.get_y()-20))
        elif(p_direction == 2):screen.blit(player2_image,(player.get_x(), player.get_y()-20))
        else:screen.blit(player3_image,(player.get_x(), player.get_y()-20))


        ########################################################
        # bullet
        for bullet in b_list:
            screen.blit(bullet_image,(bullet.get_x()-3,bullet.get_y()-3))

        ########################################################

        pg.display.flip()
