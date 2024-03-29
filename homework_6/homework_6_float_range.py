class Frange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
            self.step = 1
        else:
            self.start = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        range_perfom = self.start
        if self.step > 0:
            while range_perfom < self.stop:
                yield range_perfom
                range_perfom += self.step
        elif self.step < 0:
            while range_perfom > self.stop:
                yield range_perfom
                range_perfom += self.step
        else:
            return "Step can not be 0"


for i in Frange(1, 100, 3.5):
    print(i)


assert (list(Frange(5)) == [0, 1, 2, 3, 4])
assert (list(Frange(2, 5)) == [2, 3, 4])
assert (list(Frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(Frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(Frange(1, 5)) == [1, 2, 3, 4])
assert (list(Frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(Frange(0, 0)) == [])
assert (list(Frange(100, 0)) == [])

print("SUCCESS!")
