from bisect import bisect, bisect_left


# 函数 bisect() 还可以用于数字表查询。这个例子是使用 bisect() 从一个给定的考试成绩集合里，通过一个有序数字表，查出其对应的字母等级：
# 90 分及以上是 'A'，80 到 89 是 'B'，以此类推
def grade(score, breakpoints=None, grades='FDCBA'):
    if breakpoints is None:
        breakpoints = [60, 70, 80, 90]
    i = bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])  # ['F', 'A', 'C', 'C', 'B', 'A', 'A']

# 与 sorted() 函数不同，对于 bisect() 函数来说，key 或者 reversed 参数并没有什么意义。
# 因为这会导致设计效率低下（连续调用 bisect 函数时，是不会 "记住" 过去查找过的键的）。
# 正相反，最好去搜索预先计算好的键列表，来查找相关记录的索引。

data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]  # precomputed list of keys
print(data[bisect_left(keys, 0)])  # ('black', 0)
print(data[bisect_left(keys, 1)])  # ('blue', 1)
print(data[bisect_left(keys, 5)])  # ('red', 5)
print(data[bisect_left(keys, 8)])  # ('yellow', 8)
