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
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

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


### 4.7.1 关键字参数

在函数调用中，关键字参数必须跟随在位置参数的后面。传递的所有关键字参数必须与函数接受的其中一个参数匹配（比如 actor 不是函数 parrot 的有效参数），它们的顺序并不重要。这也包括非可选参数。不能对同一个参数多次赋值。下面是一个因为此限制而失败的例子:

```python
>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for keyword argument 'a'
```

当存在一个形式为 **name 的最后一个形参时，它会接收一个字典 (参见 映射类型 --- dict)，其中包含除了与已有形参相对应的关键字参数以外的所有关键字参数。 这可以与一个形式为 *name，接收一个包含除了与已有形参列表以外的位置参数的 元组 的形参 (将在下一小节介绍) 组合使用 (*name 必须出现在 **name 之前。) 例如，如果我们这样定义一个函数:

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

它会打印出：

```text
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

注意打印时关键字参数的顺序保证与调用函数时提供它们的顺序是相匹配的。


### 4.7.3 特殊参数

默认情况下，函数的参数传递形式可以是位置参数或是显式的关键字参数。 为了确保可读性和运行效率，限制允许的参数传递形式是有意义的，这样开发者只需查看函数定义即可确定参数项是仅按位置、按位置也按关键字，还是仅按关键字传递。

函数的定义看起来可以像是这样：

```text
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

在这里 / 和 * 是可选的。 如果使用这些符号则表明可以通过何种形参将参数值传递给函数：仅限位置、位置或关键字，以及仅限关键字。 关键字形参也被称为命名形参。

如果函数定义中未使用 / 和 *，则参数可以按位置或按关键字传递给函数。

在这里还可以发现更多细节，特定形参可以被标记为 仅限位置。 如果是 仅限位置 的形参，则其位置是重要的，并且该形参不能作为关键字传入。 仅限位置形参要放在 / (正斜杠) 之前。 这个 / 被用来从逻辑上分隔仅限位置形参和其它形参。 如果函数定义中没有 /，则表示没有仅限位置形参。在 / 之后的形参可以为 位置或关键字 或 仅限关键字。

要将形参标记为 仅限关键字，即指明该形参必须以关键字参数的形式传入，应在参数列表的第一个 仅限关键字 形参之前放置一个 *。

请考虑以下示例函数定义并特别注意 / 和 * 标记:

```python
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```

第一个函数定义 standard_arg 是最常见的形式，对调用方式没有任何限制，参数可以按位置也可以按关键字传入。第二个函数 pos_only_arg 在函数定义中带有 /，限制仅使用位置形参。第三个函数 kwd_only_args 在函数定义中通过 * 指明仅允许关键字参数。而最后一个则在同一函数定义中使用了全部三种调用方式。

```python
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2


>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got an unexpected keyword argument 'arg'


>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3


>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got an unexpected keyword argument 'pos_only'
```

作为指导：

* 如果你希望形参名称对用户来说不可用，则使用仅限位置形参。 这适用于形参名称没有实际意义，以及当你希望强制规定调用时的参数顺序，或是需要同时收受一些位置形参和任意关键字形参等情况。
* 当形参名称有实际意义，以及显式指定形参名称可使函数定义更易理解，或者当你想要防止用户过于依赖传入参数的位置时，则使用仅限关键字形参。
* 对于 API 来说，使用仅限位置形参可以防止形参名称在未来被修改时造成破坏性的 API 变动。


### 4.7.4 任意的参数列表

最后，最不常用的选项是可以使用任意数量的参数调用函数。这些参数会被包含在一个元组里（参见 元组和序列 ）。在可变数量的参数之前，可能会出现零个或多个普通参数。:

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

一般来说，这些 可变参数 将在形式参数列表的末尾，因为它们收集传递给函数的所有剩余输入参数。出现在 *args 参数之后的任何形式参数都是 ‘仅关键字参数’，也就是说它们只能作为关键字参数而不能是位置参数。:

```python
def concat(*args, sep="/"):
     return sep.join(args)

print(concat("earth", "mars", "venus"))
'earth/mars/venus'
print(concat("earth", "mars", "venus", sep="."))
'earth.mars.venus'
```

### 4.7.5 解包参数列表

当参数已经在列表或元组中但要为需要单独位置参数的函数调用解包时，会发生相反的情况。例如，内置的 range() 函数需要单独的 start 和 stop 参数。如果它们不能单独使用，可以使用 *-操作符 来编写函数调用以便从列表或元组中解包参数:

```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```

