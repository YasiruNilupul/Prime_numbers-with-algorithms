limit = 20000
is_prime = [True] * limit  # initialize a boolean list to mark all numbers as prime
is_prime[0] = is_prime[1] = False  # mark 0 and 1 as not prime

# sieve of eratosthenes algorithm to mark composite numbers
for i in range(2, int(limit**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, limit, i):
            is_prime[j] = False

# sum all prime numbers up to the limit
sum = 0
for i in range(2, limit):
    if is_prime[i]:
        sum += i

print(sum)

