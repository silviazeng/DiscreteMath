def is_prime(n):
    return n != 1 and all(n % d != 0 for d in range(2, n))


print(next(n for n in range(2, 1000000) if
           not is_prime(n * n + n + 41)))