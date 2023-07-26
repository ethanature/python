num = int(input("Enter a number: "))  # your number
factorial = 1  # var name - factorial
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of", num, "is", factorial)
