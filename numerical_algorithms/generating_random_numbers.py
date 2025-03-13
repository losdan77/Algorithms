from datetime import datetime


class Random:
    x_o = 2

    def __init__(self, max_i, use_time=False):
        self.a = 48271
        self.b = 0
        self.m = 2**31 - 1

        if use_time:
            self.x = datetime.now().microsecond
        else:
            self.x = Random.x_o

        self.i = 0
        self.max_i = max_i

    def __next__(self):
        if self.i == self.max_i:
            raise StopIteration
        
        self.i += 1

        self.x = (self.a * self.x + self.b) % self.m
        return self.x
    
    def __iter__(self):
        return self
    

for i, random in enumerate(Random(20, True)):
    print(i + 1, random)