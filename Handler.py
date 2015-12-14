import pygame
import Camera
import Tile
from vector3 import Vector3 as vec3
import random
import VoronoiMapGen as vmg
import midpointDisplacement as md

class Handler(object):

    def __init__(self, ss):
        self.ss = ss
        self.camera = Camera.Camera(self)
        self.camera.offset.x = self.ss[0]/2
        
        self.rock_tile_image = pygame.image.load("res/RockIso.png").convert()
        self.base_tile_image = pygame.image.load("res/BaseIso.png").convert()
        self.water_tile_image = pygame.image.load("res/WaterIso.png").convert()
        self.snow_tile_image = pygame.image.load("res/SnowIso.png").convert()
        self.rock_tile_image.set_colorkey((255, 0, 255))
        self.base_tile_image.set_colorkey((255, 0, 255))
        self.water_tile_image.set_colorkey((255, 0, 255))
        self.snow_tile_image.set_colorkey((255, 0, 255))


        self.world_size = (32, 32)
        self.map_generator = md.terrain(5, 1)
        self.map_generator.generate(.5)
        #print len(self.map_generator.map)
        #self.map_array = self.map_generator.whole_new(20, self.world_size)

        max_height = 0

        self.tiles = []
        for i in range(self.world_size[0]):
            previous_offset = 0.0
            for j in range(self.world_size[1]):
                #previous_offset += random.randint(-2,2)/40.0
                previous_offset = self.map_generator.map[i][j] / 16.0
                max_height = max(previous_offset, max_height)
                self.tiles.append(Tile.Tile(vec3(i,j,previous_offset), self))

        print max_height

    def render(self, surface):
        for TILE in self.tiles:
            TILE.render(surface)
