# Program 1: Print numbers from 1 to 10

for i in range(1, 11):
    print(i)


# Program 2: Multiplication table

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

    # Program 3: Find factorial of a number

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

# Program 4: Generate the first N Fibonacci numbers

n = int(input("Enter N: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

    # Program 5: Check if a number is prime

n = int(input("Enter a number: "))
prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime number")
else:
    print("Not a prime number")

    # Program 6: Reverse a number

n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reversed number =", reverse)

# Program 7: Count digits in a number

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1

print("Number of digits =", count)

# Program 8: Sum of even numbers between 1-100

sum = 0

for i in range(2, 101, 2):
    sum = sum + i

print("Sum of even numbers =", sum)

# Program 9: Print a pyramid pattern

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("* " * i)
    
    # Program 10: Find all divisors of a number

n = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)