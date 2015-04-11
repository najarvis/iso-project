import math

class Vector3(tuple):

    def __new__(typ, x=1.0, y=1.0, z=1.0):
        n = tuple.__new__(typ, (int(x), int(y), int(z)))
        n.x = x
        n.y = y
        n.z = z
        return n

    def __mul__(self, other):
        return Vector3(self.x*other, self.y*other, self.z*other)

    def __add__(self, other):
        return self.__new__(type(self), self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __str__(self):
        return "(%s, %s, %s)"%(self.x, self.y, self.z)

    @staticmethod
    def from_points(P1, P2):
        return Vector3( P2[0] - P1[0], P2[1] - P1[1] )

    def get_magnitude(self): #Magnitude is distance
        return math.sqrt( self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude

    #rhs stands for right hand side

    def __sub__(self, rhs):
        return Vector3(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __div__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar, self.z/ scalar)

