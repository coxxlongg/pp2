import math

numbers = [int(a) for a in input().split()]
prime = list(filter(lambda x: all(x % i != 0 for i in range(2, math.isqrt(x) + 1)), numbers))

print("Prime numbers:", prime)
