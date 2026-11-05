import pygame 
from sys import exit

pygame.init() #necessary for all pygame codes, initaties subparts like rendering images and sounds

screen = pygame.display.set_mode((800,400)) #needs a tuple width,height
pygame.display.set_caption("Project-F-Demo")

clock = pygame.time.Clock() 


test_surface = pygame.Surface((100, 200)) #w, h
test_surface.fill("Red") # fill shape colour 


while True: 

    for event in pygame.event.get(): #Checks for any player input
        if event.type == pygame.QUIT: #closing the window
            pygame.quit()
            exit() #imported from sys, kills the while True loop
    # draw all our elements
    # update everything 

    screen.blit(test_surface, (200,100)) #stands for block image transfer, put one surface onto another
    #0,0 is top leftmost corner 


    pygame.display.update()
    clock.tick(60) # controls frame rate, caps it at 60