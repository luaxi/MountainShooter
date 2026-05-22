"""
MountainShooter Main Game Loop
Esse módulo cria a janela do jogo e mantém o loop principal.
"""

import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da janela
window = pygame.display.set_mode(size=(600, 480))

# Loop principal
while True:
    # Checa todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
