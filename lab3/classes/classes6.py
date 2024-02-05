
#numbers = [i for i in range(1, 100)]
#prime = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))

#print(prime)

def filter_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

numbers = list(map(int, input()))

prime_numbers = list(filter(lambda x: filter_prime(x), numbers))