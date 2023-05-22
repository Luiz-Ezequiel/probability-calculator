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
        if num_balls_drawn > len(self.contents):
            return self.contents
        for _ in range(num_balls_drawn):
            index = self.contents.pop(random.choice(range(len(self.contents))))
            balls_drawn.append(index)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        balls_gotten = hat_copy.draw(num_balls_drawn)
        
        for color in balls_gotten:
            if color in expected_copy:
                expected_copy[color]-= 1

        if all(x <= 0 for x in expected_copy.values()):
            m += 1

    return m / num_experiments