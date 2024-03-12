import pygame
import button
import math
import random

pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()
pygame.mixer.music.set_volume(0.3)

#icon
pygame_icon = pygame.image.load('icon.png')
pygame.display.set_icon(pygame_icon)

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jungle Adventures')

#load button images
start_img = pygame.image.load("start_btn.png").convert_alpha()
exit_img = pygame.image.load("exit_btn.png").convert_alpha()
settings_img = pygame.image.load("settings.png").convert_alpha()
m_settings_img = pygame.image.load("m_settings.png").convert_alpha()
mus_resume_img = pygame.image.load("mus_resume.png").convert_alpha()
mus_stop_img = pygame.image.load("mus_stop.png").convert_alpha()
restart_img = pygame.image.load("restart.png").convert_alpha()

restart_l = pygame.image.load("restart_l.png").convert_alpha()
exit_l = pygame.image.load("exit_l.png").convert_alpha()

#dialogue windows
dialogue_window1_img = pygame.image.load("dialogue_window1.png").convert_alpha()
dialogue_window2_img = pygame.image.load("dialogue_window2.png").convert_alpha()
dialogue_window3_img = pygame.image.load("dialogue_window3.png").convert_alpha()
dialogue_window4_img = pygame.image.load("dialogue_window4.png").convert_alpha()
dialogue_window5_img = pygame.image.load("dialogue_window5.png").convert_alpha()

#music windows
start_mus = pygame.image.load("start_btn.png").convert_alpha()
stop_mus = pygame.image.load("exit_btn.png").convert_alpha()

#create button instances
start_button = button.Button(300, 400, start_img, 0.8)
exit_button = button.Button(750, 400, exit_img, 0.8)
settings_button = button.Button(10, 10, settings_img, 0.3)
m_settings_button = button.Button(430, 80, m_settings_img, 1.9)
mus_resume_button = button.Button(520, 360, mus_resume_img, 0.8)
mus_stop_button = button.Button(520, 500, mus_stop_img, 0.8)
dialogue_window1_button = button.Button(0,575, dialogue_window1_img, 1)
dialogue_window2_button = button.Button(0,575, dialogue_window2_img, 1)
dialogue_window3_button = button.Button(0,575, dialogue_window3_img, 1)
dialogue_window4_button = button.Button(0,575, dialogue_window4_img, 1)
dialogue_window5_button = button.Button(0,575, dialogue_window5_img, 1)
restart_button = button.Button(350, 600, restart_img, 0.8)
exit_button2 = button.Button(700, 600, exit_img, 0.8)

restart_button_l = button.Button(350, 400, restart_l, 0.8)
exit_button_l = button.Button(700, 400, exit_l, 0.8)
#fonts
font_main = pygame.font.Font('DisposableDroidBB.ttf', 60)
font_l = pygame.font.Font('DisposableDroidBB.ttf', 150)


#colors
white = (255, 255, 255)
yellow = (255, 255, 102)
gray = (128, 128, 128)
light_gray = (211, 211, 211)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
brown = (160, 82, 45)
background_color = white
score = 0


#sprites
player = pygame.transform.scale(pygame.image.load('main_spirit_r.png'), (300, 300)).convert_alpha()
dialogueBg = pygame.transform.scale(pygame.image.load('background.png'), (1280, 720)).convert_alpha()
templeBgDoor = pygame.transform.scale(pygame.image.load("temple_window1.png"), (1280, 720)).convert_alpha()
templeBg = pygame.transform.scale(pygame.image.load("temple_window2.png"), (1280, 720)).convert_alpha()
title = pygame.transform.scale(pygame.image.load('title1.png'), (1100, 150)).convert_alpha()
coin = pygame.transform.scale(pygame.image.load('coin.png'), (100, 100)).convert_alpha()
winBg = pygame.transform.scale(pygame.image.load('win_window.png'), (1280, 720)).convert_alpha()
loseBg = pygame.transform.scale(pygame.image.load('lose.png'), (1280, 720)).convert_alpha()

monster = pygame.transform.scale(pygame.image.load('monster.png'), (275, 275)).convert_alpha()
hearts = pygame.transform.scale(pygame.image.load('life_three.png'), (240, 80)).convert_alpha()

#time
timer = pygame.time.Clock()
fps = 60
a, b = pygame.mouse.get_pos()
game_over = True
settings = False
player_x, player_y = 1280/2, 720/2+80

x_change = 0
y_change = 0
player_speed = 15
wd1 = 0

scroll = 0
frames = 0




