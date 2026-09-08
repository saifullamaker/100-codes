# 1. Get the upper limit from the user
limit = int(input("Print primes up to what number? "))

# 2. Check every number from 2 up to the limit
for num in range(2, limit + 1):
    is_prime = True
    
    # 3. Check if 'num' has any factors
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # Not prime, stop checking this number
            
    # 4. If it's prime, print it
    if is_prime:
        print(num, end=" ")