同样的方式，字典可使用 ** 操作符 来提供关键字参数:

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin demised", "action": "VOOM"}
>>> parrot(**d)
This parrot wouldn't VOOM if you put four million volts through it. E's bleedin demised !
```

### 4.7.6 Lambda 表达式

可以用 lambda 关键字来创建一个小的匿名函数。这个函数返回两个参数的和： lambda a, b: a+b 。Lambda函数可以在需要函数对象的任何地方使用。它们在语法上限于单个表达式。从语义上来说，它们只是正常函数定义的语法糖。与嵌套函数定义一样，lambda函数可以引用所包含域的变量:

```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
42
f(1)
43
```

上面的例子使用一个lambda表达式来返回一个函数。另一个用法是传递一个小函数作为参数:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

### 4.7.7 文档字符串

以下是有关文档字符串的内容和格式的一些约定。

第一行应该是对象目的的简要概述。为简洁起见，它不应显式声明对象的名称或类型，因为这些可通过其他方式获得（除非名称恰好是描述函数操作的动词）。这一行应以大写字母开头，以句点结尾。

如果文档字符串中有更多行，则第二行应为空白，从而在视觉上将摘要与其余描述分开。后面几行应该是一个或多个段落，描述对象的调用约定，它的副作用等。

Python 解析器不会从 Python 中删除多行字符串文字的缩进，因此处理文档的工具必须在需要时删除缩进。 这是使用以下约定完成的。 文档字符串第一行 之后 的第一个非空行确定整个文档字符串的缩进量。（我们不能使用第一行，因为它通常与字符串的开头引号相邻，因此它的缩进在字符串文字中不明显。）然后从字符串的所有行的开头剥离与该缩进 "等效" 的空格。 缩进更少的行不应该出现，但是如果它们出现，则应该剥离它们的所有前导空格。 应在转化制表符为空格后测试空格的等效性（通常转化为8个空格）。

下面是一个多行文档字符串的例子:

```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it does not do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it does not do anything.
```

### 4.7.8 函数标注

函数标注 是关于用户自定义函数中使用的类型的完全可选元数据信息（有关详情请参阅 PEP 3107 和 PEP 484 ）。

函数标注 以字典的形式存放在函数的 __annotations__ 属性中，并且不会影响函数的任何其他部分。 形参标注的定义方式是在形参名称后加上冒号，后面跟一个表达式，该表达式会被求值为标注的值。 返回值标注的定义方式是加上一个组合符号 ->，后面跟一个表达式，该标注位于形参列表和表示 def 语句结束的冒号之间。 下面的示例有一个位置参数，一个关键字参数以及返回值带有相应标注:

```python
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

### 4.8 小插曲：编码风格

现在你将要写更长，更复杂的 Python 代码，是时候讨论一下 代码风格 了。 大多数语言都能以不同的风格被编写（或更准确地说，被格式化）；有些比其他的更具有可读性。 能让其他人轻松阅读你的代码总是一个好主意，采用一种好的编码风格对此有很大帮助。

对于Python，PEP 8 已经成为大多数项目所遵循的风格指南；它促进了一种非常易读且令人赏心悦目的编码风格。每个Python开发人员都应该在某个时候阅读它；以下是为你提取的最重要的几个要点：

* 使用4个空格缩进，不要使用制表符。
* 4个空格是一个在小缩进（允许更大的嵌套深度）和大缩进（更容易阅读）的一种很好的折中方案。制表符会引入混乱，最好不要使用它。
* 换行，使一行不超过79个字符。
* 这有助于使用小型显示器的用户，并且可以在较大的显示器上并排放置多个代码文件。
* 使用空行分隔函数和类，以及函数内的较大的代码块。
* 如果可能，把注释放到单独的一行。
* 使用文档字符串。
* 在运算符前后和逗号后使用空格，但不能直接在括号内使用： a = f(1, 2) + g(3, 4)。
* 以一致的规则为你的类和函数命名；按照惯例应使用 UpperCamelCase 来命名类，而以 lowercase_with_underscores 来命名函数和方法。 始终应使用 self 来命名第一个方法参数 (有关类和方法的更多信息请参阅 初探类)。
* 如果你的代码旨在用于国际环境，请不要使用花哨的编码。Python 默认的 UTF-8 或者纯 ASCII 在任何情况下都能有最好的表现。
* 同样，哪怕只有很小的可能，遇到说不同语言的人阅读或维护代码，也不要在标识符中使用非ASCII字符。


### 5.1.3 列表推导式

列表推导式提供了一个更简单的创建列表的方法。常见的用法是把某种操作应用于序列或可迭代对象的每个元素上，然后使用其结果来创建列表，或者通过满足某些特定条件元素来创建子序列。

例如，假设我们想创建一个平方列表，像这样

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

