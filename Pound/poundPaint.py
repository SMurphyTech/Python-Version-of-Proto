
import pygame
import poundPlayer

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

mode = "overworld"
x = 50
y = 50
speedX = 0
speedY = 0
lx = 50
player = poundPlayer.pound_player(350, 250)

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Rpg prototype")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if(mode == "overworld"):
            if event.type == pygame.KEYDOWN:
                # key is pressed down
                if event.key == pygame.K_DOWN:
                    speedY = 6
                if event.key == pygame.K_UP:
                    speedY = -6
                if event.key == pygame.K_RIGHT:
                    speedX = 6
                if event.key == pygame.K_LEFT:
                    speedX = -6
            elif event.type == pygame.KEYUP:
                # key is let up
                # "and speedX == 6" is to prevent stopping movement while another key is pressed
                if event.key == pygame.K_DOWN and speedY == 6:
                    speedY = 0
                elif event.key == pygame.K_UP and speedY == -6:
                    speedY = 0
                elif event.key == pygame.K_RIGHT and speedX == 6:
                    speedX = 0
                elif event.key == pygame.K_LEFT and speedX == -6:
                    speedX = 0

    screen.fill((0, 0, 0))

    player.update
    # Beginning of Drawing

    pygame.draw.rect(screen, WHITE, [x, y, 50, 50])
    f = open("Pound/test.txt")
    for line in f:
        # print(repr(line))
        if line == "hs\n":
            lx += 1
            pygame.draw.rect(screen, RED, [lx, 50, 10, 10])

    # End of Drawing
    pygame.display.flip()

    clock.tick(60)

pygame.quit()