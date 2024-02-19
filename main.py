import pygame, controls
import sys
from gun import Gun
from pygame.sprite import Group
from stats import Stats
def run():
    
    pygame.init()
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w //3
    screen_height = screen_info.current_h - 30
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space")
    bg_color = (8, 1, 28)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    clock = pygame.time.Clock()
    fps = 100
    stats = Stats()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(inos, bullets)
        controls.update_inos(stats, screen, gun, inos, bullets)
        
        
        # set fps must be in the end
        clock.tick(fps)

run()