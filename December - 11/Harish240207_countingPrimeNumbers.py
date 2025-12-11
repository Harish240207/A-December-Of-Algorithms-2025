# December 11 - Counting Prime Numbers
# Input:  A single integer N
# Output: "The count of prime numbers less than N is: <value>"

import sys

def count_primes(N):
    if N <= 2:
        return 0

    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes
    p = 2
    while p * p < N:
        if is_prime[p]:
            for multiple in range(p * p, N, p):
                is_prime[multiple] = False
        p += 1

    return sum(is_prime)


def main():
    data = sys.stdin.read().strip()
    N = int(data)

    result = count_primes(N)
    print(f"The count of prime numbers less than {N} is: {result}")


if __name__ == "__main__":
    main()