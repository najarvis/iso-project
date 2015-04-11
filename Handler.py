import pygame
import Camera
import Tile
from vector3 import Vector3 as vec3
import random

class Handler(object):

    def __init__(self, ss):
        self.ss = ss
        self.camera = Camera.Camera(self)
        self.camera.offset.x = self.ss[0]/2
        
        self.rock_tile_image = pygame.image.load("res/RockIso.png").convert()
        self.base_tile_image = pygame.image.load("res/BaseIso.png").convert()
        self.rock_tile_image.set_colorkey((255, 0, 255))
        self.base_tile_image.set_colorkey((255, 0, 255))

        self.tiles = []
        for i in range(10):
            for j in range(10):
                self.tiles.append(Tile.Tile(vec3(j,i,random.randint(0,2)/20.0), self))

    def render(self, surface):
        for TILE in self.tiles:
            TILE.render(surface)
