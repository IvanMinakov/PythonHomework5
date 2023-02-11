def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a+1, b-1)

A = int(input("Enter first number (A): "))
B = int(input("Enter second number (B): "))

result = sum(A, B)
print(f"{A} + {B} = {result}")
