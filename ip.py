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
        self.delta = (-self.delta[1], self.delta[0])

    def rotatecc(self):
        self.delta = (self.delta[1], -self.delta[0])

    def setmode(self, m):
        self.mode = m
