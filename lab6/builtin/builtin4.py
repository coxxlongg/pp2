from time import sleep
from math import sqrt

def fun(num, sec):
    sleep_seconds = sec / 1000
    sleep(sleep_seconds)
    root = sqrt(num)
    
    print(f"Square root of {num} after {int(sec)} milliseconds is {root}")
