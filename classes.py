class Bullet:
    def __init__(self, rect, v):
        self.rect = rect
        self.v = v

class Enemy:
    def __init__(self, rect):
        self.rect = rect
        self.alive = True
        # middle y
        self.my = rect.y+1
        # side y
        self.sy = rect.y
    def move(self):
        self.rect.centery += 1
        if self.my == self.rect.centery:
            self.my = self.rect.y
            self.sy = self.rect.y+1
        else:
            self.my = self.rect.y+1
            self.sy = self.rect.y