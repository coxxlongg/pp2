def filter_prime(nums: list):
        primeList = []
        for number in nums:
            if number < 2:
                continue
            isPrime = True
            for i in range (2, (number ** 0.5) + 1):
                if number % i == 0:
                    isPrime = False
                    break
            if isPrime:
                primeList.append(number)
        return primeList
