#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import Surface
import pygame

from src.entity import Entity
from src.entityFactory import EntityFactory

class Level:
    def __init__(self, window: Surface, name, game_mode):
        self.window: Surface = window
        self.name            = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            pygame.display.flip()
