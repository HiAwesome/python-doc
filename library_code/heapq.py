from heapq import heappush, heappop


# 堆排序 可以通过将所有值推入堆中然后每次弹出一个最小值项来实现。
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
