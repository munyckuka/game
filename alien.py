from typing import Any
import pygame
# alien 
class Ino(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('media\\alien.png')
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
# u see this aliens
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.1
        self.rect.y = self.y