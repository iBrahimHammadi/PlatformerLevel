import pygame, sys
pygame.init()

clock = pygame.time.Clock()

def playerMovement():
    global player_speed
    player.x += player_speed

#Creating the screen
width, height = 800, 600
Screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A Platformer Level')

#Creating the ground
ground = pygame.Rect(0, 540, width, height)
#Creating the player
player = pygame.Rect(width/2 - 15, 480, 30, 60 )
#Creating the player Speed
player_speed = 0

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
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    Screen.fill(cyan)
    playerMovement()
    #Drawing the ground
    pygame.draw.rect(Screen,(200, 200, 200), ground)
    pygame.draw.rect(Screen,(10, 10, 10), player)
    pygame.display.update()
    clock.tick(60)
