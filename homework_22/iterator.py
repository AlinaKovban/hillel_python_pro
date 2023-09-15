class MyMap:

    class MyMapIter:

        def __init__(self, iterable_key, iterable_value, function1, function2):
            self._iterable_key = iterable_key
            self._iterable_value = iterable_value
            self._function1 = function1
            self._function2 = function2
            self._pointer = 0

        def __next__(self):
            if self._pointer == len(self._iterable_key):
                raise StopIteration
            result_function1 = self._function1(list(self._iterable_key)[self._pointer])
            result_function2 = self._function2(list(self._iterable_value)[self._pointer])
            result = {result_function1: result_function2}
            self._pointer += 1
            return result

    def __init__(self, iterable, function1, function2):
        self._iterable_key = iterable.keys()
        self._iterable_value = iterable.values()
        self._function1 = function1
        self._function2 = function2

    def __iter__(self):
        return self.MyMapIter(self._iterable_key, self._iterable_value, self._function1, self._function2)