注意这里创建（或被重写）的名为 x 的变量在for循环后仍然存在。我们可以计算平方列表的值而不会产生任何副作用

```python
squares = list(map(lambda x: x**2, range(10)))
```

或者，等价于

```python
squares = [x**2 for x in range(10)]
```

上面这种写法更加简洁易读。

列表推导式的结构是由一对方括号所包含的以下内容：一个表达式，后面跟一个 for 子句，然后是零个或多个 for 或 if 子句。 其结果将是一个新列表，由对表达式依据后面的 for 和 if 子句的内容进行求值计算而得出。 举例来说，以下列表推导式会将两个列表中不相等的元素组合起来:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

而它等价于

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

注意在上面两个代码片段中， for 和 if 的顺序是相同的。

如果表达式是一个元组（例如上面的 (x, y)），那么就必须加上括号

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

列表推导式可以使用复杂的表达式和嵌套函数

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 5.1.4 嵌套的列表推导式

列表推导式中的初始表达式可以是任何表达式，包括另一个列表推导式。

考虑下面这个 3x4的矩阵，它由3个长度为4的列表组成

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

下面的列表推导式将交换其行和列

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

如上节所示，嵌套的列表推导式是基于跟随其后的 for 进行求值的，所以这个例子等价于:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

反过来说，也等价于

```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

实际应用中，你应该会更喜欢使用内置函数去组成复杂的流程语句。 [zip()](https://docs.python.org/zh-cn/3/library/functions.html#zip) 函数将会很好地处理这种情况

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

关于本行中星号的详细说明，参见 [解包参数列表](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#tut-unpacking-arguments) 。

### 5.3 元组和序列

我们看到列表和字符串有很多共同特性，例如索引和切片操作。他们是 序列 数据类型中的两种。随着 Python 语言的发展，其他的序列类型也会被加入其中。这里介绍另一种标准序列类型: 元组。

一个元组由几个被逗号隔开的值组成，例如

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

如你所见，元组在输出时总是被圆括号包围的，以便正确表示嵌套元组。输入时圆括号可有可无，不过经常会是必须的（如果这个元组是一个更大的表达式的一部分）。给元组中的一个单独的元素赋值是不允许的，当然你可以创建包含可变对象的元组，例如列表。

虽然元组可能看起来与列表很像，但它们通常是在不同的场景被使用，并且有着不同的用途。元组是 immutable （不可变的），其序列通常包含不同种类的元素，并且通过解包（这一节下面会解释）或者索引来访问（如果是 namedtuples 的话甚至还可以通过属性访问）。列表是 mutable （可变的），并且列表中的元素一般是同种类型的，并且通过迭代访问。

一个特殊的问题是构造包含0个或1个元素的元组：为了适应这种情况，语法有一些额外的改变。空元组可以直接被一对空圆括号创建，含有一个元素的元组可以通过在这个元素后添加一个逗号来构建（圆括号里只有一个值的话不够明确）。丑陋，但是有效。例如

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

语句 t = 12345, 54321, 'hello!' 是 元组打包 的一个例子：值 12345, 54321 和 'hello!' 被打包进元组。其逆操作也是允许的

```python
>>> x, y, z = t
```

这被称为 序列解包 也是很恰当的，因为解包操作的等号右侧可以是任何序列。序列解包要求等号左侧的变量数与右侧序列里所含的元素数相同。注意多重赋值其实也只是元组打包和序列解包的组合。

### 5.4 集合

Python也包含有 集合 类型。集合是由不重复元素组成的无序的集。它的基本用法包括成员检测和消除重复元素。集合对象也支持像 联合，交集，差集，对称差分等数学运算。

花括号或 set() 函数可以用来创建集合。注意：要创建一个空集合你只能用 set() 而不能用 {}，因为后者是创建一个空字典，这种数据结构我们会在下一节进行讨论。

以下是一些简单的示例：

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

类似于 列表推导式，集合也支持推导式形式

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

### 5.5 字典

另一个非常有用的 Python 內置数据类型是 字典 (参见 映射类型 --- dict)。字典在其他语言里可能会被叫做 联合内存 或 联合数组。与以连续整数为索引的序列不同，字典是以 关键字 为索引的，关键字可以是任意不可变类型，通常是字符串或数字。如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字。但如果元组直接或间接地包含了可变对象，那么它就不能用作关键字。列表不能用作关键字，因为列表可以通过索引、切片或 append() 和 extend() 之类的方法来改变。

理解字典的最好方式，就是将它看做是一个 键: 值 对的集合，键必须是唯一的（在一个字典中）。一对花括号可以创建一个空字典：{} 。另一种初始化字典的方式是在一对花括号里放置一些以逗号分隔的键值对，而这也是字典输出的方式。

字典主要的操作是使用关键字存储和解析值。也可以用 del 来删除一个键值对。如果你使用了一个已经存在的关键字来存储值，那么之前与这个关键字关联的值就会被遗忘。用一个不存在的键来取值则会报错。

对一个字典执行 list(d) 将返回包含该字典中所有键的列表，按插入次序排列 (如需其他排序，则要使用 sorted(d))。要检查字典中是否存在一个特定键，可使用 in 关键字。

以下是使用字典的一些简单示例

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

dict() 构造函数可以直接从键值对序列里创建字典。

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

此外，字典推导式可以从任意的键值表达式中创建字典

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

当关键字是简单字符串时，有时直接通过关键字参数来指定键值对更方便

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

### 5.6 循环的技巧

当在字典中循环时，用 items() 方法可将关键字和对应的值同时取出

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

当在序列中循环时，用 [enumerate()](https://docs.python.org/zh-cn/3/library/functions.html#enumerate) 函数可以将索引位置和其对应的值同时取出

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

当同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素一一匹配。

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

当逆向循环一个序列时，先正向定位序列，然后调用 reversed() 函数

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

>>> for i in range(9, 0, -2):
...     print(i)
...
9
7
5
3
1
```

