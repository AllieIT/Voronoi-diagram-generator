import numpy as np
import random
from PIL import Image


class Point:
    x = 0
    y = 0
    color = [0, 0, 0]

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    # This can be modified
    def dist(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2


class VoronoiGenerator:

    SIZE = (512, 512)

    def __init__(self, no_points=20):
        self.no_points = no_points

    def generate(self):
        data = np.zeros((self.SIZE[0], self.SIZE[1], 3), dtype=np.uint8)
        points = []
        # Create central points
        for i in range(self.no_points):
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            p = Point(random.randint(0, self.SIZE[0]), random.randint(0, self.SIZE[1]), color)
            points.append(p)

        # Iterate over board and set color
        for x in range(self.SIZE[0]):
            for y in range(self.SIZE[1]):
                dist = []
                for point in points:
                    dist.append(point.dist(x, y))
                i = dist.index(min(dist))
                data[x, y] = points[i].color

        # Create black points
        for point in points:
            for x_off in [-1, 0, 1]:
                for y_off in [-1, 0, 1]:
                    data[point.x + x_off, point.y + y_off] = [0, 0, 0]

        return data


def main():
    generator = VoronoiGenerator(40)
    data = generator.generate()
    image = Image.fromarray(data)
    image.show()

main()