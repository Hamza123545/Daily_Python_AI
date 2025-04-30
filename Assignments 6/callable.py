#callable() and __call__()


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

m = Multiplier(3)
print(callable(m))  
print(m(5))         
