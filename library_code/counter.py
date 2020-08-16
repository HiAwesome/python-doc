from collections import Counter

cnt = Counter()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
  cnt[word] += 1

print(cnt)  # Counter({'blue': 3, 'red': 2, 'green': 1})

# Counter对象有一个字典接口，如果引用的键没有任何记录，就返回一个0，而不是弹出一个 KeyError.
print(cnt['yellow'])  # 0

# elements(): 返回一个迭代器，其中每个元素将重复出现计数值所指定次。 元素会按首次出现的顺序返回。 如果一个元素的计数值小于一，elements() 将会忽略它。

c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b']

# most_common([n]): 返回一个列表，其中包含 n 个最常见的元素及出现次数，按常见程度由高到低排序。 如果 n 被省略或为 None，most_common() 将返回计数器中的所有元素。 计数值相等的元素按首次出现的顺序排序。
print(Counter('abracadabra').most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]

# subtract([iterable-or-mapping]): 从 迭代对象 或 映射对象 减去元素。像 dict.update() 但是是减去，而不是替换。输入和输出都可以是0或者负数。
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})




