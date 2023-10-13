import pygame, sys
pygame.init()

#Creating the screen
width, height = 800, 600
Screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A Platformer Level')

#Colors
cyan = (0,88,88)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Screen.fill(cyan)
    pygame.display.update()
