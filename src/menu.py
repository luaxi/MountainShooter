import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from src.const import (
    MENU_OPTION,
    MENU_TITLE_COLOR,
    MENU_TITLE_SIZE,
    C_WHITE,
    C_YELLOW,
    WIN_WIDTH_CENTER,
    MENU_OPTION_SIZE
)

class Menu:

    def __init__(self, window: Surface):
        self.window: Surface = window
        self.background: Surface = pygame.image.load('./asset/image/MenuBg.png')
        self.rect: Rect = self.background.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        # Reproduz a música do menu
        pygame.mixer_music.load('./asset/sound/Menu.mp3')
        pygame.mixer_music.play(-1)

        # Loop do menu
        while True:
            # Imprime o background
            self.window.blit(source=self.background, dest=self.rect)

            # Imprime o título
            self.menu_text(MENU_TITLE_SIZE, 'Mountain', MENU_TITLE_COLOR, (WIN_WIDTH_CENTER, 70))
            self.menu_text(MENU_TITLE_SIZE, 'Shooter', MENU_TITLE_COLOR, (WIN_WIDTH_CENTER, 120))

            # Imprime as opções do menu
            for option in MENU_OPTION:
                height = (180 + (MENU_OPTION.index(option) * 25))

                if MENU_OPTION.index(option) == menu_option:
                    self.menu_text(MENU_OPTION_SIZE, option, C_YELLOW, (WIN_WIDTH_CENTER, height))
                else:
                    self.menu_text(MENU_OPTION_SIZE, option, C_WHITE, (WIN_WIDTH_CENTER, height))

            pygame.display.flip()

            # Checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # fecha a janela
                    sys.exit() # encerra o programa

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    if event.key == pygame.K_RETURN:
                        return menu_option

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Texto
        text_font: Font    = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        # Surface do text
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # Rect de destino
        text_rect: Rect    = text_surf.get_rect(center=text_center_pos)

        self.window.blit(source=text_surf, dest=text_rect)
