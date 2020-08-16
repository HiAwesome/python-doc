from collections import namedtuple

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)  # instantiate with positional or keyword arguments
print(p[0] + p[1])  # indexable like the plain tuple (11, 22)
# 33
x, y = p  # unpack like a regular tuple
print(x, y)
# (11, 22)
print(p.x + p.y)  # fields also accessible by name
# 33
print(p)  # readable __repr__ with a name=value style
Point(x=11, y=22)

# classmethod somenamedtuple._make(iterable) 类方法从存在的序列或迭代实例创建一个新实例。
t = [33, 44]
c = Point._make(t)
print(c)  # Point(x=33, y=44)

# somenamedtuple._asdict() 返回一个新的 dict ，它将字段名称映射到它们对应的值：
p = Point(x=11, y=22)
print(p._asdict())  # {'x': 11, 'y': 22}
