import operator
from itertools import *

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(accumulate(data, operator.mul)))  # running product
# [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]

print(list(accumulate(data, max)))  # running maximum
# [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]

cashflows = [1000, -90, -90, -90, -90]
print(list(accumulate(cashflows, lambda bal, pmt: bal * 1.05 + pmt)))
# [1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]

logistic_map = lambda x, _: r * x * (1 - x)
r = 3.8
x0 = 0.4
inputs = repeat(x0, 36)  # only the initial value is used
print([format(x, '.2f') for x in accumulate(inputs, logistic_map)])
# ['0.40', '0.91', '0.30', '0.81', '0.60', '0.92', '0.29', '0.79', '0.63', '0.88', '0.39', '0.90', '0.33', '0.84', '0.52', '0.95', '0.18', '0.57', '0.93', '0.25', '0.71', '0.79', '0.63', '0.88', '0.39', '0.91', '0.32', '0.83', '0.54', '0.95', '0.20', '0.60', '0.91', '0.30', '0.80', '0.60']
