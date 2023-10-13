import pygame, sys
pygame.init()

clock = pygame.time.Clock()

#Creating the screen
width, height = 800, 600
Screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A Platformer Level')

#Creating the ground
ground = pygame.Rect(0, 540, width, height)

#Colors
cyan = (0,88,88)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Screen.fill(cyan)
    #Drawing the ground
    pygame.draw.rect(Screen,(0, 0, 0), ground)
    pygame.display.update()
    clock.tick(60)
