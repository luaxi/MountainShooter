import pygame
from src.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):

        # Loop principal
        while True:
            menu = Menu(self.window)
            menu.run()

            # Checa todos os eventos
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
