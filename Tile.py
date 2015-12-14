import pygame
import random
from vector2 import Vector2 as vec2

class Tile(object):

    def __init__(self, pos, handler):
        self.handler = handler
        self.pos = pos
        if self.pos.z > 1.1:
            self.image = handler.snow_tile_image
        elif self.pos.z > .8:
            self.image = handler.rock_tile_image
        elif self.pos.z < .4:
            self.pos.z = .4
            self.image = handler.water_tile_image
        else:
            self.image = handler.base_tile_image

    def render(self, surface):
        surface.blit(self.image, 
                self.handler.camera.offset + vec2((16*self.pos.x)-(16*self.pos.y), (8*self.pos.x)+(8*self.pos.y)))#-(32*self.pos.z)))

