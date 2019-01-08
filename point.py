import math


class Point(object):
    def __init__(self, x=0, y=0, z=0, coords=None):
        if coords:
            self.coords = coords
        else:
            self.coords = [x, y, z]

    @property
    def x(self):
        return self.coords[0]

    @property
    def dimension(self):
        dimension = len(self.coords)
        return dimension

    def distance_to(self, other):
        sum_squares = 0

        if self.dimension != other.dimension:
            raise DimensionMismatch

        for x1, x2 in zip(self.coords, other.coords):
            sum_squares += (x1 - x2)**2

        return math.sqrt(sum_squares)


class DimensionMismatch(Exception):
    pass
