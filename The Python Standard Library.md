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

#### heapq 堆队列算法

这个模块提供了堆队列算法的实现，也称为优先队列算法。

堆是一个二叉树，它的每个父节点的值都只会小于或大于所有孩子节点（的值）。它使用了数组来实现：从零开始计数，对于所有的 k ，都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]。 为了便于比较，不存在的元素被认为是无限大。 堆最有趣的特性在于最小的元素总是在根结点：heap[0]。

这个API与教材的堆算法实现有所不同，具体区别有两方面：（a）我们使用了从零开始的索引。这使得节点和其孩子节点索引之间的关系不太直观但更加适合，因为 Python 使用从零开始的索引。 （b）我们的 pop 方法返回最小的项而不是最大的项（这在教材中称为“最小堆”；而“最大堆”在教材中更为常见，因为它更适用于原地排序）。

基于这两方面，把堆看作原生的Python list也没什么奇怪的： heap[0] 表示最小的元素，同时 heap.sort() 维护了堆的不变性！

要创建一个堆，可以使用list来初始化为 [] ，或者你可以通过一个函数 heapify() ，来把一个list转换成堆。

Python 提供的是最小堆，如果需要最大堆目前的主流方案是给每个元素乘负一，取值的时候再乘负一，参考 [What do I use for a max-heap implementation in Python?](https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python) 和 [Max Heap in Python](https://www.geeksforgeeks.org/max-heap-in-python/).

