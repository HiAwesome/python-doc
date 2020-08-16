from heapq import heappush, heappop


# 堆排序 可以通过将所有值推入堆中然后每次弹出一个最小值项来实现。
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 这类似于 sorted(iterable)，但与 sorted() 不同的是这个实现是不稳定的。

# 堆元素可以为元组。 这适用于将比较值（例如任务优先级）与跟踪的主记录进行赋值的场合:
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
print(heappop(h))  # (1, 'write spec')
