from collections import OrderedDict

d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(''.join(d.keys()))  # acdeb

# move_to_end:
#   Move an existing element to the end (or beginning if last is false).
#   Raise KeyError if the element does not exist.
d.move_to_end('b', last=False)
print(''.join(d.keys()))  # bacde


class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


