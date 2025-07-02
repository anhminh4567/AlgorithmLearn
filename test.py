import sys


# print(sys.path)
a: list[int] = [ 1, 3 , 6 , 4 ,1 ,2 ]
a.sort()
print(a)
for val in a:
    print(val)
    pass


def sol(A : list[int]) -> int:
    smallest = 1
    for i in A:
        if i == smallest:
            smallest += 1
    return smallest    
        
print(sol(a))  # 5