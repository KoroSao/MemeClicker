import pygame
from pygame.locals import *
from filepath import *
from font import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255,223,0)
 
pygame.init()
 
d_is_for_dogecoin = pygame.mixer.music.load("sounds/dogecoinsong.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

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
 
doge_count = 0
max_doge_count = 150
clicks = 0
r = 255
g = b = 0

# -------- Main Program Loop -----------
while not done:

    if doge_count >= max_doge_count:
        doge_count = 0
        max_doge_count *= 2.5
        max_doge_count = int(max_doge_count)

    if(r > 0 and b == 0):
        r -= 3
        g += 3
    if(g > 0 and r == 0):
        g -= 3
        b += 3
    if(b > 0 and g == 0):
        r += 3
        b -= 3


    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                doge_count = 150
        if event.type == MOUSEBUTTONDOWN:
            clicks += 1
            doge_count += 1
    
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    # pygame.draw.rect(surf, (0,0,0,0), pygame.Rect(1050,20,200,50))
    bg = pygame.image.load(PATH_bg).convert()
    bg = pygame.transform.scale(bg, (1280, 720))
    surf.blit(bg, (0,0))

    pygame.draw.rect(surf, GOLD, pygame.Rect(1050, 20, doge_count * 150 // max_doge_count, 30))

    goldbarimg = pygame.image.load(PATH_bar).convert_alpha()
    surf.blit(goldbarimg, (1050,20))

    dogecoin = pygame.image.load(PATH_dogecoin).convert_alpha()
    dogecoin = pygame.transform.scale(dogecoin, (40,40))
    surf.blit(dogecoin, (1210, 15))
    
    # titleimg = pygame.image.load(PATH_title).convert_alpha()
    # surf.blit(titleimg, (20,20))
    game_name_gui = sketch_font.render("Meme Clicker", True, (0, 0, 0))
    screen.blit(game_name_gui,(20, 30 ))
    click_count_gui = sketch_font.render("Clicks : " + str(clicks), True, (0,0,0))
    screen.blit(click_count_gui, (20,60))

    click_count_gui = sketch_font_20.render(str(doge_count) + " / " + str(max_doge_count), True, (0,0,0))
    screen.blit(click_count_gui, (1100,26))

    pygame.draw.rect(surf, (r,g,b), pygame.Rect(1018, 68, 254, 624), border_radius = 10)
    pygame.draw.rect(surf, (220,220,220), pygame.Rect(1020, 70, 250, 620), border_radius = 10)
    
    game_name_gui = sketch_font.render("Upgrades", True, (r, g, b))
    screen.blit(game_name_gui,(1030, 80 ))

    gpu = pygame.image.load(PATH_gpu).convert_alpha()
    gpu = pygame.transform.scale(gpu, (200,100))
    surf.blit(gpu, (1050, 150))

    piss = pygame.image.load(PATH_piss_drawer).convert_alpha()
    piss = pygame.transform.scale(piss, (200,100))
    surf.blit(piss, (1050, 270))
    
    
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()