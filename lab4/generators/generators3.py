def special_numbers(n):
    numbers = [i for i in range(0, n+1) if i % 3 == 0 and i % 4 == 0]
    
    numbers_str = ', '.join(map(str, numbers))
    print(numbers_str)

n = 100
special_numbers(n)