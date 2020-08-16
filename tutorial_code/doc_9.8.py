class Reverse:
    """Iterator for looping over a sequence backward."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]


if __name__ == '__main__':
    rev = Reverse('Spam')
    for char in rev:
        print(char)

"""
m
a
p
S
"""
