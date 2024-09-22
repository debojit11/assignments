# Print out every prime number between 1 and 1000.
# Loop through numbers from 1 to 1000
for number in range(1, 1001):
    # Assume number is prime until proven otherwise
    is_prime = True
    # Check divisibility by any number from 2 to the number-1
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number)
