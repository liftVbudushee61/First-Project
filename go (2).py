import pygame
from hero import Hero

DARKBACKGROUND = (54, 55, 55)
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("My best game")
clock = pygame.time.Clock()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
DONE = False
FPS = 30

my_hero = Hero(7, 7, 7, 2, 1, 1)

while not DONE:

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                DONE = True
                quit()

            if event.key == pygame.K_w:
                my_hero.moveY(-10)

            if event.key == pygame.K_s:
                my_hero.moveY(10)

            if event.key == pygame.K_a:
                my_hero.moveX(-10)

            if event.key == pygame.K_d:
                my_hero.moveX(10)

    screen.fill(DARKBACKGROUND)
    pygame.draw.circle(screen, pygame.Color("red"), (my_hero.get_position()[0], my_hero.get_position()[1]), 20)
    clock.tick(FPS)
    pygame.display.flip()
