import gc
import weakref


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a

print(d['primary'])

del a
print(gc.collect())

try:
    print(d['primary'])
except KeyError as e:
    assert str(e) == "'primary'"

"""
10
8
"""
