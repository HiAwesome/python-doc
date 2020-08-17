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

## [内置异常](https://docs.python.org/zh-cn/3/library/exceptions.html)

下面列出的内置异常可通过解释器或内置函数来生成。除非另有说明，它们都会具有一个提示导致错误详细原因的“关联值”。 这可以是一个字符串或由多个信息项（例如一个错误码和一个解释错误的字符串）组成的元组。 关联值通常会作为参数被传递给异常类的构造器。

用户代码可以引发内置异常。 这可被用于测试异常处理程序或报告错误条件，“就像” 在解释器引发了相同异常的情况时一样；但是请注意，没有任何机制能防止用户代码引发不适当的错误。

不论在哪种情况下，异常本身总会在任何串连异常之后显示，以便回溯的最后一行总是显示所引发的最后一个异常。

## [文本处理服务](https://docs.python.org/zh-cn/3/library/text.html)

本章介绍的模块提供了广泛的字符串操作和其他文本处理服务。

### [string 常见的字符串操作](https://docs.python.org/zh-cn/3/library/string.html)

本章主要介绍了字符串常量、自定义字符串格式化、格式字符串语法、模板字符串、辅助函数。

### [re 正则表达式操作](https://docs.python.org/zh-cn/3/library/re.html)

这个模块提供了与 Perl 语言类似的正则表达式匹配操作。

## [数据类型](https://docs.python.org/zh-cn/3/library/datatypes.html)

本章所描述的模块提供了许多专门的数据类型，如日期和时间、固定类型的数组、堆队列、双端队列、以及枚举。

Python也提供一些内置数据类型，特别是，dict、 list、set、frozenset、以及 tuple。str 这个类是用来存储Unicode字符串的，而 bytes 和 bytearray 这两个类是用来存储二进制数据的。

### [datetime 基本的日期和时间类型](https://docs.python.org/zh-cn/3/library/datetime.html)

datetime 模块提供用于处理日期和时间的类。

在支持日期时间数学运算的同时，实现的关注点更着重于如何能够更有效地解析其属性用于格式化输出和数据操作。

### [calendar 日历相关函数](https://docs.python.org/zh-cn/3/library/calendar.html)

这个模块让你可以输出像 Unix cal 那样的日历，它还提供了其它与日历相关的实用函数。 默认情况下，这些日历把星期一当作一周的第一天，星期天为一周的最后一天（按照欧洲惯例）。 可以使用 setfirstweekday() 方法设置一周的第一天为星期天 (6) 或者其它任意一天。 使用整数作为指定日期的参数。 更多相关的函数，参见 datetime 和 time 模块。

在这个模块中定义的函数和类都基于一个理想化的日历，现行公历向过去和未来两个方向无限扩展。这与 Dershowitz 和 Reingold 的书 "历法计算" 中所有计算的基本日历 -- "proleptic Gregorian" 日历的定义相符合。 ISO 8601标准还规定了 0 和 负数年份。0年指公元前1年， -1年指公元前2年，依此类推。

### [collections 容器数据类型](https://docs.python.org/zh-cn/3/library/collections.html)

这个模块实现了特定目标的容器，以提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择。

#### ChainMap 对象

一个 ChainMap 类是为了将多个映射快速的链接到一起，这样它们就可以作为一个单元处理。它通常比创建一个新字典和多次调用 update() 要快很多。

这个类可以用于模拟嵌套作用域，并且在模版化的时候比较有用。

#### Counter 对象

一个计数器工具提供快速和方便的计数。

#### deque 对象

Deque 队列是由栈或者 queue 队列生成的（发音是 “deck”，”double-ended queue”的简称）。Deque 支持线程安全，内存高效添加(append)和弹出(pop)，从两端都可以，两个方向的大概开销都是 O(1) 复杂度。

虽然 list 对象也支持类似操作，不过这里优化了定长操作和 pop(0) 和 insert(0, v) 的开销。它们引起 O(n) 内存移动的操作，改变底层数据表达的大小和位置。

如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。限定长度deque提供类似Unix filter tail 的功能。它们同样可以用与追踪最近的交换和其他数据池活动。

#### defaultdict 对象

defaultdict 是内置 dict 类的子类。它重载了一个方法并添加了一个可写的实例变量。其余的功能与 dict 类相同，此处不再重复说明。

本对象包含一个名为 default_factory 的属性，构造时，第一个参数用于为该属性提供初始值，默认为 None。所有其他参数（包括关键字参数）都相当于传递给 dict 的构造函数。

#### namedtuple() 命名元组的工厂函数

命名元组赋予每个位置一个含义，提供可读性和自文档性。它们可以用于任何普通元组，并添加了通过名字获取值的能力，通过索引值也是可以的。

#### OrderedDict 对象

有序词典就像常规词典一样，但有一些与排序操作相关的额外功能。由于内置的 dict 类获得了记住插入顺序的能力（在 Python 3.7 中保证了这种新行为），它们变得不那么重要了。

一些与 dict 的不同仍然存在：
* 常规的 dict 被设计为非常擅长映射操作。 跟踪插入顺序是次要的。
* OrderedDict 旨在擅长重新排序操作。 空间效率、迭代速度和更新操作的性能是次要的。
* 算法上， OrderedDict 可以比 dict 更好地处理频繁的重新排序操作。 这使其适用于跟踪最近的访问（例如在 LRU cache 中）。
* 对于 OrderedDict ，相等操作检查匹配顺序。
* OrderedDict 类的 popitem() 方法有不同的签名。它接受一个可选参数来指定弹出哪个元素。
* OrderedDict 类有一个 move_to_end() 方法，可以有效地将元素移动到任一端。
* Python 3.8之前， dict 缺少 __reversed__() 方法。