如果要按某个指定顺序循环一个序列，可以用 sorted() 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

有时可能会想在循环时修改列表内容，一般来说改为创建一个新列表是比较简单且安全的，另外一种方法是遍历浅拷贝：

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]

# 如果原列表不需要保留，则不需要声明新的列表名称 
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> for value in raw_data.copy():
...     if math.isnan(value):
...         raw_data.remove(value)
...
>>> raw_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

### 5.7 深入条件控制

while 和 if 条件句中可以使用任意操作，而不仅仅是比较操作。

比较操作符 in 和 not in 校验一个值是否在（或不在）一个序列里。操作符 is 和 is not 比较两个对象是不是同一个对象，这只对像列表这样的可变对象比较重要。所有的比较操作符都有相同的优先级，且这个优先级比数值运算符低。

比较操作可以传递。例如 a < b == c 会校验是否 a 小于 b 并且 b 等于 c。

比较操作可以通过布尔运算符 and 和 or 来组合，并且比较操作（或其他任何布尔运算）的结果都可以用 not 来取反。这些操作符的优先级低于比较操作符；在它们之中，not 优先级最高， or 优先级最低，因此 A and not B or C 等价于 (A and (not B)) or C。和之前一样，你也可以在这种式子里使用圆括号。

布尔运算符 and 和 or 也被称为 短路 运算符：它们的参数从左至右解析，一旦可以确定结果解析就会停止。例如，如果 A 和 C 为真而 B 为假，那么 A and B and C 不会解析 C。当用作普通值而非布尔值时，短路操作符的返回值通常是最后一个变量。

也可以把比较操作或者逻辑表达式的结果赋值给一个变量，例如

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

