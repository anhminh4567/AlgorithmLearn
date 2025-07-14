
n1 = 3
n2= 15
n3 =0
n4=1
n5=2
n6 = 4
n7 = 5
def fibonacci(n):
    
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    return fibonacci(n - 1) + fibonacci( n - 2)

print(fibonacci(n1))

print(fibonacci(n2))
print(fibonacci(n3))
print(fibonacci(n4))
print(fibonacci(n5))
print(fibonacci(n6))

print(fibonacci(n7))

    
    
    