### [heapq 堆队列算法](https://docs.python.org/zh-cn/3/library/heapq.html)

这个模块提供了堆队列算法的实现，也称为优先队列算法。

堆是一个二叉树，它的每个父节点的值都只会小于或大于所有孩子节点（的值）。它使用了数组来实现：从零开始计数，对于所有的 k ，都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]。 为了便于比较，不存在的元素被认为是无限大。 堆最有趣的特性在于最小的元素总是在根结点：heap[0]。

这个API与教材的堆算法实现有所不同，具体区别有两方面：（a）我们使用了从零开始的索引。这使得节点和其孩子节点索引之间的关系不太直观但更加适合，因为 Python 使用从零开始的索引。 （b）我们的 pop 方法返回最小的项而不是最大的项（这在教材中称为“最小堆”；而“最大堆”在教材中更为常见，因为它更适用于原地排序）。

基于这两方面，把堆看作原生的Python list也没什么奇怪的： heap[0] 表示最小的元素，同时 heap.sort() 维护了堆的不变性！

要创建一个堆，可以使用list来初始化为 [] ，或者你可以通过一个函数 heapify() ，来把一个list转换成堆。

Python 提供的是最小堆，如果需要最大堆目前的主流方案是给每个元素乘负一，取值的时候再乘负一，参考 [What do I use for a max-heap implementation in Python?](https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python) 和 [Max Heap in Python](https://www.geeksforgeeks.org/max-heap-in-python/).

### [bisect 数组二分查找算法](https://docs.python.org/zh-cn/3/library/bisect.html)

这个模块对有序列表提供了支持，使得他们可以在插入新数据仍然保持有序。对于长列表，如果其包含元素的比较操作十分昂贵的话，这可以是对更常见方法的改进。这个模块叫做 bisect 因为其使用了基本的二分（bisection）算法。源代码也可以作为很棒的算法示例（边界判断也做好啦！）

### [weakref 弱引用](https://docs.python.org/zh-cn/3/library/weakref.html)

weakref 模块允许Python程序员创建对象的 weak references 。

在下文中，术语 referent 表示由弱引用引用的对象。

对对象的弱引用不能保证对象存活：当对像的引用只剩弱引用时， garbage collection 可以销毁引用并将其内存重用于其他内容。但是，在实际销毁对象之前，即使没有强引用，弱引用也一直能返回该对象。

弱引用的主要用途是实现保存大对象的高速缓存或映射，但又并希望大对象仅仅因为它出现在高速缓存或映射中而保持存活。

### [copy 浅层 (shallow) 和深层 (deep) 复制操作](https://docs.python.org/zh-cn/3/library/copy.html)

浅层复制和深层复制之间的区别仅与复合对象 (即包含其他对象的对象，如列表或类的实例) 相关:
* 一个 浅层复制 会构造一个新的复合对象，然后（在可能的范围内）将原对象中找到的 引用 插入其中。
* 一个 深层复制 会构造一个新的复合对象，然后递归地将原始对象中所找到的对象的 副本 插入。

深度复制操作通常存在两个问题, 而浅层复制操作并不存在这些问题：
* 递归对象 (直接或间接包含对自身引用的复合对象) 可能会导致递归循环。
* 由于深层复制会复制所有内容，因此可能会过多复制（例如本应该在副本之间共享的数据）。

### [pprint 数据美化输出](https://docs.python.org/zh-cn/3/library/pprint.html)

pprint 模块提供了“美化打印”任意 Python 数据结构的功能，这种美化形式可用作对解释器的输入。 如果经格式化的结构包含非基本 Python 类型的对象，则其美化形式可能无法被加载。 包含文件、套接字或类对象，以及许多其他不能用 Python 字面值来表示的对象都有可能导致这样的结果。

格式化后的形式会在可能的情况下以单行来表示对象，并在无法在允许宽度内容纳对象的情况下将其分为多行。 如果你需要调整宽度限制则应显式地构造 PrettyPrinter 对象。

字典在计算其显示形式前会先根据键来排序。

### [enum 对枚举的支持](https://docs.python.org/zh-cn/3/library/enum.html)

枚举是一组符号名称（枚举成员）的集合，枚举成员应该是唯一的、不可变的。在枚举中，可以对成员进行恒等比较，并且枚举本身是可迭代的。

## [数字和数学模块](https://docs.python.org/zh-cn/3/library/numeric.html)

本章介绍的模块提供与数字和数学相关的函数和数据类型。 numbers 模块定义了数字类型的抽象层次结构。 math 和 cmath 模块包含浮点数和复数的各种数学函数。 decimal 模块支持使用任意精度算术的十进制数的精确表示。

### [math 数学函数](https://docs.python.org/zh-cn/3/library/math.html)

该模块提供了对C标准定义的数学函数的访问。

这些函数不适用于复数；如果你需要计算复数，请使用 cmath 模块中的同名函数。将支持计算复数的函数区分开的目的，来自于大多数开发者并不愿意像数学家一样需要学习复数的概念。得到一个异常而不是一个复数结果使得开发者能够更早地监测到传递给这些函数的参数中包含复数，进而调查其产生的原因。

该模块提供了以下函数。除非另有明确说明，否则所有返回值均为浮点数。

### [decimal 十进制定点和浮点运算](https://docs.python.org/zh-cn/3/library/decimal.html)

decimal 模块为快速正确舍入的十进制浮点运算提供支持。 与 float 数据类型相比，它具有以下几个优点：
* Decimal 类型的“设计是基于考虑人类习惯的浮点数模型，并且因此具有以下最高指导原则 —— 计算机必须提供与人们在学校所学习的算术相一致的算术。” —— 摘自 decimal 算术规范描述。
* Decimal 数字的表示是完全精确的。 相比之下，1.1 和 2.2 这样的数字在二进制浮点中没有精确的表示。 最终用户通常不希望 1.1 + 2.2 如二进制浮点数表示那样被显示为 3.3000000000000003。
* 精确性会延续到算术类操作中。 对于 decimal 浮点数，0.1 + 0.1 + 0.1 - 0.3 会精确地等于零。 而对于二进制浮点数，结果则为 5.5511151231257827e-017 。 虽然接近于零，但其中的误差将妨碍可靠的相等性检验，并且误差还会不断累积。 因此，decimal 更适合具有严格相等不变性要求的会计类应用。
* 十进制模块包含有效位的概念，因此 1.30 + 1.20 的结果是 2.50 。 保留尾随零以表示有效位。 这是货币的惯用表示方法。乘法则沿用 “教科书“ 中：保留被乘数中的所有数字的方法。 例如， 1.3 * 1.2 结果是 1.56 而 1.30 * 1.20 结果是 1.5600 。
* 与基于硬件的二进制浮点不同，十进制模块具有用户可更改的精度（默认为28位），可以与给定问题所需的一样大：

```python
from decimal import *
getcontext().prec = 6
Decimal(1) / Decimal(7)
Decimal('0.142857')
getcontext().prec = 28
Decimal(1) / Decimal(7)
Decimal('0.1428571428571428571428571429')
```

* 二进制和 decimal 浮点数都是根据已发布的标准实现的。 虽然内置浮点类型只公开其功能的一小部分，但 decimal 模块公开了标准的所有必需部分。 在需要时，程序员可以完全控制舍入和信号处理。 这包括通过使用异常来阻止任何不精确操作来强制执行精确算术的选项。
* decimal 模块旨在支持“无偏差，精确无舍入的十进制算术（有时称为定点数算术）和有舍入的浮点数算术”。 —— 摘自 decimal 算术规范说明。

### [fractions 分数](https://docs.python.org/zh-cn/3/library/fractions.html)

fractions 模块支持分数运算。

分数实例可以由一对整数，一个分数，或者一个字符串构建而成。

### [random 生成伪随机数](https://docs.python.org/zh-cn/3/library/random.html)

该模块实现了各种分布的伪随机数生成器。

对于整数，从范围中有统一的选择。 对于序列，存在随机元素的统一选择、用于生成列表的随机排列的函数、以及用于随机抽样而无需替换的函数。

在实数轴上，有计算均匀、正态（高斯）、对数正态、负指数、伽马和贝塔分布的函数。 为了生成角度分布，可以使用 von Mises 分布。

几乎所有模块函数都依赖于基本函数 random() ，它在半开放区间 [0.0,1.0) 内均匀生成随机浮点数。 Python 使用 Mersenne Twister 作为核心生成器。 它产生 53 位精度浮点数，周期为 2**19937-1 ，其在 C 中的底层实现既快又线程安全。 Mersenne Twister 是现存最广泛测试的随机数发生器之一。 但是，因为完全确定性，它不适用于所有目的，并且完全不适合加密目的。

这个模块提供的函数实际上是 random.Random 类的隐藏实例的绑定方法。 你可以实例化自己的 Random 类实例以获取不共享状态的生成器。

如果你想使用自己设计的不同基础生成器，类 Random 也可以作为子类：在这种情况下，重载 random() 、 seed() 、 getstate() 以及 setstate() 方法。可选地，新生成器可以提供 getrandbits() 方法——这允许 randrange() 在任意大的范围内产生选择。

random 模块还提供 SystemRandom 类，它使用系统函数 os.urandom() 从操作系统提供的源生成随机数。

警告: 不应将此模块的伪随机生成器用于安全目的。 有关安全性或加密用途，请参阅 [secrets](https://docs.python.org/zh-cn/3/library/secrets.html#module-secrets) 模块。

```python
>>> a = random.Random(10)
>>> a.random()
0.5714025946899135
>>> a.random()
0.4288890546751146
>>> b = random.Random(10)
>>> b.random()
0.5714025946899135
>>> b.random()
0.4288890546751146
```

为什么不可能产生真正的随机数？参考: [Why Random Numbers are Impossible in Software](https://thecodeboss.dev/2017/05/why-random-numbers-are-impossible-in-software/), [Why is it impossible to produce truly random numbers?](https://softwareengineering.stackexchange.com/questions/124233/why-is-it-impossible-to-produce-truly-random-numbers).

### [statistics 数学统计函数](https://docs.python.org/zh-cn/3/library/statistics.html)

该模块提供了用于计算数字 (Real-valued) 数据的数理统计量的函数。

此模块并不是诸如 NumPy ， SciPy 等第三方库或者诸如 Minitab ， SAS ， Matlab 等针对专业统计学家的专有全功能统计软件包的竟品。此模块针对图形和科学计算器的水平。

除非明确注释，这些函数支持 int ， float ， Decimal 和 Fraction 。当前不支持同其他类型（是否在数字塔中）的行为。混合类型的集合也是未定义的，并且依赖于实现。如果你输入的数据由混合类型组成，你应该能够使用 map() 来确保一个一致的结果，比如： map(float, input_data) 。

## [函数式编程](https://docs.python.org/zh-cn/3/library/functional.html)

本章里描述的模块提供了函数和类，以支持函数式编程风格和在可调用对象上的通用操作。

### [itertools 为高效循环而创建迭代器的函数](https://docs.python.org/zh-cn/3/library/itertools.html)

本模块实现一系列 iterator ，这些迭代器受到APL，Haskell和SML的启发。为了适用于Python，它们都被重新写过。

本模块标准化了一个快速、高效利用内存的核心工具集，这些工具本身或组合都很有用。它们一起形成了“迭代器代数”，这使得在纯Python中有可能创建简洁又高效的专用工具。

例如，SML有一个制表工具： tabulate(f)，它可产生一个序列 f(0), f(1), ...。在Python中可以组合 map() 和 count() 实现： map(f, count())。

这些内置工具同时也能很好地与 operator 模块中的高效函数配合使用。例如，我们可以将两个向量的点积映射到乘法运算符： sum(map(operator.mul, vector1, vector2)) 。

### [functools 高阶函数和可调用对象上的操作](https://docs.python.org/zh-cn/3/library/functools.html)

functools 模块应用于高阶函数，即参数或（和）返回值为其他函数的函数。 通常来说，此模块的功能适用于所有可调用对象。

### [operator 标准运算符替代函数](https://docs.python.org/zh-cn/3/library/operator.html)

operator 模块提供了一套与Python的内置运算符对应的高效率函数。例如，operator.add(x, y) 与表达式 x+y 相同。 许多函数名与特殊方法名相同，只是没有双下划线。为了向后兼容性，也保留了许多包含双下划线的函数。为了表述清楚，建议使用没有双下划线的函数。

函数包含的种类有：对象的比较运算、逻辑运算、数学运算以及序列运算。

对象比较函数适用于所有的对象，函数名根据它们对应的比较运算符命名。

#### 原地运算符

许多运算都有“原地”版本。 以下列出的是提供对原地运算符相比通常语法更底层访问的函数，例如 statement x += y 相当于 x = operator.iadd(x, y)。 换一种方式来讲就是 z = operator.iadd(x, y) 等价于语句块 z = x; z += y。

在这些例子中，请注意当调用一个原地方法时，运算和赋值是分成两个步骤来执行的。 下面列出的原地函数只执行第一步即调用原地方法。 第二步赋值则不加处理。

对于不可变的目标例如字符串、数字和元组，更新的值会被计算，但不会被再被赋值给输入变量：

```python
>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'
```

对于可变的目标例如列表和字典，原地方法将执行更新，因此不需要后续赋值操作：

```python
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```

## [文件和目录访问](https://docs.python.org/zh-cn/3/library/filesys.html)

本章中描述的模块处理磁盘文件和目录。 例如，有一些模块用于读取文件的属性，以可移植的方式操作路径以及创建临时文件。

### [os.path 常用路径操作](https://docs.python.org/zh-cn/3/library/os.path.html)

该模块在路径名上实现了一些有用的功能：如需读取或写入文件，请参见 open() ；有关访问文件系统的信息，请参见 os 模块。路径参数可以字符串或字节形式传递。我们鼓励应用程序将文件名表示为（Unicode）字符串。不幸的是，某些文件名在Unix上可能无法用字符串表示，因此在Unix上平台上需要支持任意文件名的应用程序，应使用字节对象来表示路径名。反之亦然，在Windows平台上仅使用字节对象，不能表示的所有文件名（以标准 mbcs 编码），因此Windows应用程序应使用字符串对象来访问所有文件。

### [glob Unix 风格路径名模式扩展](https://docs.python.org/zh-cn/3/library/glob.html)

glob 模块可根据 Unix 终端所用规则找出所有匹配特定模式的路径名，但会按不确定的顺序返回结果。 波浪号扩展不会生效，但 *, ? 以及表示为 [] 的字符范围将被正确地匹配。 这是通过配合使用 os.scandir() 和 fnmatch.fnmatch() 函数来实现的，而不是通过实际发起调用子终端。 请注意不同于 fnmatch.fnmatch()，glob 会将以点号 (.) 开头的文件名作为特殊情况来处理。 （对于波浪号和终端变量扩展，请使用 os.path.expanduser() 和 os.path.expandvars()。）

对于字面值匹配，请将原字符用方括号括起来。 例如，'\[?\]' 将匹配字符 '?'。

## [数据持久化](https://docs.python.org/zh-cn/3/library/persistence.html)

本章中描述的模块支持在磁盘上以持久形式存储 Python 数据。 pickle 和 marshal 模块可以将许多 Python 数据类型转换为字节流，然后从字节中重新创建对象。 各种与 DBM 相关的模块支持一系列基于散列的文件格式，这些格式存储字符串到其他字符串的映射。

## [数据压缩和存档](https://docs.python.org/zh-cn/3/library/archiving.html)

本章中描述的模块支持 zlib、gzip、bzip2 和 lzma 数据压缩算法，以及创建 ZIP 和 tar 格式的归档文件。参见由 shutil 模块提供的 归档操作 。

## [文件格式](https://docs.python.org/zh-cn/3/library/fileformats.html)

本章中描述的模块解析各种不是标记语言且与电子邮件无关的杂项文件格式。

### [plistlib 生成与解析 Mac OS X .plist 文件](https://docs.python.org/zh-cn/3/library/plistlib.html)

此模块提供了读写主要用于 Mac OS X 的 "property list" 文件的接口，并同时支持二进制和 XML plist 文件。

property list (.plist) 文件格式是一种简单的序列化格式，它支持一些基本对象类型，例如字典、列表、数字和字符串等。 通常使用一个字典作为最高层级对象。

## [加密服务](https://docs.python.org/zh-cn/3/library/crypto.html)

本章中描述的模块实现了加密性质的各种算法。 它们可以在安装时自行选择。 在 Unix 系统上，crypt 模块也可以使用。

### [secrets 生成安全随机数字用于管理密码](https://docs.python.org/zh-cn/3/library/secrets.html)

secrets 模块可用于生成高加密强度的随机数，适应管理密码、账户验证、安全凭据和相关机密数据管理的需要。

特别地，应当优先使用 secrets 来替代 random 模块中默认的伪随机数生成器，后者被设计用于建模和仿真，而不适用于安全和加密。

## [通用操作系统服务](https://docs.python.org/zh-cn/3/library/allos.html)

本章中描述的各模块提供了在（几乎）所有的操作系统上可用的操作系统特性的接口，例如文件和时钟。这些接口通常以 Unix 或 C 接口为参考对象，不过在大多数其他系统上也可用。

### [time 时间的访问和转换](https://docs.python.org/zh-cn/3/library/time.html)

该模块提供了各种时间相关的函数。相关功能还可以参阅 datetime 和 calendar 模块。

尽管此模块始终可用，但并非所有平台上都提供所有功能。 此模块中定义的大多数函数是调用了所在平台 C 语言库的同名函数。 因为这些函数的语义因平台而异,所以使用时最好查阅平台相关文档。

### [argparse 命令行选项、参数和子命令解析器](https://docs.python.org/zh-cn/3/library/argparse.html)

argparse 模块可以让人轻松编写用户友好的命令行接口。程序定义它需要的参数，然后 argparse 将弄清如何从 sys.argv 解析出那些参数。 argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。

### [logging Python 的日志记录工具](https://docs.python.org/zh-cn/3/library/logging.html)

这个模块为应用与库实现了灵活的事件日志系统的函数与类。

使用标准库提提供的 logging API 最主要的好处是，所有的 Python 模块都可能参与日志输出，包括你自己的日志消息和第三方模块的日志消息。

这个模块提供许多强大而灵活的功能。如果你对 logging 不太熟悉的话， 掌握它最好的方式就是查看它对应的教程（详见右侧的链接）。

该模块定义的基础类和函数都列在下面。
* 记录器暴露了应用程序代码直接使用的接口。
* 处理器将日志记录（由记录器创建）发送到适当的目标。
* 过滤器提供了更精细的附加功能，用于确定要输出的日志记录。
* 格式器指定最终输出中日志记录的样式。

### [logging.config 日志记录配置](https://docs.python.org/zh-cn/3/library/logging.config.html)

这一节描述了用于配置 logging 模块的 API。

### [logging.handlers 日志处理](https://docs.python.org/zh-cn/3/library/logging.handlers.html)

这个包提供了以下有用的处理程序。 请注意有三个处理程序类 (StreamHandler, FileHandler 和 NullHandler) 实际上是在 logging 模块本身定义的，但其文档与其他处理程序一同记录在此。

### [ctypes Python 的外部函数库](https://docs.python.org/zh-cn/3/library/ctypes.html)

ctypes 是 Python 的外部函数库。它提供了与 C 兼容的数据类型，并允许调用 DLL 或共享库中的函数。可使用该模块以纯 Python 形式对这些库进行封装。

## [并发执行](https://docs.python.org/zh-cn/3/library/concurrency.html)

本章中描述的模块支持并发执行代码。 适当的工具选择取决于要执行的任务（CPU密集型或IO密集型）和偏好的开发风格（事件驱动的协作式多任务或抢占式多任务处理）。 

### [threading 基于线程的并行](https://docs.python.org/zh-cn/3/library/threading.html)

这个模块在较低级的模块 _thread 基础上建立较高级的线程接口。

### [multiprocessing 基于进程的并行](https://docs.python.org/zh-cn/3/library/multiprocessing.html)

multiprocessing 是一个用于产生进程的包，具有与 threading 模块相似API。 multiprocessing 包同时提供本地和远程并发，使用子进程代替线程，有效避免 Global Interpreter Lock 带来的影响。因此， multiprocessing 模块允许程序员充分利用机器上的多核。可运行于 Unix 和 Windows 。

multiprocessing 模块还引入了在 threading 模块中没有的API。一个主要的例子就是 Pool 对象，它提供了一种快捷的方法，赋予函数并行化处理一系列输入值的能力，可以将输入数据分配给不同进程处理（数据并行）。

### [concurrent.futures 启动并行任务](https://docs.python.org/zh-cn/3/library/concurrent.futures.html)

concurrent.futures 模块提供异步执行可调用对象高层接口。

异步执行可以由 ThreadPoolExecutor 使用线程或由 ProcessPoolExecutor 使用单独的进程来实现。 两者都是实现抽像类 Executor 定义的接口。

### [subprocess 子进程管理](https://docs.python.org/zh-cn/3/library/subprocess.html)

subprocess 模块允许你生成新的进程，连接它们的输入、输出、错误管道，并且获取它们的返回码。

### [queue 一个同步的队列类](https://docs.python.org/zh-cn/3/library/queue.html)

queue 模块实现了多生产者、多消费者队列。这特别适用于消息必须安全地在多线程间交换的线程编程。模块中的 Queue 类实现了所有所需的锁定语义。

模块实现了三种类型的队列，它们的区别仅仅是条目取回的顺序。在 FIFO 队列中，先添加的任务先取回。在 LIFO 队列中，最近被添加的条目先取回(操作类似一个堆栈)。优先级队列中，条目将保持排序( 使用 heapq 模块 ) 并且最小值的条目第一个返回。

在内部，这三个类型的队列使用锁来临时阻塞竞争线程；然而，它们并未被设计用于线程的重入性处理。

此外，模块实现了一个 "简单的" FIFO 队列类型， SimpleQueue ，这个特殊实现为小功能在交换中提供额外的保障。

### [_thread 底层多线程 API](https://docs.python.org/zh-cn/3/library/_thread.html)

该模块提供了操作多个线程（也被称为 轻量级进程 或 任务）的底层原语 —— 多个控制线程共享全局数据空间。为了处理同步问题，也提供了简单的锁机制（也称为 互斥锁 或 二进制信号）。threading 模块基于该模块提供了更易用的高级多线程 API。

## [网络和进程间通信](https://docs.python.org/zh-cn/3/library/ipc.html)

本章介绍的模块提供了网络和进程间通信的机制。

某些模块仅适用于同一台机器上的两个进程，例如 signal 和 mmap 。 其他模块支持两个或多个进程可用于跨机器通信的网络协议。

### [asyncio 异步 I/O](https://docs.python.org/zh-cn/3/library/asyncio.html)

asyncio 是用来编写 并发 代码的库，使用 async/await 语法。

asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。

asyncio 往往是构建 IO 密集型和高层级 结构化 网络代码的最佳选择。

#### [协程与任务](https://docs.python.org/zh-cn/3/library/asyncio-task.html)

本节将简述用于协程与任务的高层级 API。

#### [Futures](https://docs.python.org/zh-cn/3/library/asyncio-future.html)

Future 对象用来链接 底层回调式代码 和高层异步/等待式代码。

### [socket 底层网络接口](https://docs.python.org/zh-cn/3/library/socket.html)

这个模块提供了访问 BSD 套接字 的接口。在所有现代 Unix 系统、Windows、macOS 和其他一些平台上可用。

注解: 一些行为可能因平台不同而异，因为调用的是操作系统的套接字API。

这个Python接口是用Python的面向对象风格对Unix系统调用和套接字库接口的直译：函数 socket() 返回一个 套接字对象 ，其方法是对各种套接字系统调用的实现。形参类型一般与C接口相比更高级：例如在Python文件 read() 和 write() 操作中，接收操作的缓冲区分配是自动的，发送操作的缓冲区长度是隐式的。

## [互联网数据处理](https://docs.python.org/zh-cn/3/library/netdata.html)

本章介绍了支持处理互联网上常用数据格式的模块。

### [email 电子邮件与 MIME 处理包](https://docs.python.org/zh-cn/3/library/email.html)

该email软件包是用于管理电子邮件的库。它不是专门为将电子邮件发送到SMTP（RFC 2821），NNTP或其他服务器；这些是模块的功能，如 smtplib和nntplib。该email软件包尝试尽可能地符合RFC，以支持RFC 5233和RFC 6532以及与MIME相关的RFC，例如RFC 2045，RFC 2046，RFC 2047，RFC 2183和RFC 2231。

电子邮件软件包的整体结构可以分为三个主要部分，以及控制其他部分行为的第四个部分。

#### [email: 示例](https://docs.python.org/zh-cn/3/library/email.examples.html)

以下是一些如何使用 email 包来读取、写入和发送简单电子邮件以及更复杂的MIME邮件的示例。

### [json JSON 编码和解码器](https://docs.python.org/zh-cn/3/library/json.html)

JSON (JavaScript Object Notation)，由 RFC 7159 (which obsoletes RFC 4627) 和 ECMA-404 指定，是一个受 JavaScript 的对象字面量语法启发的轻量级数据交换格式，尽管它不仅仅是一个严格意义上的 JavaScript 的字集 1。

json 提供了与标准库 marshal 和 pickle 相似的API接口。

### [base64 Base16, Base32, Base64, Base85 数据编码](https://docs.python.org/zh-cn/3/library/base64.html)

此模块提供了将二进制数据编码为可打印的 ASCII 字符以及将这些编码解码回二进制数据的函数。它为 RFC 3548 指定的 Base16, Base32 和 Base64 编码以及已被广泛接受的 Ascii85 和 Base85 编码提供了编码和解码函数。

RFC 3548 编码的目的是使得二进制数据可以作为电子邮件的内容正确地发送，用作 URL 的一部分，或者作为 HTTP POST 请求的一部分。其中的编码算法和 uuencode 程序是不同的。

## [结构化标记处理工具](https://docs.python.org/zh-cn/3/library/markup.html)

Python 支持各种模块，以处理各种形式的结构化数据标记。 这包括使用标准通用标记语言（SGML）和超文本标记语言（HTML）的模块，以及使用可扩展标记语言（XML）的几个接口。

## [互联网协议和支持](https://docs.python.org/zh-cn/3/library/internet.html)

本章介绍的模块实现了互联网协议并支持相关技术。 它们都是用 Python 实现的。 这些模块中的大多数都需要存在依赖于系统的模块 socket ，目前大多数流行平台都支持它。 

## [多媒体服务](https://docs.python.org/zh-cn/3/library/mm.html)

本章描述的模块实现了主要用于多媒体应用的各种算法或接口。 它们可在安装时自行决定。

## [国际化](https://docs.python.org/zh-cn/3/library/i18n.html)

本章中介绍的模块通过提供选择要在程序信息中使用的语言的机制或通过定制输出以匹配本地约定来帮助你编写不依赖于语言和区域设置的软件。

## [程序框架](https://docs.python.org/zh-cn/3/library/frameworks.html)

本章中描述的模块是很大程度上决定程序结构的框架。 目前，这里描述的模块都面向编写命令行接口。

### [turtle 海龟绘图](https://docs.python.org/zh-cn/3/library/turtle.html)

海龟绘图很适合用来引导孩子学习编程。 最初来自于 Wally Feurzeig, Seymour Papert 和 Cynthia Solomon 于 1967 年所创造的 Logo 编程语言。

### [cmd 支持面向行的命令解释器](https://docs.python.org/zh-cn/3/library/cmd.html)

Cmd 类提供简单框架用于编写面向行的命令解释器。 这些通常对测试工具，管理工具和原型有用，这些工具随后将被包含在更复杂的接口中。

## [Tk图形用户界面(GUI)](https://docs.python.org/zh-cn/3/library/tk.html)

Tcl/Tk集成到Python中已经有一些年头了。Python程序员可以通过 tkinter 包和它的扩展， tkinter.tix 模块和 tkinter.ttk 模块，来使用这套鲁棒的、平台无关的窗口工具集。

tkinter 包使用面向对象的方式对Tcl/Tk进行了一层薄包装。使用 tkinter ，你不需要写Tcl代码，但可能需要参考Tk文档，甚至Tcl文档。 tkinter 使用Python类，对Tk的窗体小部件（Widgets）进行了一系列的封装。除此之外，内部模块 _tkinter 针对Python和Tcl之间的交互，提供了一套线程安全的机制。

tkinter 最大的优点就一个字：快，再一个，是Python自带的。尽管官方文档不太完整，但有其他资源可以参考，比如Tk手册，教程等。 tkinter 也以比较过时的外观为人所知，但在Tk 8.5中，这一点得到了极大的改观。除此之外，如果有兴趣，还有其他的一些GUI库可供使用。更多信息，请参考 其他图形用户界面（GUI）包 小节。

### [IDLE](https://docs.python.org/zh-cn/3/library/idle.html)

IDLE 是 Python 所内置的开发与学习环境。

IDLE 具有以下特性：
* 编码于 100% 纯正的 Python，使用名为 tkinter 的图形用户界面工具
* 跨平台：在 Windows、Unix 和 macOS 上工作近似。
* 提供输入输出高亮和错误信息的 Python 命令行窗口 （交互解释器）
* 提供多次撤销操作、Python 语法高亮、智能缩进、函数调用提示、自动补全等功能的多窗口文本编辑器
* 在多个窗口中检索，在编辑器中替换文本，以及在多个文件中检索（通过 grep）
* 提供持久保存的断点调试、单步调试、查看本地和全局命名空间功能的调试器
* 配置、浏览以及其它对话框

## [开发工具](https://docs.python.org/zh-cn/3/library/development.html)

本章中描述的各模块可帮你编写 Python 程序。例如，pydoc 模块接受一个模块并根据该模块的内容来生成文档。doctest 和 unittest 这两个模块包含了用于编写单元测试的框架，并可用于自动测试所编写的代码，验证预期的输出是否产生。2to3 程序能够将 Python 2.x 源代码翻译成有效的 Python 3.x 源代码。

### [pydoc 文档生成器和在线帮助系统](https://docs.python.org/zh-cn/3/library/pydoc.html)

该pydoc模块会自动从Python模块生成文档。该文档可以在控制台上以文本页面的形式呈现，提供给Web浏览器或保存为HTML文件。

对于模块、类、函数和方法，显示的文档内容取自文档字符串（即 __doc__ 属性），并会递归地从其带文档的成员中获取。 如果没有文档字符串，pydoc 会尝试从类、函数或方法定义上方，或是模块顶部的注释行段落获取 (参见 inspect.getcomments()).

内置函数 help() 会发起调用交互式解释器的在线帮助系统，该系统使用 pydoc 在终端上生成文本形式的文档内容。 同样的文本文档也可以在 Python 解释器以外通过在操作系统的命令提示符下以脚本方式运行 pydoc 来查看。 

### [doctest 测试交互性的Python示例](https://docs.python.org/zh-cn/3/library/doctest.html)

doctest 模块寻找像Python交互式代码的文本，然后执行这些代码来确保它们的确就像展示的那样正确运行，有许多方法来使用doctest：
* 通过验证所有交互式示例仍然按照记录的方式工作，以此来检查模块的文档字符串是否是最新的。
* 通过验证来自测试文件或测试对象的交互式示例是否按预期工作来执行回归测试。
* 编写软件包的教程文档，并通过输入输出示例进行详细说明。根据是否强调示例或说明文字，这具有“识字测试”或“可执行文档”的风格。

### [unittest 单元测试框架](https://docs.python.org/zh-cn/3/library/unittest.html)

unittest 单元测试框架是受到 JUnit 的启发，与其他语言中的主流单元测试框架有着相似的风格。其支持测试自动化，配置共享和关机代码测试。支持将测试样例聚合到测试集中，并将测试与报告框架独立。

为了实现这些，unittest 通过面向对象的方式支持了一些重要的概念。

### [unittest.mock 模拟对象库](https://docs.python.org/zh-cn/3/library/unittest.mock.html)

unittest.mock 是一个用于测试的Python库。它允许使用模拟对象来替换受测系统的部分，并对它们如何已经被使用进行断言。

unittest.mock 提供了一个核心类 Mock 用于消除了在整个测试套件中创建大量存根(stub)的需求。创建后，就可以断言调用了哪些方法/属性及其参数。还可以以常规方式指定返回值并设置所需的属性。

此外，mock 提供了用于修补测试范围内模块和类级别属性的 patch() 装饰器，和用于创建独特对象的 sentinel 。 阅读 quick guide 中的案例了解如何使用 Mock ，MagicMock 和 patch() 。

Mock 是为 unittest 而设计，且简单易用。模拟基于 'action -> assertion' 模式，而不是许多模拟框架所使用的 'record -> replay'模式。

### [unittest.mock 上手指南](https://docs.python.org/zh-cn/3/library/unittest.mock-examples.html)

使用 Mock 的常见场景：
* 模拟函数调用
* 记录“对象上的方法调用”

### [2to3 自动将 Python 2 代码转为 Python 3 代码](https://docs.python.org/zh-cn/3/library/2to3.html)

2to3 是一个 Python 程序，它可以用来读取 Python 2.x 版本的代码，并使用一系列的 修复器 来将其转换为合法的 Python 3.x 代码。标准库中已经包含了丰富的修复器，这足以处理绝大多数代码。不过 2to3 的支持库 lib2to3 是一个很灵活通用的库，所以你也可以为 2to3 编写你自己的修复器。lib2to3 也可以用在那些需要自动处理 Python 代码的应用中。

### [test Python回归测试包](https://docs.python.org/zh-cn/3/library/test.html)

注解: 该test软件包仅供Python内部使用。它被记录为Python核心开发人员的利益。不建议在Python标准库之外使用此软件包，因为此处提到的代码可以更改，也可以在不考虑Python版本之间删除的情况下删除。

该test软件包包含针对Python的所有回归测试以及模块test.support和test.regrtest。 test.support用于test.regrtest驱动测试套件时增强您 的测试。

test包中每个以其名称开头的模块test_都是针对特定模块或功能的测试套件。所有新测试都应使用unittest或doctest模块编写。一些较早的测试是使用“传统”测试样式编写的，该样式将打印输出与进行比较 sys.stdout。这种测试风格被认为已弃用。

## [调试和分析](https://docs.python.org/zh-cn/3/library/debug.html)

这些库可以帮助你进行 Python 开发：调试器使你能够逐步执行代码，分析堆栈帧并设置中断点等等，性能分析器可以运行代码并为你提供执行时间的详细数据，使你能够找出你的程序中的瓶颈。 审计事件提供运行时行为的可见性，如果没有此工具则需要进行侵入式调试或修补。

### [Python Profilers 分析器](https://docs.python.org/zh-cn/3/library/profile.html)

cProfile 和 profile 提供了 Python 程序的 确定性性能分析 。 profile 是一组统计数据，描述程序的各个部分执行的频率和时间。这些统计数据可以通过 pstats 模块格式化为报表。

Python 标准库提供了同一分析接口的两种不同实现：
1. 对于大多数用户，建议使用 cProfile ；这是一个 C 扩展插件，因为其合理的运行开销，所以适合于分析长时间运行的程序。该插件基于 lsprof ，由 Brett Rosen 和 Ted Chaotter 贡献。
2. profile 是一个纯 Python 模块（cProfile 就是模拟其接口的 C 语言实现），但它会显著增加配置程序的开销。如果你正在尝试以某种方式扩展分析器，则使用此模块可能会更容易完成任务。该模块最初由 Jim Roskind 设计和编写。

注解: profiler 分析器模块被设计为给指定的程序提供执行概要文件，而不是用于基准测试目的（ timeit 才是用于此目标的，它能获得合理准确的结果）。这特别适用于将 Python 代码与 C 代码进行基准测试：分析器为Python 代码引入开销，但不会为 C级别的函数引入开销，因此 C 代码似乎比任何Python 代码都更快。

### [timeit 测量小代码片段的执行时间](https://docs.python.org/zh-cn/3/library/timeit.html)

该模块提供了一种简单的方法来计算一小段 Python 代码的耗时。它有 命令行界面 以及一个 可调用 方法。它避免了许多用于测量执行时间的常见陷阱。另见 Tim Peters 对 O'Reilly 出版的 Python Cookbook 中“算法”章节的介绍。

## [软件打包和分发](https://docs.python.org/zh-cn/3/library/distribution.html)

这些库可帮助你发布和安装 Python 软件。 虽然这些模块设计为与 [Python 包索引](https://pypi.org) 结合使用，但它们也可以与本地索引服务器一起使用，或者根本不使用任何索引服务器。

### [distutils 构建和安装 Python 模块](https://docs.python.org/zh-cn/3/library/distutils.html)

distutils 包为将待构建和安装的额外的模块，打包成 Python 安装包提供支持。新模块既可以是百分百的纯 Python，也可以是用 C 写的扩展模块，或者可以是一组包含了同时用 Python 和 C 编码的 Python 包。

大多数 Python 用户 不会 想要直接使用这个包，而是使用 Python 包官方维护的跨版本工具。特别地， setuptools 是一个对于 distutils 的增强选项，它能提供：
* 对声明项目依赖的支持
* 额外的用于配置哪些文件包含在源代码发布中的机制（包括与版本控制系统集成需要的插件）
* 生成项目“进入点”的能力，进入点可用作应用插件系统的基础
* 自动在安装时间生成 Windows 命令行可执行文件的能力，而不是需要预编译它们
* 跨所有受支持的 Python 版本上的一致的表现

## [Python 运行时服务](https://docs.python.org/zh-cn/3/library/python.html)

本章里描述的模块提供了和Python解释器及其环境交互相关的广泛服务。

### [sys 系统相关的参数和函数](https://docs.python.org/zh-cn/3/library/sys.html)

该模块提供了一些变量和函数。这些变量可能被解释器使用，也可能由解释器提供。这些函数会影响解释器。本模块总是可用的。

### [builtins 内建对象](https://docs.python.org/zh-cn/3/library/builtins.html)

该模块提供对Python的所有“内置”标识符的直接访问；例如，builtins.open 是内置函数的全名 open() 。请参阅 内置函数 和 内置常量 的文档。

大多数应用程序通常不会显式访问此模块，但在提供与内置值同名的对象的模块中可能很有用，但其中还需要内置该名称。例如，在一个想要实现 open() 函数的模块中，它包装了内置的 open() ，这个模块可以直接使用。

### [contextlib 为 with语句上下文提供的工具](https://docs.python.org/zh-cn/3/library/contextlib.html)

此模块为涉及 with 语句的常见任务提供了实用的程序。更多信息请参见 上下文管理器类型 和 with 语句上下文管理器。

### [\__future\__ Future 语句定义](https://docs.python.org/zh-cn/3/library/__future__.html)

\__future\__ 是一个真正的模块，这主要有 3 个原因：
* 避免混淆已有的分析 import 语句并查找 import 的模块的工具。
* 确保 future 语句 在 2.1 之前的版本运行时至少能抛出 runtime 异常（import __future__ 会失败，因为 2.1 版本之前没有这个模块）。
* 当引入不兼容的修改时，可以记录其引入的时间以及强制使用的时间。这是一种可执行的文档，并且可以通过 import __future__ 来做程序性的检查。











