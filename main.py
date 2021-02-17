import math
from math import *

# x = 77
# y = 48
# f = (x**5 + x**3) / (40 * y**5 - tan(y)) + sqrt((sin(y) + y**8 - 63) / (28 * x**6 + 89 * x**5)) - (x - sin(y))
# print ('{:.2e}'.format(f))
x = 167
f = 0
if x < 57:
    f = x ** 5 + x ** 3
elif 57 <= x < 141:
   f = 40 * (x + math.exp ** x) ** 5 - x ** 3
elif 141 <= x < 194:
   f = sin(41 * x ** 5 - tan(x)) + tan(x) + 92
elif x >= 194:
    f = x + 95 * x ** 5
print('{:.2e}'.format(f))