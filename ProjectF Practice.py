import pygame 
import pytmx
from sys import exit

pygame.init() #necessary for all pygame codes, initaties subparts like rendering images and sounds

screen = pygame.display.set_mode((800,800)) #needs a tuple width,height
pygame.display.set_caption("Project-F-Demo")
clock = pygame.time.Clock() 

test_font = pygame.font.Font("fonts/star-crush/star_crush.ttf", 50) #font type (s), size(int)
grass_surface = pygame.image.load('graphics/tested_map.png').convert_alpha() #any graphics is a new surface
text_surface = test_font.render("welcome to azania", False, "black" ) #text information, antialisaing, colour
# for pytmx future use map_surface = pytmx.load_pygame("graphics/test_map.tmx")

#slime variables
slime_surface = pygame.image.load("graphics/BlueSlime.png").convert_alpha()
slime_rect = slime_surface.get_rect(topleft = (400,400))


kei_surface = pygame.image.load("graphics/kei_base_sprite.png").convert_alpha()
kei_rect = kei_surface.get_rect(topleft = (400, 400)) #demo --> player_rect = player_surf.get_rect(topleft = (x,y))
#kei_surf = pygame.image.load

while True: #event loop 

    for event in pygame.event.get(): #Checks for any player input
        if event.type == pygame.QUIT: #closing the window
            pygame.quit()
            exit() #imported from sys, kills the while True loop
    # draw all our elements
    # update everything 

    screen.blit(grass_surface, (0,0)) #stands for block image transfer, put one surface onto another
    # needs to be parsed through a loop first to draw (map_surface, (0,0))
    screen.blit(text_surface, (300, 50))

    screen.blit(slime_surface, slime_rect)
    slime_rect.left += 5
    if slime_rect.left >= 800: slime_rect.left = 0

    kei_rect.left += 3
    if kei_rect.left >= 800: kei_rect.left = 0
    kei_rect.left
    screen.blit(kei_surface, kei_rect)
    #0,0 is top leftmost corner 
    # pygame prints in order
    #collisions
    if kei_rect.colliderect(slime_rect): 
        print("collision")
    mouse_pos = pygame.mouse.get_pos()
    if kei_rect.collidepoint((mouse_pos)): #(x,y)
        print(pygame.mouse.get_pressed())
        print("collided!")

    pygame.display.update()
    clock.tick(60) # controls frame rate, caps it at 60