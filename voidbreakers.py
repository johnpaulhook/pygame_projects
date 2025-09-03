
# ---------------- IMPORTS ---------------- #
import pygame
import sys
import time
import random 
# ---------------- SETUP ---------------- #
pygame.init()                          # start pygame
WIDTH, HEIGHT = 1800, 1000            # window size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VoidBreakers")  # window title
clock = pygame.time.Clock()            # controls game speed (FPS)
ship_x = 250
ship_y = 0
stars = []
for i in range(1001):
    star_x = random.randint(0, WIDTH)
    star_y = random.randint(0, HEIGHT)
    stars.append([star_x, star_y])
    
    
pygame.draw.rect(screen, (255, 255, 255) ,(ship_x, ship_y, 100, 1), thickness = 0)
# ---------------- GAME LOOP ---------------- #
while True:
    for event in pygame.event.get():      # check events
        if event.type == pygame.QUIT:     # click [X] button
            pygame.quit()                 # shut down pygame
            sys.exit()
        if event.type == pygame.K_SPACE:
            pygame.draw.rect(screen, (255, 0, 0),ship_x, ship_y, 10, 2)

    # --- drawing ---
    screen.fill((0, 0, 0))             # dark background

    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), star, 2)

    
    star[0] -= random.randint(1,5)
    
    if star[0] < 0 :
        star[0] = WIDTH
        star[1] = random.randint(0, HEIGHT)
    # --- update screen ---
    pygame.display.flip()                 # update frame
    clock.tick(60)                        # limit to 60 FPS
