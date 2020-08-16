# The Python Language Reference

根据 [官网教程](https://docs.python.org/3/reference/index.html) 练习 Python3。

## Tips

### 2.1.5. 显式的行拼接

两个或更多个物理行可使用反斜杠字符 (\) 拼接为一个逻辑行，规则如下: 当一个物理行以一个不在字符串或注释内的反斜杠结尾时，它将与下一行拼接构成一个单独的逻辑行，反斜杠及其后的换行符会被删除。例如:

```python
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1
```

以反斜杠结束的行不能带有注释。反斜杠不能用来拼接注释。反斜杠不能用来拼接形符，字符串除外 (即原文字符串以外的形符不能用反斜杠分隔到两个物理行)。不允许有原文字符串以外的反斜杠存在于物理行的其他位置。

### 2.1.6. 隐式的行拼接

圆括号、方括号或花括号以内的表达式允许分成多个物理行，无需使用反斜杠。例如:

```python
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year
```

隐式的行拼接可以带有注释。后续行的缩进不影响程序结构。后续行也允许为空白行。隐式拼接的行之间不会有 NEWLINE 形符。隐式拼接的行也可以出现于三引号字符串中 (见下)；此情况下这些行不允许带有注释。

### 5.2.1. 常规包

Python 定义了两种类型的包，常规包 和 命名空间包。 常规包是传统的包类型，它们在 Python 3.2 及之前就已存在。 常规包通常以一个包含 __init__.py 文件的目录形式实现。 当一个常规包被导入时，这个 __init__.py 文件会隐式地被执行，它所定义的对象会被绑定到该包命名空间中的名称。__init__.py 文件可以包含与任何其他模块中所包含的 Python 代码相似的代码，Python 将在模块被导入时为其添加额外的属性。

例如，以下文件系统布局定义了一个最高层级的 parent 包和三个子包:

```text
parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py
```

导入 parent.one 将隐式地执行 parent/__init__.py 和 parent/one/__init__.py。 后续导入 parent.two 或 parent.three 则将分别执行 parent/two/__init__.py 和 parent/three/__init__.py。

## 5.7. 包相对导入

相对导入使用前缀点号。 一个前缀点号表示相对导入从当前包开始。 两个或更多前缀点号表示对当前包的上级包的相对导入，第一个点号之后的每个点号代表一级。 例如，给定以下的包布局结构:

```text
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```

不论是在 subpackage1/moduleX.py 还是 subpackage1/__init__.py 中，以下导入都是有效的:

```python
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```

绝对导入可以使用 import <> 或 from <> import <> 语法，但相对导入只能使用第二种形式；其中的原因在于:

```python
import XXX.YYY.ZZZ
```

应当提供 XXX.YYY.ZZZ 作为可用表达式，但 .moduleY 不是一个有效的表达式。



