import math

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    max_factor = n**0.5
    while i <= max_factor:
        if n % i:
            i += 2
        else:
            n //= i
            factors.append(i)
            max_factor = n**0.5
    if n > 1:
        factors.append(n)
    return factors

def check(n, cache):
    if n in cache:
        return cache[n]
    test = prime_factors(n)
    for i in test:
        if n %(i**2) == 0:
            cache[n] = False
            return False
    cache[n] = True
    return True

L, R = map(int, input().split())

# cache đóng vai trò như một dictionary (nếu có sẵn trong cache thì sẽ bỏ qua không cần check lại bằng cách chạy vòng lặp)
cache = {}
special_numbers = [i for i in range(L, R + 1) if check(i, cache)]
special_set = set(special_numbers)
count = 0

for ind, i in enumerate(special_numbers):
    for j in special_numbers[ind+1:]:
        # Hàm gcd (https://www.w3schools.com/python/ref_math_gcd.asp)
        if (math.gcd(i, j) == 1 or (i * j) in special_set):
            count += 1 

print(count)