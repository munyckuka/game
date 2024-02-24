import subprocess
import pygame, sys, random
from lvl1 import Lvl1
from lvl2 import Lvl2
pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

font = pygame.font.Font("Font/monogram.ttf", 40)
level_surface = font.render("LEVEL 01", False, YELLOW)
game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()


SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))




game = Lvl1(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
game2 = Lvl2(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
def check_for_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()

def update_game_state():
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

def draw_game_objects():
    screen.fill(GREY)
    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

    if game.run:
        screen.blit(level_surface, (570, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))
    screen.blit(highscore_text_surface, (550, 15, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (625, 40, 50, 50))
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

def game_loop():
    while True:
        check_for_events()
        update_game_state()
        draw_game_objects()
        pygame.display.update()
        clock.tick(60)

# =====================
def check_for_events2():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER and game2.run:
            game2.alien_shoot_laser()

        if event.type == MYSTERYSHIP and game2.run:
            game2.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game2.run == False:
            game2.reset()

def update_game_state2():
    if game2.run:
        game2.spaceship_group.update()
        game2.move_aliens()
        game2.alien_lasers_group.update()
        game2.mystery_ship_group.update()
        game2.check_for_collisions()

def draw_game_objects2():
    screen.fill(GREY)
    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

    if game2.run:
        screen.blit(level_surface, (570, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game2.lives):
        screen.blit(game2.spaceship_group.sprite.image, (x, 745))
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game2.score).zfill(5)
    score_surface = font.render(formatted_score, False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))
    screen.blit(highscore_text_surface, (550, 15, 50, 50))
    formatted_highscore = str(game2.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, YELLOW)
    screen.blit(highscore_surface, (625, 40, 50, 50))
    game2.spaceship_group.draw(screen)
    game2.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game2.obstacles:
        obstacle.blocks_group.draw(screen)
    game2.aliens_group.draw(screen)
    game2.alien_lasers_group.draw(screen)
    game2.mystery_ship_group.draw(screen)

def game2_loop():
    while True:
        check_for_events2()
        update_game_state2()
        draw_game_objects2()
        pygame.display.update()
        clock.tick(60)


# Menu
class Button():
    def __init__(self, pos, label, callback, size):
        self.pos = pos
        self.label = label
        self.callback = callback
        self.image = pygame.Surface(size)
        self.image.fill(GREY)
        self.font = pygame.font.SysFont("Font/monogram.ttf", 40)
        self.text = self.font.render(label, False, YELLOW)
        self.rect = self.image.get_rect(center=pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()


class Menu():
    def __init__(self, screen, game):
        self.background_image = pygame.image.load('Graphics/bg_space.jpg')
        self.screen = screen
        self.width, self.height = screen.get_size()
        # self.play_button = Button((self.width // 2 - 60, self.height // 2 - 50,), "Play", self.play, (120, 40))
        self.exit_button = Button((self.width // 2 - 60, self.height // 2 + 10), "Exit", self.exit, (120, 40))
        self.title_button = Button((self.width // 2 - 60, self.height // 2 -200), "Space battle", self.title, (0, 0))
        self.lvl1_button = Button((self.width // 2 - 100, self.height // 2 - 100), "Easy", self.start_level_1, (60, 40))
        self.lvl2_button = Button((self.width // 2 + 100, self.height // 2 -100), "Hard", self.start_level_2, (60, 40))
        self.game = Lvl1(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

    def draw(self):
        self.screen.blit(self.background_image, (0,0))
        self.title_button.draw(self.screen)
        self.lvl1_button.draw(self.screen)
        self.lvl2_button.draw(self.screen)
        # self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)

    def handle_event(self, event):
        # self.play_button.handle_event(event)
        self.exit_button.handle_event(event)
        self.lvl1_button.handle_event(event)
        self.lvl2_button.handle_event(event)

    def start_level_1(self):
        # game = Lvl1(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
        print("lvl1")
        game_loop()
    
    def start_level_2(self):
        # game = Lvl2(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
        print("lvl2")
        game2_loop()

    def exit(self):
        pygame.quit()
        sys.exit()

    def title(self):
        print('Space battle by kuanysh')

menu = Menu(screen, game)


def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        menu.handle_event(event)
        menu.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()