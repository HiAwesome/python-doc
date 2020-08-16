from collections import ChainMap

# 注意，一个 ChainMap() 的迭代顺序是通过扫描最后的映射来确定的:
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(adjustments, baseline)))  # ['music', 'art', 'opera']

# 这给出了与 dict.update() 调用序列相同的顺序，从最后一个映射开始:
combined = baseline.copy()
combined.update(adjustments)
print(list(combined))  # ['music', 'art', 'opera']

print()

a = ChainMap({1: 1, 2: 2}, {2: 100, 3: 1000})
print(a)  # ChainMap({1: 1, 2: 2}, {2: 100, 3: 1000})
print(list(a))  # [2, 3, 1]
print(a[2])  # 2
