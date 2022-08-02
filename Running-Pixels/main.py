import pygame
from random import randint
time_score = 0
def time_scoring():
    global time_score
    time_score = pygame.time.get_ticks() - start_time
    time_fount = pygame.font.Font("Running-Pixels/pick/fonty/xddd.ttf",14)
    time_score_surface = time_fount.render(str(time_score),False,"yellow")
    time_score_rect = time_score_surface.get_rect(topleft = (680,9))
    screen.blit(time_score_surface,time_score_rect)
    
def obs_movement(obs_list):
    if obs_list:
        for obs_rect in obs_list:
            obs_rect.x -= 6
            if obs_rect.top == 270:
                screen.blit(enemy_surface,obs_rect)
            else:
                screen.blit(flying_surface,obs_rect)
            if obs_rect.x <= -100:
                del(obs_rect) 
        return obs_list
    else:
        return []
def colision_funk(obs):
    if obs:
        for obs_rect in obs:
            if player_rect.colliderect(obs_rect):
                return False
    return True


pygame.init()                                               # inicjalizuj pygame

main_music = pygame.mixer.Sound("Running-Pixels/pick/music1.mp3")
main_music.set_volume(0.3)
main_music.play()
jump_music = pygame.mixer.Sound("Running-Pixels/pick/je.mp3")
jump_music.set_volume(1)
screen = pygame.display.set_mode((800,400))                 # ustaw konsole na 800x400
pygame.display.set_caption("Running pixels")                # ustawia nazwe konsoli
clock = pygame.time.Clock()                                   # tworzy zegar do fps gry (licznika)
test_fount = pygame.font.Font("Running-Pixels/pick/fonty/xeros_theorem.ttf",28)                      # ustawia/inicjuje font
score_fount = pygame.font.Font("Running-Pixels/pick/fonty/xeros_theorem.ttf",14)
score_surface = score_fount.render("Score: ",False, "yellow")
score_rect = score_surface.get_rect(topleft = (600,10))
background_surface = pygame.image.load("Running-Pixels/pick/background.png").convert()            # ustawia zmienna backgr. jako ładowanie obrazu
text_surface = test_fount.render("Run For Life",False,"black")
start_time = 0
enemy_surface = pygame.image.load("Running-Pixels/pick/ogr.png").convert_alpha()
enemy_x_position = 600
enemy_x_rect = enemy_surface.get_rect(topleft = (600,270))
n=1
flying_surface = pygame.image.load("Running-Pixels/pick/ufo.png").convert_alpha()

player_surface = pygame.image.load("Running-Pixels/pick/roller.png").convert_alpha()
player_rect = player_surface.get_rect(topleft = (80,275))
player_gravity = 0
game_active = True
start_time = pygame.time.get_ticks()

obs_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obs_timer,1500)
random_range = randint(850,1200)
obs_rect_list = []
print("""    
    game created by PRO.TEIN, thx to usage of:
        1) https://www.redbubble.com/i/ipad-case/Retro-Game-Over-Pixel-Graphic-by-digsterdesigns/25410010.MNKGF
        2) https://www.dreamstime.com/fantasy-wide-sci-fi-martian-background-ui-game-illustration-seamless-cartoon-
            funny-alien-planet-landscape-layers-image104553382
        3) paint 3D - 3D lib collections 
        4) Xeros Theorem Font - Author: Chequered Ink
        5) SEASIDERESORT Font - Author: Nick's Fonts """)
while True:
    if n == 0:
        main_music.play()
        n+=1
    for event in pygame.event.get():                        # tworzy pętle zadaniową (event loop)
        if  event.type == pygame.QUIT:                      # umożliwia zamkniecie programu bez błędu
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom==375:
                    jump_music.play()
                    player_gravity=-13
        if game_active==False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
    
    
        if event.type == obs_timer and game_active:
            if randint(0,2):
                obs_rect_list.append(enemy_surface.get_rect(topleft = (random_range,270)))
            else:
                if randint(0,2):
                    obs_rect_list.append(flying_surface.get_rect(topleft = (random_range,randint(265,310))))
                else:
                    obs_rect_list.append(flying_surface.get_rect(topleft = (random_range,210)))
                

    if game_active:
        screen.blit(background_surface,(0,0))                   # wyświetla grafike backgr. na ekranie od punktu startowego 0,0 lewy górny róg
        screen.blit(text_surface,(250,50))                      # ustawiamy napis i wyswietlamy
        obs_rect_list = obs_movement(obs_rect_list)
        time_scoring()
        #pygame.draw.rect(screen,"red",score_rect)              #funkcja do rysowania
        screen.blit(score_surface,score_rect)
        # screen.blit(enemy_surface,(enemy_x_rect))
        screen.blit(player_surface,(player_rect))
        # enemy_x_rect.x-=4
        # if enemy_x_rect.x==-100:
        #     enemy_x_rect.x=900
        game_active = colision_funk(obs_rect_list)


        player_gravity+=0.5
        player_rect.y+=player_gravity
        if player_rect.bottom>=375:
            player_rect.bottom=375 
        # if player_rect.colliderect(enemy_x_rect):
        #     game_active=False
 
    else:
        screen.blit(pygame.image.load("Running-Pixels/pick/go.png").convert(),(0,0))
        screen.blit(score_surface,(330,300))
        time_fount = pygame.font.Font("Running-Pixels/pick/fonty/xddd.ttf",14)
        time_score_surface = time_fount.render(str(time_score),False,"yellow")
        screen.blit(time_score_surface,(410,299))
        #enemy_x_rect.x=900
        obs_rect_list.clear()
        start_time = pygame.time.get_ticks()
        player_rect.y = 275
        main_music.stop()
        n=0

        
    
        
          
    # if player_rect.bottom>=375:
    #     player_rect.bottom=375
    # keys = pygame.key.get_pressed()                       # inny sposob na ogarnciecie spacji
    # if keys[pygame.K_SPACE]==1

    # if player_rect.colliderect(enemy_x_rect)==1:          # ustawienia warunku pod collizje
    #     pass
    
    
    
    #rysujemy tu wszytkie nasze elementy na display
    #odswierzamy wszystko z funkcją update
    pygame.display.update()                                 # w pętli odświerza ekran co zmiane
    clock.tick(60)                                          # fps na 60
