import pygame
from  laser import Laser
from pygame.sprite import Group
class Spaceship (pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("media/spaceship.png")
        self.rect = self.image.get_rect(midbottom = (screen_width/2,screen_height))
        self.speed = 6
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_dealy = 300

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_s] and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, self.screen_height)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left <0:
            self.rect.left = 0
        
    def recharge_laser(self):
        if not self.laser_dealy:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_dealy:
                self.laser_ready = True