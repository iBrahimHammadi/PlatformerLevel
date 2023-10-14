import pygame, sys
pygame.init()

clock = pygame.time.Clock()

def playerMovement():
    global player_speed
    player.x += player_speed
    if player.right >= width:
        player.right = width
    if player.left <= 0:
        player.left = 0


#Creating the screen
width, height = 800, 600
Screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A Platformer Level')

#Creating the ground
ground = pygame.Rect(0, 540, width, height)
#Creating the player
player = pygame.Rect(width/2 - 15, 480, 30, 60 )
#Player speed and gravity
jumping = False
player_speed = 0
gravity = 1
jump_height = 20
y_vel = jump_height

#Colors
cyan = (0,88,88)
while True:
    
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_speed += 5
            if event.key == pygame.K_LEFT:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_speed -= 5
            if event.key == pygame.K_LEFT:
                player_speed += 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jumping = True
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if jumping:
        player.y -= y_vel
        y_vel -= gravity
        if y_vel < -jump_height:
            jumping = False
            y_vel = jump_height


    Screen.fill(cyan)
    playerMovement()
    #Drawing the ground
    pygame.draw.rect(Screen,(200, 200, 200), ground)
    pygame.draw.rect(Screen,(10, 10, 10), player)
    pygame.display.update()
    clock.tick(60)