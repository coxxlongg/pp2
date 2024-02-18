def even_num(n):
    even_numbers = [i for i in range(0, n+1) if i % 2 == 0]
    
    even_numbers_str = ', '.join(map(str, even_numbers))
    print(even_numbers_str)

n = 9
even_num(n)