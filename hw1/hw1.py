class Sequence(object):
    def __init__(self, array):
        self.array = array

    def __len__(self):
        return len(self.array)
    
    def __iter__(self):
        return iter(self.array)
    
    def __next__(self):
        return next(self.array)
    
    def __eq__(self, other):
        if len(self) != len(other):
            raise ValueError("Two arrays are not equal in length!")
        return sum(x == y for x, y in zip(self.array, other.array))

class Arithmetic(Sequence):
    def __init__(self, start, step):
        self.start = start
        self.step = step
        super().__init__([])

    def __call__(self, length):
        self.array = [self.start + i * self.step for i in range(length)]

class Geometric(Sequence):
    def __init__(self, start, ratio):
        self.start = start
        self.ratio = ratio
        super().__init__([])

    def __call__(self, length):
        self.array = [self.start * self.ratio ** i for i in range(length)]


if __name__ == "__main__":
    AS = Arithmetic(start=1, step=2)
    AS(length=5)
    print([n for n in AS])

    GS = Geometric(start=1, ratio=2)
    GS(length=5)
    print([n for n in GS])

    print(AS == GS)