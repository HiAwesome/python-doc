from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))  # 0.74
print(round(0.70 * 1.05, 2))  # 0.73
print()

print(Decimal('1.00') % Decimal('.10'))  # 0.00
print(1.00 % 0.10)  # 0.09999999999999995
print()

getcontext().prec = 36
print(Decimal(1) / Decimal(7))  # 0.142857142857142857142857142857142857
