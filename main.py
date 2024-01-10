import pygame, controls
import sys
from gun import Gun
from pygame.sprite import Group
def run():
    pygame.init()
    screen = pygame.display.set_mode((640, 960))
    pygame.display.set_caption("Space")
    bg_color = (8, 1, 28)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    clock = pygame.time.Clock()
    fps = 75

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(bullets)
        controls.update_inos(inos)
        # Get the current FPS
        clock.tick(fps)

        # Print the FPS to the console
        print(fps)
run()