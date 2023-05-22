import copy
import random

class Hat():
    def __init__(self, **kwargs):
        self.contents = []
        for keys, values in kwargs.items():
            for _ in range(values):
                self.contents.append(keys)

    def draw(self, num_balls_drawn):
        balls_drawn = []
        for _ in range(num_balls_drawn):
            index = random.randrange(len(self.contents))
            balls_drawn.append(self.contents.pop(index))
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass