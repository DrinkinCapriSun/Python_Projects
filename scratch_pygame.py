import pygame
from sys import exit

def displayer_score():
    current_time = int(pygame.time.get_ticks() / 1000)- start_time #to subtract the start_time to current_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)


# THIS IS THE VERY VERY VERY FIRST THING THAT NEED TO DO!!!
pygame.init()# set the screen display (width, height) base on px
screen = pygame.display.set_mode((800,400))# the title of the game
pygame.display.set_caption('Runner')# to help with adjusting the fps
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)# to make a text (font type, font size)
game_active = False
start_time = 0
current_time = pygame.time.get_ticks()

sky_surface = pygame.image.load('graphics/Sky.png').convert()# to set the of the surface within the screen(width,height)
ground_surface = pygame.image.load('graphics/ground.png').convert()
# (text, anti-aliase, color)
# score_surf = test_font.render('My game', False, (64,64,64))# used color here is rgb
# score_rect = score_surf.get_rect(center = (400, 50))

# snail surface
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

# player surface
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))# to get the rectangle of the player_surf Variable | player rectangle (left, top, width, height)
player_gravity = 0 # gravity
# intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400,200))

# to put color on the surface
# test_surface.fill('Red')


while True:# forever loop to actually stop the screen from closing
    for event in pygame.event.get():# for loop to be able to close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()# exit() to stop the while loop. this is from Import

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:  # Check if any mouse button is pressed
                if player_rect.collidepoint(event.pos) and player_rect.bottom:  # Check if the left mouse button (button 1) is pressed to the player rect
                    player_gravity = -20  # Modify player's gravity (example)

            if event.type == pygame.KEYDOWN:# Check if any key is pressed
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:# Check if the spacebar key is pressed
                    player_gravity = -20

        else: # to restart the game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)# score back to 0 when restarted

        # if event.type == pygame.KEYUP:# to press keyup
        #     print('key up')

    if game_active:#INGAME CODE
        # to put one surface to another surface (surface,position(x and y axis)->px) already have surface Variable -> test_surface||position is to position the Variable
        # +x= right, -x= left, +y= down, -y= up
        screen.blit(sky_surface,(0,0))#sky
        screen.blit(ground_surface,(0, 300))#ground
        # pygame.draw.rect(screen, '#c0e8ec', score_rect,)#this is the center when using border width below | used color here is hex
        # pygame.draw.rect(screen,'#c0e8ec', score_rect, 10) #rectangle of drawing (display surface, color, the Variable you want to put to, border width)
        # # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))#circle | pygame.Rect(left, top, width, height)
        # screen.blit(score_surf, score_rect)#score
        displayer_score()

        # snail
        snail_rect.x -=4 #.x means x coord. so -4 for snail to go to left
        if snail_rect.right <= 0: #check whether the right side of snail is 0 coord
            snail_rect.left = 800 #if true, then show the left side of snail too 800 coord
        screen.blit(snail_surf, snail_rect) #coordinates of snail

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:# to make the player standing on the ground
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect) #already assigned the coordinates on the Variable

        #collision
        if snail_rect.colliderect(player_rect):# to quit when player touches the snail
           game_active = False

    else:# when the game ended
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)


        # keys = pygame.key.get_pressed()#to press keys
        # if keys[pygame.K_SPACE]:#check the documentation what buttons is needed to be press
        #     print('jump')

        # if player_rect.collidedrect(snail_rect):
            # print('collision')

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print('collision')

    pygame.display.update()# this is to update everything to screen Variable
    clock.tick(60)# this is to set the maximum fps