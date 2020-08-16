# The Python Standard Library

根据 [Python 标准库](https://docs.python.org/3/library/index.html) 练习 Python3。

## [内置函数](https://docs.python.org/zh-cn/3/library/functions.html)

Python 解释器内置了很多函数和类型，您可以在任何时候使用它们。以下按字母表顺序列出它们。

## [内置类型](https://docs.python.org/zh-cn/3/library/stdtypes.html)

主要内置类型有数字、序列、映射、类、实例和异常。

有些多项集类是可变的。 它们用于添加、移除或重排其成员的方法将原地执行，并不返回特定的项，绝对不会返回多项集实例自身而是返回 None。

### 字典演示

作为演示，以下示例返回的字典均等于 {"one": 1, "two": 2, "three": 3}:

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
```

