import pygame
import sys 

pygame.init()

screen = pygame.display.set_mode((1600.900))
pygame.display.set_caption("Koukaton Game")

background = pygame.image.load('pg_bg.jpg')

koukaton = pygame.image.load('3.png')

koukaton_flipped = pygame.transform.flip(koukaton, True, False)

clock = pygame.time.Clock()
fps = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(koukaton_flipped, (300, 200))

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
sys.exit()