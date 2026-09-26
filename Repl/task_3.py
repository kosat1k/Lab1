"""x = 17
y = 5
print(x+y) #22 int
print(x-y) #12 int
print(x*y) #85 int
print(x/y) #3.4 float
print(x//y) #3 int
print(x%y) #2 int
print(x**y) #1419857 int
print(2**1000) #1071508607186267320948......
"""
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(2026), type(str(2026)))
print(bool(0), type(bool(0)))
print(bool(-1), type(bool(-1)))
print(bool(""), type(bool("")))
print(bool("False"), type(bool("False")))
z = complex(2, -3)
print(z, type(z))
print("Действительная часть:", z.real)
print("Мнимая часть:", z.imag)

import math

result = 0.1 + 0.2
print(result)
print(result == 0.3)
print(result - 0.3)
print(math.isclose(result, 0.3))