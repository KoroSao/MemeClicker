 
import pygame
from pygame.locals import *
import random as rd

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255,223,0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Meme Clicker")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Init surfaces
surf = pygame.display.set_mode((1280,720))
 
gold_count = 150
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                gold_count = 150
    
    gold_count *= 0.999
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    # pygame.draw.rect(surf, (0,0,0,0), pygame.Rect(1050,20,200,50))
    bg = pygame.image.load("bg.jpg").convert()
    bg = pygame.transform.scale(bg, (1280, 720))
    surf.blit(bg, (0,0))

    pygame.draw.rect(surf, GOLD, pygame.Rect(1050, 20, gold_count, 30))

    golbartemplate = "bar.png"
    goldbarimg = pygame.image.load(golbartemplate).convert_alpha()
    surf.blit(goldbarimg, (1050,20))

    dogecoin = pygame.image.load("dogecoin.png").convert_alpha()
    dogecoin = pygame.transform.scale(dogecoin, (40,40))
    surf.blit(dogecoin, (1210, 15))
    
    title = "title.png"
    titleimg = pygame.image.load(title).convert_alpha()
    surf.blit(titleimg, (20,20))
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()