def setup():
    global frames, scroll, bg_width, background, temple_screen_scroll, start_menu, temple_window, dialogue_window, win_window, player_width, current_room, coin_room, game_score, dialogueBg, tiles, wd1, jump, jump_height, monke_x, lifes, lose, d_message
    temple_screen_scroll = 0
    frames = 0
    scroll = 0
    background = dialogueBg
    bg_width = background.get_width()
    player_width = player.get_width()
    start_menu = True
    dialogue_window = False
    temple_window = False
    win_window = False
    current_room = 0
    coin_room = 1
    game_score = 0
    tiles = math.ceil(WIDTH / bg_width) + 1
    wd1 = 0
    jump = False
    jump_height = 16
    monke_x = 1100
    lifes = 0
    lose = False
    d_message = False

setup()
running = True
while running:
    timer.tick(fps)
    frames = (frames%player_speed) + 1
    pygame.font.get_fonts()
    keys = pygame.key.get_pressed()
    if player_x > bg_width + player_width/2:
        player_x = -player_width/2
    if player_x < -player_width/2:
        player_x = bg_width + player_width/2
    if jump == True:
        player_y -= jump_height
        if player_y <= 100:
            jump_height *= -1
        if(player_y  > 440):
            player_y = 440
            jump_height *= -1
            jump = False
    rect = player.get_rect()
    rect.center = (player_x, player_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and settings == False:
            if event.key == pygame.K_SPACE:
                jump = True
                d_message = False
            if event.key == pygame.K_a:
                player = pygame.transform.scale(pygame.image.load('main_spirit_l.png').convert_alpha(), (300, 300))
                x_change = -player_speed/2
            elif event.key == pygame.K_d:
                player = pygame.transform.scale(pygame.image.load('main_spirit_r.png').convert_alpha(), (300, 300))
                x_change = player_speed/2
        if event.type == pygame.KEYUP and settings == False:
            if event.key == pygame.K_a:
                player = pygame.transform.scale(pygame.image.load('main_spirit_l.png').convert_alpha(), (300, 300))
                x_change = 0
            if event.key == pygame.K_d:
                player = pygame.transform.scale(pygame.image.load('main_spirit_r.png').convert_alpha(), (300, 300))
                x_change = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            a, b = pygame.mouse.get_pos()
    if settings == True:
        x_change = 0
    if start_menu == True:
        screen.blit(background, (0, 0))
        screen.blit(title, (100, 80))
        if start_button.draw(screen):
            dialogue_window = True
            start_menu = False
        if exit_button.draw(screen):
            running = False
        screen.blit(player, rect)


    if dialogue_window == True:
        hearts = pygame.transform.scale(pygame.image.load('life_three.png'), (240, 80)).convert_alpha()
        if abs(scroll) > bg_width:
            scroll = 0
        if(x_change < 0):
            scroll += player_speed
            if(frames % player_speed / 2 > player_speed / 4):
                player = pygame.transform.scale(pygame.image.load('main_spirit_l.png'), (300, 300))
            else:
                player = pygame.transform.scale(pygame.image.load('main_spirit_l_mov.png'), (300, 300))
        if(x_change > 0):
            scroll -= player_speed
            if(frames % player_speed / 2 > player_speed / 4):
                player = pygame.transform.scale(pygame.image.load('main_spirit_r.png'), (300, 300))
            else:
                player = pygame.transform.scale(pygame.image.load('main_spirit_r_mov.png'), (300, 300))
        screen.fill(white)
        player_x += x_change
        for i in range (-1, tiles):
            screen.blit(background, (i * bg_width + scroll, 0))
        match wd1:
            case 0:
                if dialogue_window1_button.draw((screen)):
                    wd1 +=1
                    dialogue_window2_button.draw((screen))
            case 1:
                if dialogue_window2_button.draw(screen):
                    wd1 +=1
                    dialogue_window3_button.draw(screen)
            case 2:
                if dialogue_window3_button.draw(screen):
                    wd1 +=1
                    pass
            case 3:
                if(player_x >= bg_width / 2 - temple_screen_scroll or x_change < 0):
                    temple_screen_scroll = max(min(temple_screen_scroll + x_change*2, bg_width), 0)
                if(temple_screen_scroll >= bg_width - player_x + player_width/2):
                    player_x -= x_change*3

                if(temple_screen_scroll >= bg_width):
                    background = templeBgDoor
                    wd1 +=1
                    scroll = 0
                    dialogue_window = False
                    temple_window = True
                screen.blit(templeBgDoor, (bg_width - temple_screen_scroll, 0))
                pass
        screen.blit(player, rect)

    if temple_window == True:
        player_x = min(player_x + x_change*2, bg_width/2)
        if settings == False:
            monke_x -= 10
        else:
            pass
        if(player_x >= 540) and x_change != 0:
            monke_x -= 10 * x_change / abs(x_change)
        if(monke_x < 0):
            monke_x = 1200
        if(monke_x > 1200):
            monke_x = 1200
        if (game_score < 1):
            player_x = max(player_width/2, player_x)
        elif player_x < 0:
            background = dialogueBg
            temple_window = False
            win_window = True
        if abs(scroll) > bg_width:
            scroll = 0
            if(x_change < 0):
                current_room -= 2
            current_room += 1
        if(x_change < 0):
            if(current_room > 0 or scroll < 0 ):
                scroll += player_speed
                player_x += player_speed

            if(frames % player_speed / 2 > player_speed / 4):
                player = pygame.transform.scale(pygame.image.load('main_spirit_l.png').convert_alpha(), (300, 300))
            else:
                player = pygame.transform.scale(pygame.image.load('main_spirit_l_mov.png').convert_alpha(), (300, 300))
        if(x_change > 0):
            if(player_x == bg_width/2):
                scroll -= player_speed

            if(frames % player_speed / 2 > player_speed / 4):
                player = pygame.transform.scale(pygame.image.load('main_spirit_r.png').convert_alpha(), (300, 300))
            else:
                player = pygame.transform.scale(pygame.image.load('main_spirit_r_mov.png').convert_alpha(), (300, 300))

        coin_pos = (coin_room - current_room) * bg_width + scroll
        if abs(coin_pos - player_x) <= 40:
            if (320 - player_y) <= 40:
                coin_room += random.randint(1, 5)
                game_score += 1


        if abs(player_x - monke_x) <= 40 and abs(player_y - 440) <= 150:
            lifes += 1
            monke_x = 1500
            player_x = 320
            d_message = True
            if game_score == 0:
                pass
            else:
                game_score -=1
            match lifes:
                case 1:
                    hearts = pygame.transform.scale(pygame.image.load('life_two.png'), (160, 80)).convert_alpha()
                    pass
                case 2:
                    hearts = pygame.transform.scale(pygame.image.load('life_one.png'), (80, 80)).convert_alpha()
                    pass

                case _:
                    lose = True

        for i in range (-1, tiles):
            screen.blit(templeBg, (i * bg_width + scroll, 0))
            if(current_room <= 1):
                screen.blit(templeBgDoor, (-current_room * bg_width + scroll, 0))
            if(abs(current_room - coin_room) == 1 or current_room - coin_room == 0):
                coin_rect = coin.get_rect()
                coin_rect.center = (-(current_room-coin_room) * bg_width + scroll, 400)
                screen.blit(coin, coin_rect)
            pass
        screen.blit(player, rect)
        screen.blit(monster, (monke_x, 290))
        screen.blit(hearts, (100, 15))
        if wd1 == 4:
            if dialogue_window5_button.draw(screen):
                wd1 += 1
        score = str(game_score)
        text2 = font_main.render("Your score: " + score, True, black)
        text_x2 = 4
        text_y2 = 90
        screen.blit(text2, [text_x2, text_y2])
        text = font_main.render("Your score: " + score, True, yellow)
        text_x = 10
        text_y = 90
        screen.blit(text, [text_x, text_y])
    if win_window == True:
        screen.blit(winBg, (0, 0))
        player_x = 3*bg_width
        if exit_button2.draw(screen):
            running = False
        if restart_button.draw(screen):
            setup()
            player_x = bg_width/2
            win_window = False
    if lose == True:
        screen.blit(loseBg, (0, 0))
        player_x = 3 * bg_width
        if exit_button_l.draw(screen):
            running = False
        if restart_button_l.draw(screen):
            setup()
            player_x = bg_width / 2
            lose = False
        score = str(game_score)
        text2 = font_l.render("Your score: " + score, True, black)
        text_x2 = 240
        text_y2 = 270
        screen.blit(text2, [text_x2, text_y2])
        text = font_l.render("Your score: " + score, True, gray)
        text_x = 245
        text_y = 270
        screen.blit(text, [text_x, text_y])
    if settings_button.draw(screen):
        settings = True
    if d_message == True:
        if lose == True:
            pass
        else:
            dialogue_window4_button.draw(screen)
    if settings == True:
        m_settings_button.draw(screen)
        if mus_stop_button.draw(screen):
            pygame.mixer.music.pause()
            settings = False

        if mus_resume_button.draw(screen):
            pygame.mixer.music.unpause()
            settings = False
    pygame.display.flip()
pygame.quit()