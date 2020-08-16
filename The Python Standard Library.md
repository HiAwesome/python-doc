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







