from math import sin, cos


def rotate(vector, theta):
    rotmatrix = [[cos(theta), -sin(theta)],
                 [sin(theta), cos(theta)]]
    zip_rm = zip(rotmatrix)
    zip_rm = list(zip_rm)
    return tuple([round(elem) for elem in [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
                                            for col_b in zip_rm] for row_a in vector]])

class IP:
    def __init__(self, x, y, delta):
        self.x = x
        self.y = y
        assert type(delta) == tuple and len(delta) == 2
        self.delta = delta
        self.mode = 'main'

    def step(self):
        self.x += self.delta[0]
        self.y += self.delta[1]

    def backstep(self):
        self.x -= self.delta[0]
        self.y -= self.delta[1]

    def rotatec(self):
        self.delta = rotate(self.delta[1], -90)

    def rotatecc(self):
        self.delta = rotate(self.delta, 90)

    def setmode(self, m):
        self.mode = m
