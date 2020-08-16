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








