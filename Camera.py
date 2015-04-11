from vector2 import Vector2 as vec2


class Camera(object):
    
    def __init__(self, handler):
        self.handler = handler
        self.offset = vec2()
