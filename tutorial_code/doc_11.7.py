from array import array

a = array('H', [4000, 10, 700, 2222])
print(sum(a))  # 6932
print(a[1:3])  # array('H', [10, 700])
print()

from collections import deque

d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('Handing ', d.popleft())  # Handing  task1
print()

import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)  # [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
print()

from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
print([heappop(data) for i in range(3)])  # [-5, 0, 1]
