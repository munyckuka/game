import pygame
import sys
from bullet import Bullet
from alien import Ino
import time

screen_info = pygame.display.Info()
screen_width = screen_info.current_w//3
screen_height = screen_info.current_h-30
# all user input here // events
def events(screen, gun, bullets):
    # close game
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    # move space_ship
            
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_d:
                        gun.mright = True
                 elif event.key == pygame.K_a:
                        gun.mleft = True
                 elif event.key == pygame.K_s:
                       new_bullet = Bullet(screen, gun)  
                       bullets.add(new_bullet)  

            elif event.type == pygame.KEYUP:
                  if event.key == pygame.K_d:
                        gun.mright = False
                  elif event.key == pygame.K_a:
                        gun.mleft = False
# screen update
def update(bg_color, screen, gun, inos, bullets):
      screen.fill(bg_color)
      for bullet in bullets.sprites():
            bullet.draw_bullet()
      gun.output()
      inos.draw(screen)
      pygame.display.flip()


# delete bullets
def update_bullets(inos, bullets):
      bullets.update()
      for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                  bullets.remove(bullet)
      collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
def update_inos(stats, screen, gun, inos, bullets):
      inos.update()
      if pygame.sprite.spritecollideany(gun, inos):
            gun_kill(stats, screen, gun, inos, bullets)

def create_army(screen, inos):
      ino = Ino(screen)
      ino_width = ino.rect.width
      number_ino_x = int((screen_width - 2 * ino_width) / ino_width)
      ino_height = ino.rect.height
      number_ino_y = int((screen_height - 100- 2 * ino_height) / ino_height)

      for row_number in range(number_ino_y - 2):
            for ino_number in range(number_ino_x):
                  ino = Ino(screen)
                  ino.x = ino_width + ino_width * ino_number
                  ino.y = ino_height + ino_height * row_number
                  ino.rect.x = ino.x
                  ino.rect.y = ino.rect.height +ino.rect.height * row_number
                  inos.add(ino)
# death
def gun_kill(stats, screen, gun, inos, bullets):
      stats.guns_left -=1
      inos.empty()
      bullets.empty()
      create_army(screen, inos)
      gun.create_gun()
      time.sleep(2)