请注意 Python 与 C 不同，在表达式内部赋值必须显式地使用 [海象运算符](https://docs.python.org/zh-cn/3/faq/design.html#why-can-t-i-use-an-assignment-in-an-expression) := 来完成，需要 Python 3.8 。 这避免了 C 程序中常见的一种问题：想要在表达式中写 == 时却写成了 =。

### 5.8 序列和其它类型的比较

序列对象通常可以与相同序列类型的其他对象比较。 这种比较使用 字典式 顺序：首先比较开头的两个对应元素，如果两者不相等则比较结果就由此确定；如果两者相等则比较之后的两个元素，以此类推，直到有一个序列被耗尽。 如果要比较的两个元素本身又是相同类型的序列，则会递归地执行字典式顺序比较。 如果两个序列中所有的对应元素都相等，则两个序列也将被视为相等。 如果一个序列是另一个的初始子序列，则较短的序列就被视为较小（较少）。 对于字符串来说，字典式顺序是使用 Unicode 码位序号对单个字符排序。 下面是一些相同类型序列之间比较的例子:

```python
# 以下结果都为 true
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

注意对不同类型对象来说，只要待比较对象提供了合适的比较方法，就可以使用 < 和 > 来比较。例如，混合数值类型是通过他们的数值进行比较的，所以 0 等于 0.0，等等。否则，解释器将抛出一个 TypeError 异常，而不是随便给出一个结果。

### 6.1 有关模块的更多信息

注解 出于效率的考虑，每个模块在每个解释器会话中只被导入一次。因此，如果你更改了你的模块，则必须重新启动解释器， 或者，如果它只是一个要交互式地测试的模块，请使用 [importlib.reload()](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.reload) ，例如 import importlib; importlib.reload(modulename)。

### 6.1.1 以脚本的方式执行模块

当你用下面方式运行一个Python模块:

```shell script
python fibo.py <arguments>
```

模块里的代码会被执行，就好像你导入了模块一样，但是 \_\_name\_\_ 被赋值为 "\_\_main\_\_"。 这意味着通过在你的模块末尾添加这些代码:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

你既可以把这个文件当作脚本又可当作一个可调入的模块来使用， 因为那段解析命令行的代码只有在当模块是以“main”文件的方式执行的时候才会运行:

```shell script
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

如果模块是被导入的，那些代码是不运行的:

```python
>>> import fibo
```

这经常用于为模块提供一个方便的用户接口，或用于测试（以脚本的方式运行模块从而执行一些测试套件）。


### 6.1.3 “编译过的”Python文件

为了加速模块载入，Python在 \_\_pycache\_\_ 目录里缓存了每个模块的编译后版本，名称为 module.version.pyc ，其中名称中的版本字段对编译文件的格式进行编码； 它一般使用Python版本号。例如，在CPython版本3.3中，spam.py的编译版本将被缓存为 \_\_pycache\_\_/spam.cpython-33.pyc。此命名约定允许来自不同发行版和不同版本的Python的已编译模块共存。

一个从 .pyc 文件读出的程序并不会比它从 .py 读出时运行的更快，.pyc 文件唯一快的地方在于载入速度。


### 6.2 标准模块

Python附带了一个标准模块库，在单独的文档Python库参考（以下称为“库参考”）中进行了描述。一些模块内置于解释器中；它们提供对不属于语言核心但仍然内置的操作的访问，以提高效率或提供对系统调用等操作系统原语的访问。这些模块的集合是一个配置选项，它也取决于底层平台。例如，winreg 模块只在Windows操作系统上提供。一个特别值得注意的模块 sys，它被内嵌到每一个Python解释器中。变量 sys.ps1 和 sys.ps2 定义用作主要和辅助提示的字符串:

```python
>>>
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

这两个变量只有在编译器是交互模式下才被定义。

sys.path 变量是一个字符串列表，用于确定解释器的模块搜索路径。该变量被初始化为从环境变量 PYTHONPATH 获取的默认路径，或者如果 PYTHONPATH 未设置，则从内置默认路径初始化。你可以使用标准列表操作对其进行修改:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

### 7.1 更漂亮的输出格式

要使用 [格式化字符串字面值](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#tut-f-strings) ，请在字符串的开始引号或三引号之前加上一个 f 或 F 。在此字符串中，你可以在 { 和 } 字符之间写可以引用的变量或字面值的 Python 表达式。

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

字符串的 [str.format()](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.format) 方法需要更多的手动操作。你仍将使用 { 和 } 来标记变量将被替换的位置，并且可以提供详细的格式化指令，但你还需要提供要格式化的信息。

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

当你不需要花哨的输出而只是想快速显示某些变量以进行调试时，可以使用 repr() or str() 函数将任何值转化为字符串。

str() 函数是用于返回人类可读的值的表示，而 repr() 是用于生成解释器可读的表示（如果没有等效的语法，则会强制执行 SyntaxError）对于没有人类可读性的表示的对象， str() 将返回和 repr() 一样的值。很多值使用任一函数都具有相同的表示，比如数字或类似列表和字典的结构。特殊的是字符串有两个不同的表示。

几个例子:

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

### 7.1.1 格式化字符串文字

格式化字符串字面值 （常简称为 f-字符串）能让你在字符串前加上 f 和 F 并将表达式写成 {expression} 来在字符串中包含 Python 表达式的值。

可选的格式说明符可以跟在表达式后面。这样可以更好地控制值的格式化方式。以下示例将pi舍入到小数点后三位:

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

在 ':' 后传递一个整数可以让该字段成为最小字符宽度。这在使列对齐时很有用。:

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

其他的修饰符可用于在格式化之前转化值。 '!a' 应用 ascii() ，'!s' 应用 str()，还有 '!r' 应用 repr():

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

有关这些格式规范的参考，请参阅参考指南 [格式规格迷你语言](https://docs.python.org/zh-cn/3/library/string.html#formatspec) 。

### 7.1.2 字符串的 format() 方法

str.format() 方法的基本用法如下所示:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

花括号和其中的字符（称为格式字段）将替换为传递给 str.format() 方法的对象。花括号中的数字可用来表示传递给 str.format() 方法的对象的位置。

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

如果在 str.format() 方法中使用关键字参数，则使用参数的名称引用它们的值。:

```python
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

位置和关键字参数可以任意组合:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
```

如果你有一个非常长的格式字符串，你不想把它拆开，那么你最好是按名称而不是按位置引用变量来进行格式化。 这可以通过简单地传递字典并使用方括号 '[]' 访问键来完成。

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

这也可以通过使用 '**' 符号将 table 作为关键字参数传递。

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

这在与内置函数 vars() 结合使用时非常有用，它会返回包含所有局部变量的字典。

例如，下面几行代码生成一组整齐的列，其中包含给定的整数和它的平方以及立方:

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

关于使用 str.format() 进行字符串格式化的完整概述，请参阅 [格式字符串语法](https://docs.python.org/zh-cn/3/library/string.html#formatstrings) 。

### 7.1.4 旧的字符串格式化方法

% 运算符（求余）也可用于字符串格式化。 给定 'string' % values，则 string 中的 % 实例会以零个或多个 values 元素替换。 此操作通常被称为字符串插值。 例如:

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

可在 [printf 风格的字符串格式化](https://docs.python.org/zh-cn/3/library/stdtypes.html#old-string-formatting) 部分找到更多信息。

7.2. 读写文件
open() 返回一个 file object，最常用的有两个参数： open(filename, mode)。

```python
>>> f = open('workfile', 'w')
```

第一个参数是包含文件名的字符串。第二个参数是另一个字符串，其中包含一些描述文件使用方式的字符。mode 可以是 'r' ，表示文件只能读取，'w' 表示只能写入（已存在的同名文件会被删除），还有 'a' 表示打开文件以追加内容；任何写入的数据会自动添加到文件的末尾。'r+' 表示打开文件进行读写。mode 参数是可选的；省略时默认为 'r'。

通常文件是以 text mode 打开的，这意味着从文件中读取或写入字符串时，都会以指定的编码方式进行编码。如果未指定编码格式，默认值与平台相关 (参见 open())。在mode 中追加的 'b' 则以 binary mode 打开文件：现在数据是以字节对象的形式进行读写的。这个模式应该用于所有不包含文本的文件。

在文本模式下读取时，默认会把平台特定的行结束符 (Unix 上的 \n, Windows 上的 \r\n) 转换为 \n。在文本模式下写入时，默认会把出现的 \n 转换回平台特定的结束符。这样在幕后修改文件数据对文本文件来说没有问题，但是会破坏二进制数据例如 JPEG 或 EXE 文件中的数据。请一定要注意在读写此类文件时应使用二进制模式。

在处理文件对象时，最好使用 with 关键字。 优点是当子句体结束后文件会正确关闭，即使在某个时刻引发了异常。 而且使用 with 相比等效的 try-finally 代码块要简短得多:

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

如果你没有使用 with 关键字，那么你应该调用 f.close() 来关闭文件并立即释放它使用的所有系统资源。如果你没有显式地关闭文件，Python的垃圾回收器最终将销毁该对象并为你关闭打开的文件，但这个文件可能会保持打开状态一段时间。另外一个风险是不同的Python实现会在不同的时间进行清理。

通过 with 语句或者调用 f.close() 关闭文件对象后，尝试使用该文件对象将自动失败。:

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 8.3 处理异常

try ... except 语句有一个可选的 else 子句，在使用时必须放在所有的 except 子句后面。对于在try 子句不引发异常时必须执行的代码来说很有用。例如:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

使用 else 子句比向 try 子句添加额外的代码要好，因为它避免了意外捕获由 try ... except 语句保护的代码未引发的异常。

发生异常时，它可能具有关联值，也称为异常 参数 。参数的存在和类型取决于异常类型。

except 子句可以在异常名称后面指定一个变量。这个变量和一个异常实例绑定，它的参数存储在 instance.args 中。为了方便起见，异常实例定义了 __str__() ，因此可以直接打印参数而无需引用 .args 。也可以在抛出之前首先实例化异常，并根据需要向其添加任何属性。:

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

### 8.6 定义清理操作

try 语句有另一个可选子句，用于定义必须在所有情况下执行的清理操作。例如:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

如果存在 finally 子句，则 finally 子句将作为 try 语句结束前的最后一项任务被执行。 finally 子句不论 try 语句是否产生了异常都会被执行。 以下几点讨论了当异常发生时一些更复杂的情况：

1. 如果在执行 try 子句期间发生了异常，该异常可由一个 except 子句进行处理。 如果异常没有被某个 except 子句所处理，则该异常会在 finally 子句执行之后被重新引发。
2. 异常也可能在 except 或 else 子句执行期间发生。 同样地，该异常会在 finally 子句执行之后被重新引发。
3. 如果在执行 try 语句时遇到一个 break, continue 或 return 语句，则 finally 子句将在执行 break, continue 或 return 语句之前被执行。
4. 如果 finally 子句中包含一个 return 语句，则返回值将来自 finally 子句的某个 return 语句的返回值，而非来自 try 子句的 return 语句的返回值。

例如

```python
def bool_return():
    try:
        return True
    finally:
        return False

bool_return()
False
```

一个更为复杂的例子:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

正如你所看到的，finally 子句在任何情况下都会被执行。 两个字符串相除所引发的 TypeError 不会由 except 子句处理，因此会在 finally 子句执行后被重新引发。

在实际应用程序中，finally 子句对于释放外部资源（例如文件或者网络连接）非常有用，无论是否成功使用资源。

### 8.7 预定义的清理操作

某些对象定义了在不再需要该对象时要执行的标准清理操作，无论使用该对象的操作是成功还是失败。请查看下面的示例，它尝试打开一个文件并把其内容打印到屏幕上。:

```python
for line in open("myfile.txt"):
    print(line, end="")
```

这个代码的问题在于，它在这部分代码执行完后，会使文件在一段不确定的时间内处于打开状态。这在简单脚本中不是问题，但对于较大的应用程序来说可能是个问题。 with 语句允许像文件这样的对象能够以一种确保它们得到及时和正确的清理的方式使用。:

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

执行完语句后，即使在处理行时遇到问题，文件 f 也始终会被关闭。和文件一样，提供预定义清理操作的对象将在其文档中指出这一点。

### 9.2.1 作用域和命名空间示例

这个例子演示了如何引用不同作用域和名称空间，以及 global 和 nonlocal 会如何影响变量绑定:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

示例代码的输出是：

```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

请注意 局部 赋值（这是默认状态）不会改变 scope_test 对 spam 的绑定。 nonlocal 赋值会改变 scope_test 对 spam 的绑定，而 global 赋值会改变模块层级的绑定。

您还可以在 global 赋值之前看到之前没有 spam 的绑定。


### 9.4 补充说明

数据属性可以被方法以及一个对象的普通用户（“客户端”）所引用。 换句话说，类不能用于实现纯抽象数据类型。 实际上，在 Python 中没有任何东西能强制隐藏数据 --- 它是完全基于约定的。 （而在另一方面，用 C 语言编写的 Python 实现则可以完全隐藏实现细节，并在必要时控制对象的访问；此特性可以通过用 C 编写 Python 扩展来使用。）

### 9.5.1 多重继承

Python也支持一种多重继承。 带有多个基类的类定义语句如下所示:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

对于多数应用来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左至右的，当层次结构中存在重叠时不会在同一个类中搜索两次。 因此，如果某一属性在 DerivedClassName 中未找到，则会到 Base1 中搜索它，然后（递归地）到 Base1 的基类中搜索，如果在那里未找到，再到 Base2 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 super() 的协同调用。 这种方式在某些其他多重继承型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。

动态改变顺序是有必要的，因为所有多重继承的情况都会显示出一个或更多的菱形关联（即至少有一个父类可通过多条路径被最底层类所访问）。 例如，所有类都是继承自 object，因此任何多重继承的情况都提供了一条以上的路径可以通向 object。 为了确保基类不会被访问一次以上，动态算法会用一种特殊方式将搜索顺序线性化， 保留每个类所指定的从左至右的顺序，只调用每个父类一次，并且保持单调（即一个类可以被子类化而不影响其父类的优先顺序）。 总而言之，这些特性使得设计具有多重继承的可靠且可扩展的类成为可能。 要了解更多细节，请参阅 [The Python 2.3 Method Resolution Order](https://www.python.org/download/releases/2.3/mro/) 。


### 9.6 私有变量

那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。 但是，大多数 Python 代码都遵循这样一个约定：带有一个下划线的名称 (例如 _spam) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。 这应当被视为一个实现细节，可能不经通知即加以改变。

由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 名称改写。 任何形式为 __spam 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 _classname__spam，其中 classname 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。

名称改写有助于让子类重载方法而不破坏类内方法调用。例如:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

上面的示例即使在 MappingSubclass 引入了一个 __update 标识符的情况下也不会出错，因为它会在 Mapping 类中被替换为 _Mapping__update 而在 MappingSubclass 类中被替换为 _MappingSubclass__update。

请注意，改写规则的设计主要是为了避免意外冲突；访问或修改被视为私有的变量仍然是可能的。这在特殊情况下甚至会很有用，例如在调试器中。

请注意传递给 exec() 或 eval() 的代码不会将发起调用类的类名视作当前类；这类似于 global 语句的效果，因此这种效果仅限于同时经过字节码编译的代码。 同样的限制也适用于 getattr(), setattr() 和 delattr()，以及对于 __dict__ 的直接引用。


### 9.10 生成器表达式

某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，将外层为圆括号而非方括号。 这种表达式被设计用于生成器将立即被外层函数所使用的情况。 生成器表达式相比完整的生成器更紧凑但较不灵活，相比等效的列表推导式则更为节省内存。

示例:

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```


### 10.5 字符串模式匹配

re 模块为高级字符串处理提供正则表达式工具。对于复杂的匹配和操作，正则表达式提供简洁，优化的解决方案:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']

# 注意 (\b[a-z]+) \1 中 \1 前面必须有一个空格
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

### 10.6 数学

random 模块提供了进行随机选择的工具:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

statistics 模块计算数值数据的基本统计属性（均值，中位数，方差等）:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

[SciPy项目](https://scipy.org) 有许多其他模块用于数值计算。

### 10.8 日期和时间

datetime 模块提供了以简单和复杂的方式操作日期和时间的类。虽然支持日期和时间算法，但实现的重点是有效的成员提取以进行输出格式化和操作。该模块还支持可感知时区的对象。

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

### 10.9 数据压缩

常见的数据存档和压缩格式由模块直接支持，包括：zlib, gzip, bz2, lzma, zipfile 和 tarfile。:

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

### 10.10 性能测量

一些Python用户对了解同一问题的不同方法的相对性能产生了浓厚的兴趣。 Python提供了一种可以立即回答这些问题的测量工具。

例如，元组封包和拆包功能相比传统的交换参数可能更具吸引力。timeit 模块可以快速演示在运行效率方面一定的优势:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

与 timeit 的精细粒度级别相反， profile 和 pstats 模块提供了用于在较大的代码块中识别时间关键部分的工具。


### 10.11 质量控制

开发高质量软件的一种方法是在开发过程中为每个函数编写测试，并在开发过程中经常运行这些测试。

doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。测试构造就像将典型调用及其结果剪切并粘贴到文档字符串一样简单。这通过向用户提供示例来改进文档，并且它允许doctest模块确保代码保持对文档的真实:

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

unittest 模块不像 doctest 模块那样易于使用，但它允许在一个单独的文件中维护更全面的测试集:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```


### 11.2 模板

string 模块包含一个通用的 Template 类，具有适用于最终用户的简化语法。它允许用户在不更改应用逻辑的情况下定制自己的应用。

上述格式化操作是通过占位符实现的，占位符由 $ 加上合法的 Python 标识符（只能包含字母、数字和下划线）构成。一旦使用花括号将占位符括起来，就可以在后面直接跟上更多的字母和数字而无需空格分割。$$ 将被转义成单个字符 $:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

如果在字典或关键字参数中未提供某个占位符的值，那么 substitute() 方法将抛出 KeyError。对于邮件合并类型的应用，用户提供的数据有可能是不完整的，此时使用 safe_substitute() 方法更加合适 —— 如果数据缺失，它会直接将占位符原样保留。

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

Template 的子类可以自定义定界符。例如，以下是某个照片浏览器的批量重命名功能，采用了百分号作为日期、照片序号和照片格式的占位符:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

模板的另一个应用是将程序逻辑与多样的格式化输出细节分离开来。这使得对 XML 文件、纯文本报表和 HTML 网络报表使用自定义模板成为可能。


### 11.6 弱引用

Python 会自动进行内存管理（对大多数对象进行引用计数并使用 garbage collection 来清除循环引用）。 当某个对象的最后一个引用被移除后不久就会释放其所占用的内存。

此方式对大多数应用来说都适用，但偶尔也必须在对象持续被其他对象所使用时跟踪它们。 不幸的是，跟踪它们将创建一个会令其永久化的引用。 weakref 模块提供的工具可以不必创建引用就能跟踪对象。 当对象不再需要时，它将自动从一个弱引用表中被移除，并为弱引用对象触发一个回调。 典型应用包括对创建开销较大的对象进行缓存:

```python
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python38/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

### 14.1 Tab 补全和编辑历史

在解释器启动的时候，补全变量和模块名的功能将 自动打开，以便在按下 Tab 键的时候调用补全函数。它会查看 Python 语句名称，当前局部变量和可用的模块名称。处理像 string.a 的表达式，它会求值在最后一个 '.' 之前的表达式，接着根据求值结果对象的属性给出补全建议。如果拥有 __getattr__() 方法的对象是表达式的一部分，注意这可能会执行程序定义的代码。默认配置下会把编辑历史记录保存在用户目录下名为 .python_history 的文件。在下一次 Python 解释器会话期间，编辑历史记录仍旧可用。

























