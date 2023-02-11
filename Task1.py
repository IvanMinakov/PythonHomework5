def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)


A = int(input("Enter a number (A): "))
B = int(input("Enter a power (B): "))

result = power(A, B)
print(f"{A}^{B} = {result}")