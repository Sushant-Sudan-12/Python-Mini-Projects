import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def minimize_penalty(arr):
    primes = []
    non_primes = []

    # Separate primes and non-primes
    for num in arr:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes.append(num)

    # Calculate penalty
    if len(primes) > len(non_primes):
        penalty = sum(sorted(primes)[:len(primes) - len(non_primes)])
    else:
        penalty = sum(sorted(non_primes)[:len(non_primes) - len(primes)])

    return penalty
# Example usage
n = int(input("Enter the size of the array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element {}: ".format(i+1))))
penalty = minimize_penalty(arr)
print("Penalty:", penalty)