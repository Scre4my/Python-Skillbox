class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.index = 0

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        else:
            value1 = self.lst[self.index]
            if self.index + 1 < len(self.lst):
                value2 = self.lst[self.index + 1]
            else:
                value2 = None
            self.index += 2
            return value1, value2

    def __iter__(self):
        return self
d = DoubleElement(1, 2, 3, 4, 5)
for pair in d:
    print(pair,end=" ")