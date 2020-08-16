from functools import lru_cache


# 以下是使用缓存通过 动态规划 计算 斐波那契数列 的例子。
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


a = [fib(n) for n in range(16)]
print(a)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

print(fib.cache_info())  # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)


