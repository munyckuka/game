import pygame
class Gun():
    def __init__(self, screen):
        self.screen = screen
        # import image and rescale
        self.image = pygame.image.load("media\space_ship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        # hitbox
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # for movement
        self.mright = False
        self.mleft = False
    
    # draw ship
    def output(self):
        self.screen.blit(self.image, self.rect)

    # pos update
    def update_gun(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2.5
        elif self.mleft and self.rect.left > 0:
            self.center  -= 2.5
        
        self.rect.centerx = self.center