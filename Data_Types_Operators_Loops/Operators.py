# Arithmetic Operators
a, b = 10, 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a // b)  # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b)  # Exponentiation: 1000

# Comparison Operators
print(a == b)  # Equal: False
print(a != b)  # Not Equal: True
print(a > b)  # Greater Than: True
print(a < b)  # Less Than: False
print(a >= b)  # Greater or Equal: True
print(a <= b)  # Less or Equal: False

# Logical Operators
x, y = True, False
print(x and y)  # AND: False
print(x or y)  # OR: True
print(not x)  # NOT: False

# Bitwise Operators
p, q = 5, 3  # (Binary: 5 = 101, 3 = 011)
print(p & q)  # AND: 1 (001)
print(p | q)  # OR: 7 (111)
print(p ^ q)  # XOR: 6 (110)
print(~p)  # NOT: -6
print(p << 1)  # Left Shift: 10 (1010)
print(p >> 1)  # Right Shift: 2 (010)

# Assignment Operators
c = 10
c += 5  # Equivalent to: c = c + 5
print(c)  # 15
c -= 3
print(c)  # 12
c *= 2
print(c)  # 24
c /= 4
print(c)  # 6.0
c %= 4
print(c)  # 2.0
c **= 3
print(c)  # 8.0
c //= 2
print(c)  # 4.0

# Identity Operators
m, n = [1, 2, 3], [1, 2, 3]
print(m is n)  # False (Different memory locations)
print(m is not n)  # True
o = m
print(o is m)  # True (Same memory location)

# Membership Operators
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # True
print(10 not in numbers)  # True
