from collections import defaultdict

# 使用 list 作为 default_factory，很轻松地将（键-值对组成的）序列转换为（键-列表组成的）字典
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))  # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# 设置 default_factory 为 int，使 defaultdict 用于计数（类似其他语言中的 bag 或 multiset）
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

print(sorted(d.items()))  # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

# 设置 default_factory 为 set 使 defaultdict 用于构建 set 集合：
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

print(sorted(d.items()))  # [('blue', {2, 4}), ('red', {1, 3})]
