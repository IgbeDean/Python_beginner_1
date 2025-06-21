prime_numbers = []
non_prime_numbers = []

check_prime = int(input("Enter number range to check for prime or not: "))

def prime_num(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(check_prime + 1):
    if prime_num(i):
        prime_numbers.append(i)
    else:
        non_prime_numbers.append(i)

print("Prime numbers are:", prime_numbers)
print("Non-prime numbers are:", non_prime_numbers)