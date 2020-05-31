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

### 4.4 break 和 continue 语句，以及循环中的 else 子句 

循环语句可能带有 else 子句；它会在循环耗尽了可迭代对象 (使用 for) 或循环条件变为假值 (使用 while) 时被执行，但不会在循环被 break 语句终止时被执行。 以下搜索素数的循环就是这样的一个例子:\

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

（是的，这是正确的代码。仔细看： else 子句属于 for 循环， 不属于 if 语句。）

当和循环一起使用时，else 子句与 try 语句中的 else 子句的共同点多于 if 语句中的同类子句: try 语句中的 else 子句会在未发生异常时执行，而循环中的 else 子句则会在未发生 break 时执行。


### 4.5 pass 语句

pass 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它。例如:

```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

这通常用于创建最小的类:

```python
>>> class MyEmptyClass:
...     pass
...
```

pass 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，允许你保持在更抽象的层次上进行思考。 pass 会被静默地忽略:

```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```


### 4.6 定义函数

我们可以创建一个输出任意范围内 Fibonacci 数列的函数:

```python
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

在函数被调用时，实际参数（实参）会被引入被调用函数的本地符号表中；因此，实参是通过 按值调用 传递的（其中 值 始终是对象 引用 而不是对象的值）。当一个函数调用另外一个函数时，将会为该调用创建一个新的本地符号表。

函数定义会把函数名引入当前的符号表中。函数名称的值具有解释器将其识别为用户定义函数的类型。这个值可以分配给另一个名称，该名称也可以作为一个函数使用。这用作一般的重命名机制:

```python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```


### 4.7.1 参数默认值

默认值是在 定义过程 中在函数定义处计算的，所以：

```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```

会打印 5。

**重要警告**： 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。比如，下面的函数会存储在后续调用中传递给它的参数:

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

[1]
[1, 2]
[1, 2, 3]
```

如果你不想要在后续调用之间共享默认值，你可以这样写这个函数:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```











































