import pygame as pg
import Player
import Bullet


pg.init()

size = [720,540]
screen = pg.display.set_mode(size)
pg.display.set_caption("Devil Invade") #game title
done = False
clock = pg.time.Clock()

white = (255,255,255) #기본 색깔
black = (0,0,0)
wall = (100,100,100)

player = Player.Player(300,300,10,10)
b_list = []

MoveLeft = False
MoveRight = False
MoveUp = False
MoveDown = False

#image
bullet_image = pg.image.load("../image/enemy/BULLET.png")
mob1_image = pg.image.load("../image/enemy/mob_01.png")

#sound
pg.mixer.init()
back_music = pg.mixer.Sound('../sound/main.wav')
back_music.play(-1)

while not done :

    clock.tick(24)
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

    #interface, later, image
    font = pg.font.Font("../font/tvn.ttf", 50)
    text_hp = font.render("HP:",True,white)
    text_slash = font.render("/",True,white)
    text_hp_now = font.render(str(player.get_hp()),True,white)
    text_max_hp = font.render(str(player.get_max_hp()),True,white)
    screen.blit(text_hp,(40,8))
    screen.blit(text_slash,(130,8))
    screen.blit(text_hp_now, (100,8))
    screen.blit(text_max_hp, (155,8))
    
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

   #총알 list
    for bullet in b_list :
        bullet.move(-30,-30)
        if(bullet.hit_del(player)):
            b_list.remove(bullet)
            del(bullet)
        else:
            screen.blit(bullet_image,(bullet.get_x(),bullet.get_y()))
            

    if(player.death()):
        done = True #죽었을 때 어떻게 할지 구현해야 함 
    pg.draw.rect(screen, black, [player.get_x(), player.get_y(), 45,65],0)

    pg.display.flip()


