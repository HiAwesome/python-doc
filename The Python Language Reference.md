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




