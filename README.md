# Python Tutorial

根据 [官网教程](https://docs.python.org/3/tutorial/) 练习 Python3。

## Tips

### 3.1.2 字符串

如果你不希望前置了 \ 的字符转义成特殊字符，可以使用 原始字符串 方式，在引号前添加 r 即可:

```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

字符串字面值可以跨行连续输入。一种方式是用三重引号："""...""" 或 '''...'''。字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可。

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起，把很长的字符串拆开分别输入的时候尤其有用。只能对两个字面值这样操作，变量或表达式不行，如果你想连接变量，或者连接变量和字面值，可以用 + 号:

```python
>>> 'Py' 'thon'
'Python'

>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

字符串是可以被 索引 （下标访问）的，第一个字符索引是 0。单个字符并没有特殊的类型，只是一个长度为一的字符串（So it's not char in java）:

```python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```

注意切片的开始总是被包括在结果中，而结束不被包括。这使得 s\[:i\] + s\[i:\] 总是等于 s，切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束:

```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```

使用过大的索引会产生一个错误，但是，切片中的越界索引会被自动处理:

```python
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

>>> word[4:42]
'on'
>>> word[42:]
''
```

### 3.1.3 列表

所有的切片操作都返回一个包含所请求元素的新列表。 这意味着以下切片操作会返回列表的一个 浅拷贝:

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> aaa = squares
>>> bbb = squares[:]
>>> squares[0] = 10000
>>> squares
[10000, 4, 9, 16, 25]
>>> aaa
[10000, 4, 9, 16, 25]
>>> bbb
[1, 4, 9, 16, 25]
```

给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

### 3.2 走向编程的第一步

交互式命令行里，当一个组合的语句输入时, 需要在最后敲一个空白行表示完成（因为语法分析器猜不出来你什么时候打的是最后一行）。

```python
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```

### 4.3 range() 函数

要以序列的索引来迭代，您可以将 range() 和 len() 组合如下:

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

如果你只打印 range，会出现奇怪的结果:

```python
>>> print(range(10))
range(0, 10)
```

range() 所返回的对象在许多方面表现得像一个列表，但实际上却并不是。此对象会在你迭代它时基于所希望的序列返回连续的项，但它没有真正生成列表，这样就能节省空间。我们称这样对象为 iterable，也就是说，适合作为这样的目标对象：函数和结构期望从中获取连续的项直到所提供的项全部耗尽。 我们已经看到 for 语句就是这样一种结构，而接受可迭代对象的函数的一个例子是 sum():

```python
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```

稍后我们将看到更多返回可迭代对象以及将可迭代对象作为参数的函数。 最后，也许你会很好奇如何从一个指定范围内获取一个列表。 以下是解决方案：

```python
>>> list(range(4))
[0, 1, 2, 3]
```






















