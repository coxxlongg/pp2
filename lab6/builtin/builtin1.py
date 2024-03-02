from functools import reduce
from operator import mul

def list(list1):
    result = reduce(mul, list1)
    
    print(result)
