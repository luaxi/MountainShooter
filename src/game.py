import sys
import pygame

from src.const import WIN_WIDTH, WIN_HEIGHT
from src.menu import Menu
from src.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        # Loop principal
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            match menu_return:
                case 0 | 1 | 2: # 'NEW GAME'
                    level = Level(window=self.window, name='Level1', game_mode=menu_return)
                    level_return = level.run()

                case 4: # 'EXIT'
                    pygame.quit()
                    sys.exit()

                case _:
                    pass
