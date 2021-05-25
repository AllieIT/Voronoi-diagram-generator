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

    def dist(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2

    
x_size = 512
y_size = 512

size = 20

data = np.zeros((x_size, y_size, 3), dtype=np.uint8)
points = []
for i in range(size):
    p = Point(random.randint(0, x_size), random.randint(0, y_size), [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    points.append(p)

for x in range(x_size):
    for y in range(y_size):
        dist = []
        for point in points:
            dist.append(point.dist(x, y))
        i = dist.index(min(dist))
        data[x, y] = points[i].color

for point in points:
    data[point.x - 1, point.y - 1] = [0, 0, 0]
    data[point.x - 1, point.y] = [0, 0, 0]
    data[point.x - 1, point.y + 1] = [0, 0, 0]
    data[point.x, point.y - 1] = [0, 0, 0]
    data[point.x, point.y] = [0, 0, 0]
    data[point.x, point.y + 1] = [0, 0, 0]
    data[point.x + 1, point.y - 1] = [0, 0, 0]
    data[point.x + 1, point.y] = [0, 0, 0]
    data[point.x + 1, point.y + 1] = [0, 0, 0]

image = Image.fromarray(data)
image.show()