import pygame, sys
from spaceship import Spaceship
from laser import Laser
pygame.init()


GREY = (29, 29, 27)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spaceship adventure")

clock = pygame.time.Clock()
spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#   update()
    spaceship_group.update()

#   draw
    screen.fill(GREY)
    spaceship_group.draw(screen)
    spaceship_group.sprite.lasers_group.draw(screen)



    pygame.display.update()
    clock.tick(60)