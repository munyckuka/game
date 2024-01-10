import pygame
from pygame.sprite import Group

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (255, 255, 255)
        self.speed = 3.5
        self.rect.centerx = gun.rect.centerx 
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

#  pos update
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
#  bullets texture
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)