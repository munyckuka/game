import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пример с двумя кнопками")

# Установка цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Установка шрифта
font = pygame.font.Font(None, 36)

# Функция для отображения текста на кнопке
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Класс для кнопок
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.Font(None, 36)
            text = font.render(self.text, 1, BLACK)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        
        return False

# Функция для отображения интерфейса
def draw_interface():
    screen.fill(WHITE)
    draw_text('Нажмите кнопку, чтобы открыть меню', font, BLACK, screen, 20, 20)

# Главная функция
def main():
    running = True
    menu_opened = False

    # Создание кнопки для открытия меню
    open_button = Button((0, 255, 0), 50, 100, 200, 50, 'Открыть меню')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if open_button.is_over(pygame.mouse.get_pos()):
                    menu_opened = True

        # Отображение интерфейса
        draw_interface()

        # Отображение кнопки для открытия меню
        open_button.draw(screen)

        # Если меню открыто, отображаем две кнопки
        if menu_opened:
            button1 = Button((255, 0, 0), 50, 200, 200, 50, 'Кнопка 1')
            button2 = Button((0, 0, 255), 50, 300, 200, 50, 'Кнопка 2')

            button1.draw(screen)
            button2.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
