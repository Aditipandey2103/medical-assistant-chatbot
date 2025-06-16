def count_primes_in_range(start, end):
    def is_prime(n):
        if n <= 1:  # 0 and 1 are not prime
            return False
        for i in range(2, int(n**0.5) + 1):  # Check divisors up to √n
            if n % i == 0:
                return False
        return True

    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1

    return count

# Count prime numbers from 1 to 50
prime_count = count_primes_in_range(1, 50)
print(f"Number of prime numbers between 1 and 50: {prime_count}")
tup1 = (1,2,3,4,5,6,7,8,9,10)

result = tuple(filter(lambda num:(num%2 == 0), tup1))
print("The filtered list of even numbers: ", result)
