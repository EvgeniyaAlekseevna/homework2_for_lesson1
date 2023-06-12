class CyclicIterator:
    def __init__(self, list):
        self.list = [i for i in list]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            char = self.list[self.index]
            self.index +=1
            if self.index >= len(self.list):
                self.index = 0
            return char


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)