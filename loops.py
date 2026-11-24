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