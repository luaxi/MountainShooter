import pygame

from src.const import WIN_WIDTH, WIN_HEIGHT
from src.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        # Loop principal
        while True:
            menu = Menu(self.window)
            menu.run()
